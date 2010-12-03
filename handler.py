# !/usr/bin/env python
#
# Copyright 2010 Vivek Sekhar
#

import os
import sys
import logging

from google.appengine.ext import webapp
from google.appengine.api import users

import credentials

# import boto stuff
sys.path = [ os.path.join(os.path.dirname(__file__), "lib", "boto") ] + sys.path
from boto.s3.connection import S3Connection

conn = S3Connection(credentials.access_key, credentials.secret_key)
bucket = conn.get_bucket("cloudtv")

class MainPage(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write('Hello, %s!' % user.nickname())

			for key in bucket.list():
				self.response.out.write(key.name)
				self.response.out.write(' ')

		else:
			self.redirect(users.create_login_url(self.request.uri))



