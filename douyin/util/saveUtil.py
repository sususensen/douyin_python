class saveUtil:
    def save_video(self,video):
        try:
            with open('video/' + '1.mp4', 'wb') as f:
                f.write(video)
        except Exception as err:
            # 跳过错误代码
            pass
    def save_video_icon(self,icon):
        try:
            with open('video/' + '1.jpeg', 'wb') as f:
                f.write(icon)
        except Exception as err:
            # 跳过错误代码
            pass