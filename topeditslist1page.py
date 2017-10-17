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

template = JINJA_ENVIRONMENT.get_template(os.path.join('markup','top-edits-list-1-page.html'))

edits_stub = {
  "edits": [
    { "text" : "Trump is a bigot / NY Times is bigoted for being so biased againsed Trump's opinions." },
    { "text" : "freedom / tyranny is achieved through the rigorous policing of the subjective feelings of a small group of people as objective offences to reallocate power to that small group." }
  ]
}
class List(webapp2.RequestHandler):
  def get( self, *args, **kwargs ):
    self.response.write(template.render(edits_stub))

routes = [ webapp2.Route( '/top-edits-list-1-page', handler=List ) ]

app = webapp2.WSGIApplication( routes=routes, debug=True )   
    
