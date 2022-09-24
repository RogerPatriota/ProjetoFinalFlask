from  flask import Blueprint

ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/')
def home():
    return 'Firts Page'