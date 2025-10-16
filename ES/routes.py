from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Project, Partner, Skill
from functools import wraps
from datetime import datetime   

main = Blueprint('main', __name__)

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


@main.route('/')
def homepage():
    projetos_destaque = Project.query.limit(3).all()
    return render_template('index.html', logged_in=('user_id' in session), projects=projetos_destaque)

@main.route('/projetos')
def projetos():
    todos_os_projetos = Project.query.all()
    return render_template('projetos.html', logged_in=('user_id' in session), projects=todos_os_projetos)

@main.route('/parceiros')
def parceiros():
    return render_template('parceiros.html', logged_in=('user_id' in session))

@main.route('/projetos/<int:project_id>')
def detalhes_projeto(project_id):
    projeto = Project.query.get_or_404(project_id)
    
    return render_template('detalhes_projeto.html', logged_in=('user_id' in session), project=projeto)

@main.route('/login_cadastro', methods=['GET', 'POST'])
def login_cadastro():
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha_hash = generate_password_hash(senha)
        user_exists = User.query.filter_by(email=email).first()
        
        if user_exists:
            flash('Email já está cadastrado, tente outro.', 'danger')
            return redirect(url_for('main.login_cadastro'))
        
        novo_usuario = User(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado! Faça o login.', 'success')
        
        return redirect(url_for('main.login_cadastro'))
    
    return render_template('login_cadastro.html', logged_in=('user_id' in session))

@main.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.senha, senha):
        session['user_id'] = user.id
        session['user_name'] = user.nome
        
        if user.is_admin:
            flash(f'Bem-vindo(a), Administrador {user.nome}!', 'success')
            return redirect(url_for('main.admin_page'))
        else:
            flash(f'Login bem-sucedido! Bem-vindo(a) de volta, {user.nome}.', 'success')
            return redirect(url_for('main.homepage'))
    else:
        flash('Email ou senha inválidos. Por favor, tente novamente.', 'danger')
        return redirect(url_for('main.login_cadastro'))
    
@main.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da sua conta.', 'info')
    
    return redirect(url_for('main.homepage'))

@main.route('/login_cadastro_parceiro', methods=['GET', 'POST'])
def login_cadastro_parceiro():
    if request.method == 'POST':
        org_name = request.form.get('org_name')
        cnpj = request.form.get('cnpj')
        responsible_name = request.form.get('responsible_name')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        partner_exists = Partner.query.filter((Partner.email == email) | (Partner.cnpj == cnpj)).first()
        
        if partner_exists:
            flash('Este Email ou CNPJ já está em uso.', 'danger')
            return redirect(url_for('main.login_cadastro_parceiro'))
        
        senha_hash = generate_password_hash(senha)
        
        novo_parceiro = Partner(
            org_name=org_name,
            cnpj=cnpj,
            responsible_name=responsible_name,
            email=email,
            senha=senha_hash
        )
        
        db.session.add(novo_parceiro)
        db.session.commit()
        
        flash('Organização cadastrada com sucesso! Faça o login.', 'success')
        return redirect(url_for('main.login_cadastro_parceiro'))
    
    return render_template('login_cadastro_parceiro.html', logged_in=('user_id' in session))

@main.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html', logged_in=('user_id' in session))

@main.route('/inscricao/confirmar/<int:project_id>')
def confirmacao_inscricao(project_id):
    projeto = Project.query.get_or_404(project_id)
    
    return render_template('confirmacao_inscricao.html', logged_in=('user_id' in session), project=projeto)

@main.route('/inscrever/<int:project_id>', methods=['POST'])
def inscrever(project_id):
    
    if 'user_id' not in session:
        flash('Você precisa estar logado para se inscrever em um projeto.', 'danger')
        return redirect(url_for('main.login_cadastro'))
    
    projeto = Project.query.get_or_404(project_id)
    usuario = User.query.get(session['user_id'])
    
    if usuario in projeto.voluntarios:
        flash('Você já está inscrito neste projeto!', 'info')
        return redirect(url_for('main.detalhes_projeto', project_id=projeto.id))
    
    projeto.voluntarios.append(usuario)
    db.session.commit()
    flash('Inscrição realizada com sucesso!', 'success')
    
    return redirect(url_for('main.homepage'))

@main.route('/perfil')
def perfil():
    if 'user_id' not in session:
        flash('Você precisa fazer login para acessar esta página.', 'warning')
        return redirect(url_for('main.login_cadastro'))
    
    usuario_logado = User.query.get(session['user_id'])
    
    return render_template('perfil.html', logged_in=True, user=usuario_logado)       

@main.route('/admin', methods=['GET', 'POST'])
@admin_required
def admin_page():
    if request.method == 'POST':
        title = request.form.get('title')
        location = request.form.get('location')
        description = request.form.get('description')
        status = request.form.get('status')
        work_date_str = request.form.get('work_date')
        
        work_date = datetime.strptime(work_date_str, '%Y-%m-%d').date() if work_date_str else None

        novo_projeto = Project(
            title=title, 
            location=location, 
            description=description, 
            status=status,
            work_date=work_date
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

@main.route('/admin/delete/<int:project_id>', methods=['POST'])
@admin_required
def delete_project(project_id):
    projeto_para_deletar = Project.query.get_or_404(project_id)
    db.session.delete(projeto_para_deletar)
    db.session.commit()
    flash(f'Projeto "{projeto_para_deletar.title}" foi deletado.', 'success')
    return redirect(url_for('main.admin_page'))

@main.route('/admin/project/<int:project_id>/volunteers')
@admin_required
def view_volunteers(project_id):
    projeto = Project.query.get_or_404(project_id)
    return render_template('volunteers.html', project=projeto, logged_in=True)