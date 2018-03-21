import http.server
import socketserver
import chunker
import json
#import ssdeep

PORT = 8080

options={}
options['min_chunk_size']=20
options['min_chunk_size']=20

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Fuzzy Hashing server</title></head>")
        self.wfile.write(b"<body><p>This server will return a fuzzy hash of text posted to it/p>\
        <p>To use this server, POST some text</p></body></html>")
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        text_to_hash=str(self.rfile.read(int(self.headers['Content-Length'])))
        normalised=chunker.normalize(text_to_hash)
        chunks=chunker.chunk(normalised)
        self.send_response(200)
        self.wfile.write(bytes(json.dumps(chunks),'utf8'))

try:
    server = http.server.HTTPServer(('', PORT), MyHandler)
    print('Started http server')
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    server.socket.close()