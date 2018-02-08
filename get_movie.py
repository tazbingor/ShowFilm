#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json
import time
import web

db = web.database(dbn='sqlite', db='ShowFilm.db')


def get_movie_ids():
    movie_ids = []
    for index in range(0, 250, 50):
        # print index
        response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
        data = response.read()
        # print data

        data_json = json.loads(data)
        movie_tops = data_json['subjects']
        for movie in movie_tops:
            movie_ids.append(movie['id'])
        time.sleep(3)
    return movie_ids


def add_movie(data):
    movie = json.loads(data)
    db.insert(
        'movie',
        id=int(movie['id']),
        title=movie['title'],
        origin=movie['original_title'],
        url=movie['alt'],
        rating=movie['rating']['average'],
        image=movie['images']['large'],
        directors=','.join([d['name'] for d in movie['directors']]),
        casts=','.join([c['name'] for c in movie['casts']]),
        year=movie['year'],
        genres=','.join(movie['genres']),
        countries=','.join(movie['countries']),
        summary=movie['summary'],
    )


def main():
    """

    :rtype: object
    """
    movie_ids = get_movie_ids()
    print movie_ids  # done
    count = 0
    for movie_id in movie_ids:
        response = urllib.urlopen('http://api.douban.com/v2/movie/subject/%s' % movie_id)
        data = response.read()
        add_movie(data)
        count += 1
        time.sleep(3)


if __name__ == '__main__':
    main()
