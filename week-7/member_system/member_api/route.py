from flask import Blueprint, redirect, render_template, session, request, flash, url_for
from member_system.users.member import Member
api = Blueprint('api',__name__)

@api.route('/member', methods=['GET', 'POST'])
def get_member():
    if request.method == 'GET':
        username = request.args.get('username')
        user= Member.search_data_by_username(username)
        if user is None:
            return {'data':None}
        user_dict = {'id':user.id,'name':user.name,'username':user.username}
        return {'data':user_dict}

    if request.method =='POST':
        if 'name' in session:
            request_data = request.get_json()
            new_name = None
            if request_data:
                if 'name' in request_data:
                    if len(request_data['name']) <1:
                        return {"error":True}
                    new_name = request_data['name']    
                    username = session['username']
                    user_data = Member.search_data_by_username(username)
                    user_data.update_name_to_db(new_name)

                    return {"ok":True}
            else:
                return {"error":True}
        return redirect(url_for('home'))
