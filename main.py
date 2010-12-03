# !/usr/bin/env python
#
# Copyright 2010 Vivek Sekhar
#

__author__ = "Vivek Sekhar"
__email__ = "vivek@xmain.com"
__copyright__= "Copyright (c) 2010, Vivek Sekhar"
__license__ = "GPL v3 or later"
__url__ = "http://vgphub.appspot.com"

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# app specific code
import handler

application = webapp.WSGIApplication(
                                     [('/', handler.MainPage)],
                                     debug=True)

def main():
	run_wsgi_app(application)

if __name__ == '__main__':
	main()

