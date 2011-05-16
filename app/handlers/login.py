import tornado
from base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		self.render("../templates/pages/login.html", title="Login", login_error="")	
		
	def post(self):
		try:
			name = self.get_argument("name")
			password = self.get_argument("password")
		except:
			self.render("pages/login.html", title="Login", login_error="Please enter a Username and Password.")
			return
		
		print name, password
		
		if password:
			result = self.db.get("SELECT * FROM users WHERE username = %s AND password = MD5(%s)", name, password)
		
		print result
		
		if result is not None and result.id is not None:
			self.set_secure_cookie("user", str(result.id))
			self.redirect(self.get_argument("next", "/"))
		else:
			self.render("pages/login.html", title="Login", login_error="Invalid Username or Password.")
