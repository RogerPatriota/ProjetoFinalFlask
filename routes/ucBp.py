from  flask import Blueprint, render_template, request ,redirect, url_for, flash
from ..extensions import db
from ..models.usuario import Usuario

ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/')
def home(user_Id=0):
    #db.create_all()
    # filtra do banco pelo id quem vai vir
    # pega o nome do usuario
    # passa no html
    user_query = Usuario.query.filter_by(id = user_Id).first()
    return render_template('home_page.html', user=user_query)

@ucBp.route('/<user_Id>')
def home_logged(user_Id):
    user_query = Usuario.query.filter_by(id = user_Id).first()
    
    return render_template('home_page.html', user=user_query)

@ucBp.route('/register')
def signup():
    return render_template('register_page.html')

@ucBp.route('/add', methods=["POST"])
def valida_registro():
    uNome = request.form["nome"]
    uEmail = request.form["email"]
    uSenha = request.form["senha"]

    user =  Usuario(nome=uNome, email=uEmail, senha=uSenha)
    db.session.add(user)
    db.session.commit()

    user_query = Usuario.query.filter_by(email = uEmail).first()
    uId = user_query.id

    return redirect(url_for("ucBp.home_logged", user_Id=uId))


@ucBp.route('/login')
def login():
    return render_template('login_page.html')

@ucBp.route('/vld', methods=['POST'])
def valida_login():
    uEmail = request.form["email"]
    uSenha = request.form["senha"]

    user_query = Usuario.query.filter_by(email = uEmail, senha = uSenha).first()
    if user_query == None:
        flash('')
        return redirect(url_for('ucBp.login'))
    else:
        uId = user_query.id
        return redirect(url_for("ucBp.home_logged", user_Id=uId))


@ucBp.route('/update/<user_Id>')
def update(user_Id):
    user_query = Usuario.query.filter_by(id = user_Id).first()
    return render_template('update_page.html', user=user_query)

@ucBp.route('/upd', methods=['POST'])
def update_user():
    uId = request.form["id"]
    uNome = request.form["nome"]
    uEmail = request.form["email"]
    uSenha = request.form["senha"]

    user_query = Usuario.query.filter_by(id = uId).first()

    user_query.nome = uNome
    user_query.email = uEmail
    user_query.senha = uSenha
    db.session.add(user_query)
    db.session.commit()

    return redirect(url_for("ucBp.home_logged", user_Id=uId))

@ucBp.route('/delete/<user_Id>')
def delete(user_Id=0):
    user_query = Usuario.query.filter_by(id = user_Id).first()
    return render_template('delete_page.html', user=user_query)

@ucBp.route('/deletar', methods=['POST'])
def delete_user():

    uId = request.form['id']
    user_query = Usuario.query.filter_by(id = uId).first()
    db.session.delete(user_query)
    db.session.commit()

    return redirect(url_for('ucBp.home'))

@ucBp.route('/contruction')
def contruction():
    return render_template('construction_page.html')