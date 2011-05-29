import tornado
import json
from base import BaseHandler
from tornado.options import options

class HomeHandler(BaseHandler):
	def get(self):
		# print 'This is a message that will appear in the console'
		# if 'name' in self.request.arguments:
		# 	self.write("Hello there, %s!" % (self.request.arguments['name'][0],))
		# lol_api_result = {'name': 'jeff', 'age': 22564, 'children': ['bob', 'sam', 'jessica', 'cockface', ('butthead', 'jupiter')] }

		posts = self.db.query("SELECT * FROM posts ORDER BY posted_on DESC")
		self.render("pages/home.html", title="My title", posts=posts)	
		
