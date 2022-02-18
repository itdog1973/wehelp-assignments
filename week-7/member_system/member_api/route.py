from flask import Blueprint, redirect, render_template, session, request, flash, url_for
from member_system.users.member import Member
api = Blueprint('api',__name__)

@api.route('/members')
def get_member():
        username = request.args.get('username')
        user= Member.search_data_by_username(username)
        if user is None:
            return {'data':None}
        user_dict = {'id':user.id,'name':user.name,'username':user.username}
        return {'data':user_dict}

    

@api.route('/member',methods=["POST"])
def change_name():
    if 'name' in session:
        request_data = request.get_json()
        new_name = None
        if request_data:
            if 'name' in request_data:
                if len(request_data['name']) <1:
                    return {"error":True}
                new_name = request_data['name']    
                username = session['username']
                Member.update_name_to_db(update_name=new_name, current_username=username)

                return {"ok":True}
        else:
            return {"error":True}
    return redirect(url_for('home'))

