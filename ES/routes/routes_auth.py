from flask import render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, User, Partner, Skill
from . import dp

@dp.route('/login_cadastro', methods=['GET', 'POST'])
def login_cadastro():
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        course = request.form.get('course')
        semester_str = request.form.get('semester')
        skill_ids = request.form.getlist('skills')
        
        semester = int(semester_str) if semester_str else None
        
        senha_hash = generate_password_hash(senha)
        user_exists = User.query.filter_by(email=email).first()
        
        if user_exists:
            flash('Email já está cadastrado, tente outro.', 'danger')
            return redirect(url_for('main.login_cadastro'))
        
        novo_usuario = User(
            nome=nome, 
            email=email, 
            senha=senha_hash,
            course=course,
            semester=semester
        )
        
        for skill_id in skill_ids:
            skill = Skill.query.get(skill_id)
            if skill:
                novo_usuario.skills.append(skill)
                
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado! Faça o login.', 'success')
        return redirect(url_for('main.login_cadastro'))
    
    all_skills = Skill.query.all()  
    return render_template('login_cadastro.html', logged_in=('user_id' in session), skills=all_skills)

@dp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.senha, senha):
        session['user_id'] = user.id
        session['user_name'] = user.nome
        
        print('teste para administrador')
        print(f'administrador "{user.is_admin}"')
        print(f'usuario do sistema "{user.nome}"')
        if user.is_admin:
            flash(f'Bem-vindo(a), Administrador {user.nome}!', 'success')
            return redirect(url_for('main.admin_page'))
        else:
            flash(f'Login bem-sucedido! Bem-vindo(a) de volta, {user.nome}.', 'success')
            return redirect(url_for('main.homepage'))
    else:
        flash('Email ou senha inválidos. Por favor, tente novamente.', 'danger')
        return redirect(url_for('main.login_cadastro'))
    
@dp.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da sua conta.', 'info')
    
    return redirect(url_for('main.homepage'))

@dp.route('/login_cadastro_parceiro', methods=['GET', 'POST'])
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
        
        flash('Organização cadastrada com sucesso!.', 'success')
        return redirect(url_for('main.homepage'))
    
    return render_template('login_cadastro_parceiro.html', logged_in=('user_id' in session))
