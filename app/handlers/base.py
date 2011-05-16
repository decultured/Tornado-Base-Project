import tornado
import tornado.database
from tornado.options import options

class BaseHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def get_current_user(self):
		user_id = self.get_secure_cookie("user")
		if not user_id: return None
		return self.db.get("SELECT * FROM users WHERE id = %s", int(user_id))
