import http.server
import os

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        elif self.path.endswith('.html'):
            pass
        else:
            self.send_response(404)
            self.end_headers()
            return
        with open(os.path.join(self.path), 'rb') as f:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())

if __name__ == '__main__':
    with http.server.HTTPServer(('', PORT), MyHTTPRequestHandler) as httpd:
        print(f'Serving on http://localhost:{PORT}')
        httpd.serve_forever()
