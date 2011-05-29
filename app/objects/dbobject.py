import tornado
import tornado.database

class DBObject(object):
	def __init__(self, db):
		self.db = db;