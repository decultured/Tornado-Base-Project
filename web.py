#!/usr/bin/env python

import os
import tornado.auth
import tornado.database
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options, parse_command_line, parse_config_file
import tornado.web

import app.handlers

define("debug", default=False, help="Run in debug mode", type=bool)
define("port", default=9801, help="Run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="skeleton", help="database name")
define("mysql_user", default="skeleton", help="database user")
define("mysql_password", default="skeleton", help="database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
			(r"/", app.handlers.home.HomeHandler),
			(r"/admin", app.handlers.admin.AdminHandler),
			(r"/login", app.handlers.login.LoginHandler),
			(r"/logout", app.handlers.logout.LogoutHandler),
        ]
        settings = dict(
			cookie_secret = "IBLRBvsARnaxOqccEG+zo3Cc0PluI0RemJC0xNt8dpw=",
			xsrf_cookies = True,
			debug = options.debug,
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			login_url = "/login",
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = tornado.database.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


def main():
	tornado.options.parse_command_line()
	application = Application()
	
	print ""
	print "----------------------------------------------"
	print "Started on port %s..." % (options.port,)
	print "----------------------------------------------"
	print ""
	
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
