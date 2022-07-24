from http.server import BaseHTTPRequestHandler, HTTPServer
import time
class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>Coding with Charlies</title></head>", "utf-8"))
		self.wfile.write(bytes("<body><h2>hello world</h2></body>", "utf-8"))
		
webServer = HTTPServer(("localhost", 8080), MyServer)
webServer.serve_forever()