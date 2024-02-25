from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/app/manage':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('manage_app.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/app/popup.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('popup.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/app/register':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('popup.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Page not found.")

def run(server_class=HTTPServer, handler_class=CustomHandler, addr='localhost', port=4443):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile='cert.pem',
                                   keyfile='key.pem',
                                   ssl_version=ssl.PROTOCOL_TLS)
    print(f'HTTPS Server running on https://{addr}:{port}/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
