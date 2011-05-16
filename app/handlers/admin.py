import tornado
from base import BaseHandler

class AdminHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render("pages/admin.html", title="Admin")	

	def post(self):
		try:
			link = self.get_argument("link")
			url = self.get_argument("URL")
			tags = self.get_argument("links")
			description = self.get_argument("description")
			body = self.get_argument("body")
		except:
			self.redirect("admin")
			return
			
		
