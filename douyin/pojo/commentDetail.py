class commentDetail:
    commentIconUrl=''
    username=''
    commentTime=''
    supportCount=''
    commentContext=''
    commentContextIconUrl=[]

    def __int__(self, commentIconUrl, username,commentTime,supportCount,commentContext,commentContextIconUrl):
        self.commentIconUrl=commentIconUrl
        self.uesername=username
        self.commentTime=commentTime
        self.supportCount=supportCount
        self.commentContext=commentContext
        self.commentContextIconUrl=commentContextIconUrl
