# !/usr/bin/env python
#
# Copyright 2010 Vivek Sekhar
#

__author__ = "Vivek Sekhar"
__email__ = "vivek@xmain.com"
__copyright__= "Copyright (c) 2010, Vivek Sekhar"
__license__ = "GPL v3 or later"
__url__ = "http://vgphub.appspot.com"

import os
import sys
import logging

from google.appengine.ext import webapp

import credentials

# import boto stuff
sys.path = [ os.path.join(os.path.dirname(__file__), "lib", "boto") ] + sys.path
from boto.s3.connection import S3Connection

conn = S3Connection(credentials.access_key, credentials.secret_key)
bucket = conn.get_bucket("cloudtv")

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
    	for key in bucket.list():
    		self.response.out.write(key.name)
    		self.response.out.write(' ')


