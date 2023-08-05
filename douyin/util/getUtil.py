from douyin.pojo.commentDetail import commentDetail
from douyin.pojo.videoDetail import videoDetail
from douyin.util.help工具.helpMe import helpMe


class getUtil:

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

    def get_comment(self, html_new):

        commentDes = []

        commentList = html_new.find_all(class_="CDx534Ub")
        for comment in commentList:
            # 创建对象实例
            commentDe = commentDetail()
            # 获取评论头像
            commentDe.commentIconUrl = "https:" + comment.find(class_="V3cGkKvu comment-item-avatar").find("a").get(
                "href")
            # 获取评论名字
            commentDe.username = helpMe.get_lowest_span(comment, "Nu66P_ba NCRZnxVF").text
            # 获取评论内容（文本+图标url）
            tempRoad = comment.find(class_="VD5Aa1A1")
            context = helpMe.get_lowest_span(tempRoad, "Nu66P_ba")
            commentDe.commentContext = context.text
            urlsItem = comment.find_all(class_="jZ9bChTp")

            # 属于是踩坑了
            iconUrls = []
            # 有可能是空的好吧，有可能没有表情包
            if (urlsItem != None):
                for urlItem in urlsItem:
                    url = urlItem.get("src")
                    url = helpMe.fill_https_head(url)
                    iconUrls.append(url)
            commentDe.commentContextIconUrl = iconUrls
            # 获取评论时间+地点
            commentDe.commentTimeAndSite = comment.find(class_="L4ozKLf7").find_next("span").text
            # 获取评论点赞数
            commentDe.supportCount = comment.find(class_="eJuDTubq").find_next("span").text
            commentDes.append(commentDe)
        return commentDes
