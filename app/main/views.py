from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from .. import db
import markdown2
from . import main
from ..models import Child,User
from .forms import UpdateProfile,PostChild
@main.route('/')
def index():
    title = 'Child'
    childs = Child.query.all()
    return render_template('index.html',childs = childs)
@main.route('/user/<uname>',methods=['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    childs = Child.query.filter_by(user_id=current_user.id).all()
    
    
    return render_template("index.html", user = user,childs = childs)