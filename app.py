from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = '893f5f60-2ca8-4285-8af0-51b9fd9d43f7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

inscricoes = db.Table('inscricoes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    voluntarios = db.relationship('User', secondary=inscricoes, back_populates='projects')

    def __repr__(self):
        return f'<Project {self.title}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(256), nullable=False)
    projects = db.relationship('Project', secondary=inscricoes, back_populates='voluntarios')

    def __repr__(self):
        return f'<User {self.nome}>'

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

        flash('Cadastro realizado! Faça o login.', 'success')
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
        flash('Você precisa estar logado para se inscrever em um projeto.', 'danger')
        return redirect(url_for('login_cadastro'))

    projeto = Project.query.get_or_404(project_id)
    usuario = User.query.get(session['user_id'])

    if usuario in projeto.voluntarios:
        flash('Você já está inscrito neste projeto!', 'info')
        return redirect(url_for('detalhes_projeto', project_id=projeto.id))

    projeto.voluntarios.append(usuario)
    db.session.commit()

    flash('Inscrição realizada com sucesso!', 'success')
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)