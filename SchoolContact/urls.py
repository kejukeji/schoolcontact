# coding: UTF-8

__author__ = 'Juingya'



from SchoolContact import app
from flask.ext import restful
from SchoolContact.controls.register_control import *
from SchoolContact.controls.reset_password import *
from SchoolContact.controls.select import *
from .views.all_views import *
from .views.reset_password_view import *
from .restfuls.verify import weixin
from SchoolContact.restfuls.get_access_token import get_token

api = restful.Api(app)
app.add_url_rule('/login','login',login,methods=['GET','POST'])
app.add_url_rule('/register','register',register,methods=['GET','POST'])
app.add_url_rule('/change/<int:stu_id>','change',change,methods=['GET','POST'])
app.add_url_rule('/register_action','register_action',register_action,methods=['GET','POST'])
app.add_url_rule('/login_in','login_in',login_in,methods=['GET','POST'])
app.add_url_rule('/show_massage/<int:stu_id>','show_message',show_message,methods=['GET','POST'])
app.add_url_rule('/save_message/<int:stu_id>','save_message',save_message,methods=['GET','POST'])
app.add_url_rule('/weixin', 'weixin', weixin, methods=['GET','POST'])
app.add_url_rule('/change_message/<int:stu_id>','change_message',change_message,methods=['GET','POST'])
app.add_url_rule('/reset/<int:stu_id>','reset_password_view',reset_password_view,methods=['GET','POST'])
app.add_url_rule('/resetpassword/<int:stu_id>','resetpassword',reset_password,methods=['GET','POST'])
app.add_url_rule('/select_student','select_student',select_student,methods=['GET','POST'])
app.add_url_rule('/select_page','select',select,methods=['GET','POST'])
app.add_url_rule('/oauth', 'oauth', get_token, methods=('GET', 'POST'))
