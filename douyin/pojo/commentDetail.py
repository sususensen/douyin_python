class commentDetail:
    commentIconUrl=''
    uesername=''
    commentTime=''
    supportCount=''
    commentContext=''
    commentContextIconUrl=[]

    def __int__(self, commentIconUrl, uesername,commentTime,supportCount,commentContext,commentContextIconUrl):
        self.commentIconUrl=commentIconUrl
        self.uesername=uesername
        self.commentTime=commentTime
        self.supportCount=supportCount
        self.commentContext=commentContext
        self.commentContextIconUrl=commentContextIconUrl
