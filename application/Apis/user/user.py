from application import db,app
from flask import Flask,request,Blueprint,jsonify
from application.models import Users,UsersSchema
from werkzeug.security import generate_password_hash,check_password_hash

import os
from sqlalchemy import text
from datetime import datetime
from werkzeug.utils import secure_filename
import smtplib
import random
import requests


def SignUp():
    role = request.form.get('role')
    phone_number = request.form.get('phone_number')

    if role == 'seller':
        company_name = request.form.get('company_name')
        company_initials = request.form.get('company_initials')
        email = request.form.get('email')
        password = request.form.get('password')
        primary_contact = request.form.get('primary_contact')
        postal_code = request.form.get('postal_code')
        hash_pw = generate_password_hash(password)
        user = Users.query.filter_by(phone_no=phone_number).first()
        if user:
            return jsonify({
                "msg":"Phone Number Already Exists.Please Try Another One"
            })
        else:
            user = Users(email=email, phone_no=phone_number,companyinitials=company_initials,companyname=company_name,password=hash_pw,primary_contact=primary_contact,role='seller',postal_code=postal_code)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                "msg":"User Registered Successfully"
            })

    else:
        user = Users.query.filter_by(phone_no=phone_number).first()
        if user:
            return jsonify({
                "msg":"Phone Number Already Exists.Please Try Another One"
            })
        else:
            firstname = request.form.get('first_name')
            lastname = request.form.get('last_name')
            password = request.form.get('password')
            email = request.form.get('email')
            print(email)
            
            primary_contact = request.form.get('primary_contact')
            postal_code = request.form.get('postal_code')
            hash_pw = generate_password_hash(password)
            
            user = Users(email=email, phone_no=phone_number, primary_contact=primary_contact, postal_code=postal_code,firstname=firstname, lastname=lastname, password=hash_pw,role=role)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                "msg":"User Registered Successfully"
            })



def SignIn():
    phone_no = request.form.get('phone_no')
    password = request.form.get('password')
    
    user = Users.query.filter_by(phone_no=phone_no).first()
    if user and check_password_hash(user.password,password) and user.role !="admin":
        users_schema = UsersSchema(many=False)
        user = users_schema.dump(user)
        return jsonify({
            "user":user,
            "msg":"success"
        })
    else:
        return jsonify({
            "msg":"not found"
        })



def Profile():
    user_id = request.args.get('user_id')
    user = Users.query.filter_by(id=user_id).first()
    users_schema = UsersSchema(many=False)
    user = users_schema.dump(user)
    return jsonify({
        "user":user
    })