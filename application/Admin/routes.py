from application import app,db
import os
from sqlalchemy import text
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash,check_password_hash

from flask import Flask,request,Blueprint,jsonify,flash,render_template,redirect,url_for
from application.Admin.forms import LoginForm
from application.models import Users
from application.models import Products
from application.models import Categories
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import text


admin = Blueprint('admin', __name__,static_folder='../static')

def remove_file(file, type):
    file_name = file
    folder = os.path.join(app.root_path, "static/" + type + "/"+file_name)
    os.remove(folder)
    return 'File Has Been Removed'


def save_file(file, type):
    file_name = secure_filename(file.filename)
    file_ext = file_name.split(".")[1]
    folder = os.path.join(app.root_path, "static/" + type + "/")
    file_path = os.path.join(folder, file_name)
    try:
        file.save(file_path)
        return True, file_name
    except:
        return False, file_name





@admin.route('/',methods=['GET','POST'])
@login_required
def Home():
    hash_pw = generate_password_hash('Games587')

    if Users.query.filter_by(role='admin').count()==1:

        pass
    else:
        
        admin = Users(email='theadmin21@gmail.com',password=hash_pw,firstname="admin",role='admin')
        db.session.add(admin)
        db.session.commit()


    return render_template('home.html')





@admin.route('/login',methods=['GET', 'POST'])
def Login():
    useremail = request.form.get('useremail')
    userpassword = request.form.get('userpassword')
    hash_pw = generate_password_hash('Games587')

    if Users.query.filter_by(role='admin').count()==1:

        pass
    else:
        
        admin = Users(email='theadmin21@gmail.com',password=hash_pw,firstname="admin",role='admin')
        db.session.add(admin)
        db.session.commit()
        
  
    if current_user.is_authenticated:
        return redirect(url_for('admin.Home'))
    
    user = Users.query.filter_by(email=useremail).first()

    
    if user and check_password_hash(user.password,userpassword) and user.role == 'admin':
        
        login_user(user, False)
        return redirect(url_for('admin.Home'))
    else:
        flash('Login Unsuccessful. Please check email and password')
    return render_template('login.html')





@admin.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('admin.Login'))


@admin.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        new_category = Categories(category_name=category_name)
        db.session.add(new_category)
        db.session.commit()
    all_categories = Categories.query.all()
    return render_template('categories.html', all_categories=all_categories)


@admin.route('/delete_category/<int:id>', methods=['POST'])
def delete_category(id):
    if request.method == 'POST':
        category_name = Categories.query.get(id)
        db.session.delete(category_name)
        db.session.commit()
        return redirect(url_for('admin.add_category'))

@admin.route('/get_products', methods=['GET'])
def get_products():
    all_products = Products.query.all()
    return render_template('products.html', all_products=all_products)


@admin.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    if request.method == 'POST':
        product_name = Products.query.get(id)
        db.session.delete(product_name)
        db.session.commit()
        return redirect(url_for('admin.get_products'))


@admin.route('/get_sellers', methods=['GET'])
def get_sellers():
    sql = text("SELECT *, count(*) AS count_1 FROM users WHERE role = 'seller'")
    all_sellers = db.engine.execute(sql)
    return render_template('sellers.html', all_sellers=all_sellers)


@admin.route('/delete_seller/<int:id>', methods=['POST'])
def delete_seller(id):
    if request.method == 'POST':
        seller = Users.query.get(id)
        db.session.delete(seller)
        db.session.commit()
        return redirect(url_for('admin.get_sellers'))


@admin.route('/get_buyers', methods=['GET'])
def get_buyers():
    sql = text("SELECT *, count(*) AS count_1 FROM users WHERE role = 'buyer'")
    all_buyers = db.engine.execute(sql)
    return render_template('buyers.html', all_buyers=all_buyers)

@admin.route('/delete_buyer/<int:id>', methods=['POST'])
def delete_buyer(id):
    if request.method == 'POST':
        buyer = Users.query.get(id)
        db.session.delete(buyer)
        db.session.commit()
        return redirect(url_for('admin.get_buyers'))

