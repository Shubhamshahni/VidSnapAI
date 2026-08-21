from http.server import BaseHTTPRequestHandler
import json

from vercel.blob import BlobClient


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)

            data = json.loads(body)

            filename = data.get("filename")

            if not filename:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Filename is required")
                return

            blob_client = BlobClient()

            # We'll add the actual client-upload logic next.
            response = {
                "filename": filename,
                "message": "Upload endpoint is working"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({"error": str(e)}).encode()
            )