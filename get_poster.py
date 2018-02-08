#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import time
import web

db = web.database(dbn='sqlite', db='ShowFilm.db')


def get_poster(id, url):
    pic = urllib.urlopen(url).read()
    file_name = 'static/images/%d.jpg' % id
    f = file(file_name, 'wb')
    f.write(pic)
    f.close()


def get_image():
    movies = db.select('movie')
    count = 0
    for movie in movies:
        get_poster(movie.id, movie.image)
        count += 1
        time.sleep(2)


def main():
    get_image()


if __name__ == '__main__':
    main()
