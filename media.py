# encoding: utf-8

class Movie:
    ''' 电影类型 '''
    def __init__(self,name,poster,url):
        self.name = name
        self.poster = poster
        self.url = url

Movie movie = Movie('Book','http://www.url.com/1.jpg','http')