import pymysql
from pymysql.cursors import DictCursor

from douyin.pojo.commentDetail import commentDetail

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "susen666"
DB_PORT = 3306
DB_DATABASE = "db01"
DB_CHARSET = 'utf8mb4'
VPN_IP = "127.0.0.1"
VPN_PORT = "7890"
class DataBase:
    #初始化连接数据库db01
    def __init__(self, host, port, user, passwd, database, charset):
        self.conn = pymysql.connect(host=host, user=user, password=passwd, database=database, port=port,
                                    charset=charset)
        self.cursor = self.conn.cursor(DictCursor)

    def insert_data(self):
        sql = "insert into commentDetail values ('https://baidu.com','苏森','2023-8-4','80','第一次测试，希望成功','百度一下，你就知道')"  # 这种写法自增字段和隐藏字段都要写出来
        self.cursor.execute(sql);
        self.conn.commit()


database=DataBase(DB_HOST,DB_PORT,DB_USER,DB_PASSWORD,DB_DATABASE,DB_CHARSET)
comment=commentDetail().__int__('https://baidu.com',"苏森","2023-8-4",'80',"第一次测试，希望成功","百度一下，你就知道")
database.insert_data()