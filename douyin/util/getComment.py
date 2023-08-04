

from douyin.pojo.commentDetail import commentDetail
from douyin.util.help工具.fourthSpan import helpMe


class getComment:
    def get_comment(self,html_new):

        commentDes=[]
        commentList= html_new.find_all(class_="CDx534Ub")
        for comment in commentList:
            commentDe = commentDetail()
            commentDe.commentIconUrl="https:"+comment.find(class_="V3cGkKvu comment-item-avatar").find("a").get("href")
            commentDe.username=helpMe.get_lowest_span(comment,"Nu66P_ba NCRZnxVF").text
            tempRoad=comment.find(class_="VD5Aa1A1")
            context=helpMe.get_lowest_span(tempRoad,"Nu66P_ba")
            commentDe.commentContext=context.text
            urlsItem=context.find_next_siblings()
            #有可能是空的好吧，有可能没有表情包
            for urlItem in urlsItem:
                url=urlItem.get("src")
                commentDe.commentContextIconUrl.append(url)
            commentDes.append(commentDe)
        return commentDes
