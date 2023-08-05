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
    def __init__(self):
        self.conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE, port=DB_PORT,
                                    charset=DB_CHARSET)
        self.cursor = self.conn.cursor(DictCursor)

    def insert_comment_data(self, comment):
        sql = "INSERT INTO commentDetail (commentIconUrl, username, commentTimeAndSite, supportCount, commentContext, commentContextIconUrl) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (str(comment.commentIconUrl), str(comment.username), str(comment.commentTimeAndSite), str(comment.supportCount),
                str(comment.commentContext), str(comment.commentContextIconUrl))

        self.cursor.execute(sql, data)
        self.conn.commit()
    def insert_video_data(self,video):
        sql = "INSERT INTO videodetail (title,url, commentCount, likeCount, shareCount, collectCount, iconUrl) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (
        str(video.title), str(video.url), str(video.commentCount),
        str(video.likeCount),str(video.shareCount),str(video.collectCount),str(video.iconUrl))
        self.cursor.execute(sql, data)
        self.conn.commit()

