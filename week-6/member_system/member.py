from member_system.database import CursorFromConnection


class Member: # 建立使用者類別
    def __init__(self, name, username, password):
        self.name = name
        self.usernmae=username
        self.password=password
    def __repr__(self):
        return f"Member({self.name}, {self.usernmae}, {self.password}"

    def save_to_db(self): # 開啟collection，開啟Cursor
        with CursorFromConnection() as cursor:
                cursor.execute('INSERT INTO member (name, username, password) VALUES (%s, %s, %s)',
                (self.name, self.usernmae, self.password))

    
    @classmethod
    def search_data_by_id(cls,id):
        with CursorFromConnection() as cursor:
                cursor.execute('SELECT * FROM member WHERE username = %s', (id,))
                user_data = cursor.fetchone()
                if user_data != None: # 如果資料庫有這個使用者的資訊就建立這個物件
                    return cls(name=user_data[1],username=user_data[2],password=user_data[3])
                else:
                    return None # 沒有就回傳none