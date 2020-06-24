#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:05:11 2020

@author: jasper
"""

import requests
req = requests.get('http://www.edureka.co')
 
req.encoding # returns 'utf-8'
req.status_code # returns 200
req.elapsed # returns datetime.timedelta(0, 1, 666890)
req.url # returns '<a href="https://edureka.co/">https://edureka.co/</a>'
 
req.history 
# returns [<Response [301]>, <Response [301]>]
 
req.headers['Content-Type']