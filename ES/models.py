from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

inscricoes = db.Table('inscricoes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

project_skills = db.Table('project_skills',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Skill {self.name}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    
    status = db.Column(db.String(50), nullable=False, default='Não Inicializada')
    work_date = db.Column(db.Date, nullable=True)
    
    voluntarios = db.relationship('User', secondary=inscricoes, back_populates='projects')
    required_skills = db.relationship('Skill', secondary=project_skills, lazy='subquery', backref=db.backref('projects', lazy=True))

    def __repr__(self):
        return f'<Project {self.title}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(256), nullable=False)
    projects = db.relationship('Project', secondary=inscricoes, back_populates='voluntarios')
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User {self.nome}>'
    
class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=True)
    responsible_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Partner {self.org_name}>'