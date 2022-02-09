from crypt import methods
from flask import redirect, render_template, session, request, flash, url_for
from member_system import app
import mysql.connector
import os
from member_system import database
from member_system.database import DbConnection


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', header_message='歡迎光臨，請註冊登入系統')


@app.route('/signup', methods=['POST'])
def signup():

    username=request.form.get("username")
    userid= request.form.get('userid')
    password= request.form.get('password')

    DB = DbConnection()
    result = DB.getUserId(userid)

    if result:
        DB.connectionClose()
        return render_template("error.html", title='Error', header_message='失敗頁面',error_message='帳號已經被註冊')

    DB.addUser(username,userid,password)
    DB.connectionClose()
    flash('註冊成功，請重新登入會員系統','sucess')
    return redirect(url_for('home'))


@app.route('/signin', methods=['POST'])
def signin():
    userid = request.form.get('userid')
    password = request.form.get('password')

    DB = DbConnection()
    result =DB.verifyUser(userid)
    if result:
        if userid == result[1] and password == result[2]:
            session['name'] = result[0]
            DB.connectionClose()
            return redirect(url_for('member'))
    else:
        DB.connectionClose()
        return redirect("/error/?message= 帳號或密碼輸入錯誤")
            

      

@app.route('/error/')
def error():
    error_message = request.args.get('message')
    return render_template('error.html',error_message=error_message,header_message='失敗頁面')
    


@app.route('/signout')
def signout():
    session.pop('name',None)
    return redirect(url_for('home'))


@app.route('/member')
def member():
    if 'name' in session:
        username= session['name']
        return render_template('member.html', title='Member Page', username=username, header_message="歡迎光臨，這是會員頁")
    flash('請你重新登入','danger') 
    return redirect(url_for('home'))

@app.errorhandler(404)
def file_not_found(error):
    return render_template("error.html",title="Page Cannot Find", header_message="找不到頁面")