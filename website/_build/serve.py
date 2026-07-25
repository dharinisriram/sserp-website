# -*- coding: utf-8 -*-
"""Dev server with gzip + cache headers, approximating production hosting.
Run from website/:  python _build/serve.py  ->  http://localhost:8080
"""
import gzip
import http.server
import io
import os
import socketserver

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
COMPRESSIBLE = (".html", ".css", ".js", ".svg", ".json", ".xml", ".txt", ".webmanifest")
_GZ_CACHE = {}  # path -> (mtime, gzipped bytes)


def gz(path):
    mtime = os.path.getmtime(path)
    hit = _GZ_CACHE.get(path)
    if hit and hit[0] == mtime:
        return hit[1]
    with open(path, "rb") as f:
        data = gzip.compress(f.read(), 9)
    _GZ_CACHE[path] = (mtime, data)
    return data


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        if self.path.startswith("/assets/"):
            self.send_header("Cache-Control", "public, max-age=604800")
        elif self.path.endswith((".css", ".js")):
            self.send_header("Cache-Control", "public, max-age=86400")
        super().end_headers()

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        if (os.path.isfile(path) and path.endswith(COMPRESSIBLE)
                and "gzip" in self.headers.get("Accept-Encoding", "")):
            data = gz(path)
            self.send_response(200)
            self.send_header("Content-Type", self.guess_type(path))
            self.send_header("Content-Encoding", "gzip")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            return io.BytesIO(data)
        return super().send_head()


if __name__ == "__main__":
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", 8080), Handler) as httpd:
        print("serving", ROOT, "on http://localhost:8080 (gzip on)")
        httpd.serve_forever()
