from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#criacao do empregado

class Empregado(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key = True)
    id_empregado = db.Column(db.Integer(), unique=True)
    nome = db.Column(db.String())
    idade = db.Column(db.Integer())
    posicao = db.Column(db.String(80))

    def __init__(self, id_empregado, nome, idade, posicao):
        self.id_empregado = id_empregado
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
    
    def __repr__(self):
        return f"{self.nome:{self.id_empregado}}"
        

