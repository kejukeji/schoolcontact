# coding: UTF-8

__author__ = 'Juingya'



from schoolcontact import app
from flask.ext import restful
from schoolcontact.controls.register_control import *
from .views.all_views import *

api = restful.Api(app)
app.add_url_rule('/login','login',login,methods=['GET','POST'])
app.add_url_rule('/register','register',register,methods=['GET','POST'])
app.add_url_rule('/register_action','register_action',register_action,methods=['GET','POST'])
app.add_url_rule('/login_in','login_in',login_in,methods=['GET','POST'])
app.add_url_rule('/show_massage/<int:stu_id>','show_message',show_message,methods=['GET','POST'])
app.add_url_rule('/save_message/<int:stu_id>','save_message',save_message,methods=['GET','POST'])
