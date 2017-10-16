from google.appengine.ext import ndb

ATTACHMENTS = [
  'beforeBegin',
  'afterEnd',
  'middle'
]

TYPES = [
  'strike',
  'insert'
]

class Modification(ndb.Model):
  type = ndb.StringProperty(choices=TYPES)
  start_index = ndb.IntegerProperty()
  trigram_at_start = ndb.StringProperty()
  content = ndb.StringProperty()

class Edit(ndb.Model):
  selector = ndb.StringProperty()
  attachment = ndb.StringProperty(choices=ATTACHMENTS)
  selected_index = ndb.IntegerProperty()
  sentence_index = ndb.IntegerProperty()
  trigram_at_attach_point = ndb.StringProperty()
  modifications = ndb.StructuredProperty(Modification, repeated=True)
