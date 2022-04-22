from flask import Flask

class Properties:
    def __init__(self):
        self.port = 80;
        self.server_addresse = "server";
        self.server_port = 6666;

def run(properties):

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Web App with Python Flask!'

    app.run(host='0.0.0.0', port=properties.port)