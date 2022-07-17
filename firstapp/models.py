from mongoengine import fields , Document
from datetime import datetime

class jsondata(Document):
    end_year = fields.IntField()
    intensity = fields.IntField()
    sector = fields.StringField()
    topic = fields.StringField()
    insight = fields.StringField()
    url = fields.URLField()
    region = fields.StringField()
    start_year = fields.IntField()
    impact = fields.IntField()
    added = fields.DateTimeField()
    published = fields.DateTimeField()
    country = fields.StringField()
    relevance = fields.IntField()
    pestle  = fields.StringField()
    source = fields.StringField()
    title = fields.StringField()
    likelihood = fields.IntField()






