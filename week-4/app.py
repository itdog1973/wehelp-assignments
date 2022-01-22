from crypt import methods
from flask import Flask
from flask import request 
from flask import redirect 
from flask import render_template
from flask import session
import json
from flask import url_for
app=Flask(__name__,static_folder="public",static_url_path="/")
# 入方法目前使用 session， 同學做完的可以研究一下 cookie session JWT 差別，尤其 JWT 算是目前蠻常用的身分辨識方式
app.secret_key="flask secret"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    id = request.form["user_id"]
    password = request.form["user_password"]
    if id == "" or password == "":
        return redirect("/error/?message=請輸入帳號、密碼")
    elif id =="test" and password =="test":
        session['user_id']=id
        session['passowrd']=password
        return redirect(url_for("member"))
    elif id !="test" or password !="test":
        return redirect("/error?message=帳號、或密碼輸入錯誤")
        

@app.route("/error/")
def error():
    message = request.args.get("message", "")
    return render_template("error.html",message=message)

@app.route("/member/")
def member():
    if "user_id" in session:
        return render_template("member.html",message=f"恭喜{session['user_id']}，成功登入系統")
    return redirect(url_for("index"))

@app.route("/signout")
def signout():
    session.pop("user_id", None)
    return redirect(url_for("index"))









app.run(port=3000)