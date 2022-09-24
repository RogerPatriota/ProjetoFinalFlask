from ..extensions import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(40))

    def __repr__(self) -> str:
        return "<Usuario(nome={}, email={}, senha ={})>".format(self.nome, self.email, self.senha)
    