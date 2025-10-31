from flask import render_template, flash, redirect, url_for, session
from ..models import db, Project, User
from . import dp

@dp.route('/inscricao/confirmar/<int:project_id>')
def confirmacao_inscricao(project_id):
    projeto = Project.query.get_or_404(project_id)
    
    return render_template('confirmacao_inscricao.html', logged_in=('user_id' in session), project=projeto)

@dp.route('/inscrever/<int:project_id>', methods=['POST'])
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
