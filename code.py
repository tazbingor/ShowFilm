#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web

# 指定url网站的匹配规则,左边是正则表达式,右边是对应处理函数的名称
urls = (
    '/', 'index',
    '/movie/(.*)', 'movie',
    '/cast/(.*)', 'cast',
    '/director/(.*)', 'director',
)

# movies = [
#     {
#         'title': 'Once Upon a Time in the West',
#         'year': 1968
#     },
#     {
#         'title': 'The Good, the Bad and the Ugly',
#         'year': 1966
#     }
# ]

render = web.template.render('templates/')
db = web.database(dbn='sqlite', db='ShowFilm.db')


class index:
    '''
    index处理请求.
    GET用于请求网页,POST用于提交表单
    '''

    def GET(self):
        movies = db.select('movie')
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie')[0]['COUNT']
        print movies
        print count
        return render.index(movies, count, None)

    def POST(self):
        data = web.input()
        condition = r'TITLE LIKE "%' + data.title + r'%"'
        movies = db.select('movie', where=condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies, count, data.title)


class cast:
    def GET(self, cast_name):
        condition = r'CASTS LIKE "%' + cast_name + r'%"'
        movies = db.select('movie', where=condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies, count, cast_name)


class director:
    def GET(self, director_name):
        condition = r'DIRECTORS LIKE "%' + director_name + r'%"'
        movies = db.select('movie', where=condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies, count, director_name)


class movie:
    def GET(self, movie_id):
        movie = db.select('movie', where='id=$int(movie_id)', vars=locals())[0]
        return render.movie(movie)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
