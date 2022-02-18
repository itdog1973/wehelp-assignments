
from flask import redirect, render_template, session, request, flash, url_for, Blueprint
import mysql.connector
import os
from member_system.users.member import Member
from member_system.users.database import Database
#建立coonection pool
Database.initialise(host=f'{os.getenv("HOST")}', user=f'{os.getenv("USERDB")}', password=f'{os.getenv("PASSWORD")}', database=f'{os.getenv("DATABASE")}')

users = Blueprint('users',__name__)


@users.route('/signup', methods=['POST'])
def signup():

    name=request.form.get('name')
    username= request.form.get('username')
    password= request.form.get('password')
    
    
    # 搜尋使用者的ID，如果沒有在資料庫就建立user object, 擁有search方法和insert方法， 如果有就Fetch出來
    user = Member.search_data_by_username(username)

    print(name)

    if user:
        return redirect('/error/?message=帳號已被註冊')


    user = Member(name, username, password, None)
    #建立user object, 擁有search方法和insert方法
    user.save_to_db() #add data to db
    

    flash('註冊成功，請重新登入會員系統','sucess')
    return redirect(url_for('main.home'))


@users.route('/signin', methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    user = Member.search_data_by_username(username)
    if user:
        if user.username == username and user.password == password:
            session['name'] = user.name
            session['username'] = user.username
            return redirect(url_for('users.member'))
        else:
            return redirect('/error/?message=帳號或密碼錯誤')

    else:
        return redirect('/error/?message=帳號不存在')
            

      

@users.route('/error/')
def error():
    error_message = request.args.get('message')
    return render_template('error.html',error_message=error_message,header_message='失敗頁面')
    


@users.route('/signout')
def signout():
    session.pop('name',None)
    return redirect(url_for('main.home'))


@users.route('/member')
def member():
    if 'name' in session:
        username= session['name']
        return render_template('member.html', title='Member Page', username=username, header_message='歡迎光臨，這是會員頁')
    flash('請你重新登入','danger') 
    return redirect(url_for('main.home'))