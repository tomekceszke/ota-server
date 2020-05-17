#!/usr/bin/env python3

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import logging
from config import *


def start_ota_server(web_dir, cert_dir, server_ip, server_port):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-p', '--port', dest='port', type= int,
    #     help= "Server Port", default= 8000)
    # args = parser.parse_args()

    ca_cert_file = os.path.join(cert_dir, CA_CERT_FILE_NAME)
    server_key_file = os.path.join(cert_dir, SERVER_KEY_FILE_NAME)

    httpd = HTTPServer((server_ip, server_port), OtaRequestHandler)

    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=server_key_file, certfile=ca_cert_file, server_side=True)
    os.chdir(web_dir)
    print("OTA Server is listening on port", OTA_SERVER_PORT)
    httpd.serve_forever()


class OtaRequestHandler(SimpleHTTPRequestHandler):

    def do_DELETE(self):
        old = str(self.path)[1:] + ".old"
        try:
            os.replace(r'' + self.path[1:], r'' + old)
            logging.info("Renamed to: %s", old)
            self.send_response(200)
        except Exception as e:
            logging.error(str(e))
            self.send_error(500)
        return


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_ota_server(BUILDS_DIR, CERTS_DIR, OTA_SERVER_IP, OTA_SERVER_PORT)
