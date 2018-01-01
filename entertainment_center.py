# encoding: utf-8
from media import Movie
import fresh_tomatoes

def load_movies():
    ''' 加载电影信息 '''
    movies = []
    movie1 = Movie(u'fanghua','https://img3.doubanio.com/view/photo/l/public/p2507227732.jpg','http://v.youku.com/v_show/id_XMzAyMTgxNzA3Mg==.html')
    movies.append(movie1)
    return movies

if __name__ == '__main__':
    ''' 招待中心执行程序 '''
    movies = load_movies()
    fresh_tomatoes.open_movies_page(movies)
