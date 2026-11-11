"""Filo Konsolu'nu yerel ağda HTTPS ile yayınlar: https://<bu-bilgisayarın-IP'si>:8443/

Kullanım: python3 serve_https.py [sertifika klasörü]
Sertifika (cert.pem, key.pem) repoya konmaz; varsayılan klasör ~/StudioProjects/filo-konsolu-sertifika
"""
import http.server, os, ssl, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CERT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/StudioProjects/filo-konsolu-sertifika")
PORT = 8443

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()
    def do_GET(self):
        # yalnız sitenin dosyaları; betik ve gizli dosyalar sunulmaz
        if self.path.split("?")[0].endswith((".py", ".pem")) or "/." in self.path:
            self.send_error(404); return
        super().do_GET()

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
ctx.load_cert_chain(os.path.join(CERT_DIR, "cert.pem"), os.path.join(CERT_DIR, "key.pem"))
httpd = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
print(f"Filo Konsolu: https://0.0.0.0:{PORT}/  (Ctrl+C ile durdur)", flush=True)
httpd.serve_forever()
