from flask import render_template, request, flash, redirect, url_for, session
from ..models import db, Project, Partner, Skill, User
from functools import wraps
from datetime import datetime
from . import dp

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Acesso negado. Por favor, faça o login como admin', 'danger')
            return redirect(url_for('main.login_cadastro'))
       
        user = User.query.get(session['user_id'])
        
        if not user.is_admin:
            flash('Você não tem permissão para acessar esta pagina.', 'danger')
            return redirect(url_for('main.homepage'))
        
        return f(*args, **kwargs)
    
    return decorated_function


@dp.route('/admin', methods=['GET', 'POST'])
@admin_required
def admin_page():
    if request.method == 'POST':
        title = request.form.get('title')
        location = request.form.get('location')
        description = request.form.get('description')
        status = request.form.get('status')
        work_date_str = request.form.get('work_date')
        
        work_date = datetime.strptime(work_date_str, '%Y-%m-%d').date() if work_date_str else None

        responsible_org = request.form.get('responsible_org')
        responsible_contact = request.form.get('responsible_contact')

        novo_projeto = Project(
            title=title, 
            location=location, 
            description=description, 
            status=status,
            work_date=work_date,
            responsible_org=responsible_org,
            responsible_contact=responsible_contact
        )

        skill_ids = request.form.getlist('skills')
        for skill_id in skill_ids:
            skill = Skill.query.get(skill_id)
            if skill:
                novo_projeto.required_skills.append(skill)
        
        db.session.add(novo_projeto)
        db.session.commit()

        flash(f'Projeto "{title}" criado com sucesso!', 'success')
        return redirect(url_for('main.admin_page'))

    all_projects = Project.query.order_by(Project.id.desc()).all()
    all_skills = Skill.query.all()
    return render_template('admin.html', logged_in=True, projects=all_projects, skills=all_skills)

@dp.route('/admin/delete/<int:project_id>', methods=['POST'])
@admin_required
def delete_project(project_id):
    projeto_para_deletar = Project.query.get_or_404(project_id)
    db.session.delete(projeto_para_deletar)
    db.session.commit()
    flash(f'Projeto "{projeto_para_deletar.title}" foi deletado.', 'success')
    return redirect(url_for('main.admin_page'))

@dp.route('/admin/project/<int:project_id>/volunteers')
@admin_required
def view_volunteers(project_id):
    projeto = Project.query.get_or_404(project_id)
    return render_template('volunteers.html', project=projeto, logged_in=True)

@dp.route('/admin/add_skill', methods=['POST'])
@admin_required
def add_skill():
    skill_name = request.form.get('skill_name')
    
    if not skill_name or skill_name.strip() == "":
        flash('O nome da habilidade não pode estar vazio.', 'danger')
        return redirect(url_for('main.admin_page'))
    
    existing_skill = Skill.query.filter(Skill.name.ilike(skill_name)).first()
    if existing_skill:
        flash(f'A habilidade "{skill_name}" já existe.', 'warning')
        return redirect(url_for('main.admin_page'))
    
    new_skill = Skill(name=skill_name.strip())
    db.session.add(new_skill)
    db.session.commit()
    flash(f'Habilidade "{skill_name}" adicionada com sucesso!', 'success')
    return redirect(url_for('main.admin_page'))

@dp.route('/admin/delete_skill/<int:skill_id>', methods=['POST'])
@admin_required
def delete_skill(skill_id):
    skill_to_delete = Skill.query.get_or_404(skill_id)
    
    db.session.delete(skill_to_delete)
    db.session.commit()
    flash(f'Habilidade "{skill_to_delete}" deletada.', 'success')
    return redirect(url_for('main.admin_page'))

@dp.route('/admin/parceiros')
@admin_required
def admin_parceiros():
    parceiros = Partner.query.all()
    # telefone = Partner.
    
    return render_template('admin_parceiros.html', title='Gestão de Parceiros', parceiros=parceiros)

@dp.route('/admin/excluir-parceiro/<int:partner_id>', methods=['POST'])
@admin_required
def excluir_parceiro(partner_id):
    parceiro_para_excluir = Partner.query.get_or_404(partner_id)
    
    try:
        db.session.delete(parceiro_para_excluir)
        db.session.commit()
        flash('Parceiro excluído com sucesso.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir parceiro: {e}', 'error')
    
    return redirect(url_for('main.admin_parceiros'))