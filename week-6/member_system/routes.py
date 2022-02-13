from crypt import methods
from flask import redirect, render_template, session, request, flash, url_for
from member_system import app
import mysql.connector
import os
from member_system import database
from member_system.member import Member
from member_system.database import Database
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', header_message='歡迎光臨，請註冊登入系統')


@app.route('/signup', methods=['POST'])
def signup():

    username=request.form.get("username")
    userid= request.form.get('userid')
    password= request.form.get('password')
    #建立coonection pool
    Database.initialise(host=f'{os.getenv("HOST")}', user=f'{os.getenv("USERDB")}', password=f'{os.getenv("PASSWORD")}', database=f'{os.getenv("DATABASE")}')
    
    # 搜尋使用者的ID，如果沒有在資料庫就建立user object, 擁有search方法和insert方法， 如果有就Fetch出來
    user = Member.search_data_by_id(userid)


    if user:
        return redirect("/error/?message=帳號已被註冊")


    user = Member(username, userid, password)
    #建立user object, 擁有search方法和insert方法
    user.save_to_db() #add data to db
    

    flash('註冊成功，請重新登入會員系統','sucess')
    return redirect(url_for('home'))


@app.route('/signin', methods=['POST'])
def signin():
    userid = request.form.get('userid')
    password = request.form.get('password')
    Database.initialise(host='localhost', user='root', password='12345678', database='website')
    user = Member.search_data_by_id(userid)
    if user:
        if user.usernmae == userid and user.password == password:
            session['name'] = user.name
            return redirect(url_for('member'))
        else:
            return redirect('/error/?message=帳號或密碼錯誤')

    else:
        return redirect('/error/?message=帳號不存在')
            

      

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