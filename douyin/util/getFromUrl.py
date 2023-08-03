from douyin.pojo.videoDetail import videoDetail


class getFromUrl:
    def get_video(self, html_new):
        videoDe = videoDetail()
        soup = html_new.find(class_="xg-video-container")
        source = soup.find("source")
        videoDe.url = "https:" + source.get("src")

        soup1 = html_new.find(class_="Nu66P_ba").find_next("span").find_next("span").find_next("span").find_next("span")
        title = soup1.text
        videoDe.title = title

        soups = html_new.find_all(class_="CE7XkkTw")
        allCount = []
        for soup in soups:
            count = soup.text
            allCount.append(count)
        videoDe.likeCount = allCount[0]
        videoDe.commentCount = allCount[1]
        videoDe.collectCount = allCount[2]
        videoDe.shareCount = html_new.find(class_="Uehud9DZ").text
        videoDe.iconUrl = "https:" + html_new.find(class_="F55pZYYH QsTz7P83 avatar-component-avatar-container").find(
            "img").get("src")

        return videoDe