from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def routes(Project, User, db):
    @app.route('/')
    def homepage():
        projetos_destaque = Project.query.limit(3).all()

        return render_template(
            'index.html',
            logged_in=('user_id' in session),
            projects=projetos_destaque
        )

    @app.route('/projetos')
    def projetos():
        
        todos_os_projetos = Project.query.all()
        return render_template('projetos.html', logged_in=('user_id' in session), projects=todos_os_projetos)

    @app.route('/parceiros')
    def parceiros():
        return render_template('parceiros.html', logged_in=('user_id' in session))

    @app.route('/projetos/<int:project_id>')
    def detalhes_projeto(project_id):

        projeto = Project.query.get_or_404(project_id)
        return render_template('detalhes_projeto.html', logged_in=('user_id' in session), project=projeto)

    @app.route('/login_cadastro', methods=['GET', 'POST'])
    def login_cadastro():

        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')

            senha_hash = generate_password_hash(senha)

            user_exists = User.query.filter_by(email=email).first()

            if user_exists:
                flash('Email já está cadastrado, tente outro.', 'danger')
                return redirect(url_for('login_cadastro'))
            
            novo_usuario = User(nome=nome, email=email, senha=senha_hash)
            db.session.add(novo_usuario)
            db.session.commit()

            flash('Cadastro realizado! Faça o login.', 'sucess')
            return redirect(url_for('login_cadastro'))

        return render_template('login_cadastro.html', logged_in=('user_id' in session))

    @app.route('/login', methods=['POST'])
    def login():
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.senha, senha):
            
            session['user_id'] = user.id
            session['user_name'] = user.nome
            
            flash(f'Login deu certo!, bem-vindo(a) {user.nome}', 'success')
            
            return redirect(url_for('homepage'))
        else:
            flash('Email ou senha inválidos. por favor tente novamente', 'danger')
            return redirect(url_for('login_cadastro'))
        
    @app.route('/logout')
    def logout():
        session.clear()
        flash('Você saiu da sua conta.', 'info')
        return redirect(url_for('homepage'))

    @app.route('/login_cadastro_parceiro')
    def login_cadastro_parceiro():
        return render_template('login_cadastro_parceiro.html', logged_in=('user_id' in session))

    @app.route('/sobre_nos')
    def sobre_nos():
        return render_template('sobre_nos.html', logged_in=('user_id' in session))

    @app.route('/inscricao/confirmar/<int:project_id>')
    def confirmacao_inscricao(project_id):

        projeto = Project.query.get_or_404(project_id)
        return render_template('confirmacao_inscricao.html', logged_in=('user_id' in session), project=projeto)

    @app.route('/inscrever/<int:project_id>', methods=['POST'])
    def inscrever(project_id):
        
        if 'user_id' not in session:
            flash('Você precisa estar logado para ser inscrever em um projeto.')
            return redirect(url_for('login_cadastro'))
        
        projeto = Project.query.get_or_404(project_id)
        usuario = User.query.get(session['user_id'])

        if usuario in projeto.voluntarios:
            flash('Você já está inscrito nesse projeto!', 'info')
            return redirect(url_for('detalhes_projeto', project=projeto.id))
        
        projeto.voluntarios.append(usuario)
        db.session.commit()

        flash('Inscrição realizada com sucesso!', 'success')
        return redirect(url_for('projetos'))


    if __name__ == '__main__':
        app.run(debug=True)