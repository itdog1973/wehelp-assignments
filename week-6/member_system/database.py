import mysql.connector
from mysql.connector import pooling


class Database: # 控制資料庫的時機
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs): 
        cls.__connection_pool = pooling.MySQLConnectionPool(pool_name='my_pool', **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.get_connection()

    @staticmethod
    def return_connection(connection):
        connection.close()

    @classmethod
    def close_all_connection(cls):
        cls.connection_pool.closeall()

class CursorFromConnection: # 配合with cluase使用
    def __init__(self):
        self.connection = None
        self.cursor = None
    def __enter__(self): # 執行With的時候就建立collection Pool
        self.connection=Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor #回傳cursor 
    def __exit__(self, exception_type, exception_value,exception_traceback):

        if exception_value is not None:
            self.connection.rollback() # 如果在與database互動的期間有任何error出現， 就把所有儲存在collection裏面的data全部刪除
        else:
            self.cursor.close() 
            self.connection.commit()
        Database.return_connection(self.connection) # 無論最後成功與否都會把collection放回去collection pool裏邊
