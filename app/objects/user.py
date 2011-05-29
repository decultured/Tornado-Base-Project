import tornado
import tornado.database
from dbobject import DBObject

class User(DBObject):
	def __init__(self, db):
		self.id = None;
		self.username = None;
		super(User, self).__init__(db);

	def getById(self, user_id):
		if not user_id: return None
		results = self.db.get("SELECT id, username FROM users WHERE id = %s", int(user_id))
		self.id = results.id
		self.username = results.username
		return None
