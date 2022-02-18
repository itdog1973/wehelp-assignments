from member_system.users.database import CursorFromConnection


class Member: # 建立使用者類別
    def __init__(self, name, username, password, id):
        self.name = name
        self.username=username
        self.password=password
        self.id = id
    def __repr__(self):
        return f"Member({self.name}, {self.username}, {self.password}"

    def save_to_db(self): # 開啟collection，開啟Cursor
        with CursorFromConnection() as cursor:
                cursor.execute('INSERT INTO member (name, username, password) VALUES (%s, %s, %s)',
                (self.name, self.username, self.password))

    def update_name_to_db(self, new_name):
        with CursorFromConnection() as cursor:
            print(new_name)
            cursor.execute('UPDATE member SET name = %s  WHERE username = %s',(new_name,self.username))
    
    @classmethod
    def search_data_by_username(cls,username):
        with CursorFromConnection() as cursor:
                cursor.execute('SELECT * FROM member WHERE username = %s', (username,))
                user_data = cursor.fetchone()
                if user_data != None: # 如果資料庫有這個使用者的資訊就建立這個物件
                    return cls(id = user_data[0],name=user_data[1],username=user_data[2],password=user_data[3])
                else:
                    return None # 沒有就回傳none
    
    