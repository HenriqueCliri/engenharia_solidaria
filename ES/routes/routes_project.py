from flask import render_template, flash, redirect, url_for, session
from ..models import db, Project, Skill, User
from . import dp

@dp.route('/')
def homepage():
    projetos_destaque = Project.query.limit(3).all()
    return render_template('index.html', logged_in=('user_id' in session), projects=projetos_destaque)

@dp.route('/projetos')
def projetos():
    todos_os_projetos = Project.query.all()
    
    todas_as_skills = Skill.query.order_by(Skill.name).all()
    locations_tuples = db.session.query(Project.location).distinct().order_by(Project.location).all()
    todas_as_localizacoes = [loc[0] for loc in locations_tuples if loc[0]]
    
    return render_template(
        'projetos.html', 
        logged_in=('user_id' in session), 
        projects=todos_os_projetos,
        skills=todas_as_skills,
        locations=todas_as_localizacoes
    )

@dp.route('/projetos/<int:project_id>')
def detalhes_projeto(project_id):
    projeto = Project.query.get_or_404(project_id)
    
    return render_template('detalhes_projeto.html', logged_in=('user_id' in session), project=projeto)

@dp.route('/sobre_nos')
def sobre_nos():
    return render_template('sobre_nos.html', logged_in=('user_id' in session))

@dp.route('/parceiros')
def parceiros():
    return render_template('parceiros.html', logged_in=('user_id' in session))

@dp.route('/perfil')
def perfil():
    if 'user_id' not in session:
        flash('Você precisa fazer login para acessar esta página.', 'warning')
        return redirect(url_for('main.login_cadastro'))
    
    usuario_logado = User.query.get(session['user_id'])
    
    return render_template('perfil.html', logged_in=True, user=usuario_logado)       
