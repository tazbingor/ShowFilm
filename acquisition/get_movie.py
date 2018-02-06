#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json
import time
import web

db = web.database(dbn='sqlite', db='ShowFilm.db')

movie_ids = []


def get_movie_ids():
    for index in range(0, 250, 50):
        # print index
        response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
        data = response.read()
        # print data

        data_json = json.loads(data)
        movie_tops = data_json['subjects']
        for movie in movie_tops:
            movie_ids.append(movie['id'])



if __name__ == '__main__':
    get_movie_ids()
