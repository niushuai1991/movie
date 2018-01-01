# encoding: utf-8
'''
媒体信息类型
'''
class Movie:
    ''' 电影类型 '''
    def __init__(self,title,poster_image_url,trailer_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url # 预告片地址

