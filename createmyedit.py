import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
import models

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

template = JINJA_ENVIRONMENT.get_template(os.path.join('markup','create-my-edit.html'))

class Create(webapp2.RequestHandler):
  def get( self, *args, **kwargs ):
    self.response.write(template.render())

routes = [ webapp2.Route( '/create-my-edit', handler=Create ) ]

app = webapp2.WSGIApplication( routes=routes, debug=True )   
    
