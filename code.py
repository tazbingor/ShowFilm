#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web

# 指定url网站的匹配规则,左边是正则表达式,右边是对应处理函数的名称
urls = (
    '/', 'index'
)

movies = [
    {
        'title': '西部往事',
        'year': 1968
    },
    {
        'title': '荒野三镖客',
        'year': 1968
    }
]


class index:
    '''
    index处理请求.
    GET用于请求网页,POST用于提交表单
    '''

    def GET(self):
        page = ''
        for item in movies:
            page += '%s(%d)\n' % (item['title'], item['year'])
        return page


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
