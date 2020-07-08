#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:42:58 2020

@author: jasper
"""

import requests_with_caching
import json
def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    params_diction = {}
    params_diction['q']= title
    params_diction['type']= 'movies'
    params_diction['limit']= 5
    page_cache = requests_with_caching.get(url, params=params_diction)
    return json.loads(page_cache.text)

# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])


def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))

def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests_with_caching.get(endpoint, params=param)
    return json.loads(this_page_cache.text)

def get_movie_rating(data):
    rating = 0
    for i in data['Ratings']:
        if i['Source'] == 'Rotten Tomatoes':
            rating = int(i['Value'][:-1])
            #print(rating)
    return rating 

def get_sorted_recommendations(list):
    new_list = get_related_titles(list)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))