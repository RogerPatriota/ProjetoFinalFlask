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
    return render_template('home_page.html')

@ucBp.route('/login')
def login():
    return render_template('login_page.html')

@ucBp.route('/register')
def signup():
    return render_template('register_page.html')

@ucBp.route('/update')
def update():
    return render_template('update_page.html')

@ucBp.route('/contruction')
def contruction():
    return render_template('construction_page.html')