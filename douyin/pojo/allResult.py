
from douyin.pojo import commentDetail as comment
from douyin.pojo import videoDetail as video

class allResult:

    def __int__(self):
        self.comment = comment
        self.video = video
    def set_comment(self, comment):
        self.comment = comment

    def get_comment(self):
        return self.comment

    def set_video(self, video):
        self.video = video

    def get_video(self):
        return self.video



