from  flask import Blueprint, render_template
from ..extensions import db
from ..models.usuario import Usuario

ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/')
def home():
    #db.create_all()
    # filtra do banco pelo id quem vai vir
    # pega o nome do usuario
    # passa no html
    return render_template('home/home_page.html')

@ucBp.route('/teste')
def teste():
    return render_template('base_logged.html')