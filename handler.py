# !/usr/bin/env python
#
# Copyright 2010 Vivek Sekhar
#

import os
import sys
import logging
import cgi

from google.appengine.ext import webapp
from google.appengine.api import users

import credentials

# import boto stuff
sys.path = [ os.path.join(os.path.dirname(__file__), "lib", "boto") ] + sys.path
from boto.s3.connection import S3Connection

conn = S3Connection(credentials.access_key, credentials.secret_key)
bucket = conn.get_bucket(credentials.bucket)

class MainPage(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			#self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write('<html><body>')
			if users.is_current_user_admin():
				self.response.out.write('Hello, Mr. %s!' % user.nickname())
				self.response.out.write("<a href='%s'>Logout</a>\n" %
					users.create_logout_url(self.request.uri))
			else:
				self.response.out.write('Hello, %s!\n' % user.nickname())
			content = self.request.get('content')
			if content:
				self.response.out.write('%s\n' % cgi.escape(content))

			for key in bucket.list():
				self.response.out.write(key.name)
				self.response.out.write(' ')
			
			self.response.out.write('</body></html>')

		else:
			self.redirect(users.create_login_url(self.request.uri))



