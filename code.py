#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web

# 指定url网站的匹配规则,左边是正则表达式,右边是对应处理函数的名称
urls = (
    '/', 'index',
    '/movie/(\d+)', 'movie'
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
        return render.index(movies)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
