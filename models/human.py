from google.appengine.ext import ndb

class Human(ndb.Model):
  client_key = ndb.StringProperty()
  public_name = ndb.StringProperty()
