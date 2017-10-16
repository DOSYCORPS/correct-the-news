import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

template = JINJA_ENVIRONMENT.get_template(os.path.join('markup','delete-my-edit.html'))

edit_stub = {
  "edit_id" : "012423472"
}

class Delete(webapp2.RequestHandler):
  def get( self, *args, **kwargs ):
    self.response.write(template.render(edit_stub))

routes = [ webapp2.Route( '/delete-my-edit', handler=Delete ) ]

app = webapp2.WSGIApplication( routes=routes, debug=True )   
    
