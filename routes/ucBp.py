from  flask import Blueprint
from ..extensions import db
from ..models.usuario import Usuario

ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/')
def home():
    db.create_all()
    return 'Firts Page'