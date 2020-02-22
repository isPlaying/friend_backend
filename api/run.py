import os
from app import create_app

app = create_app()

HOST = "0.0.0.0"
PORT = "10001"
DEBUG = True if os.environ.get('MODE') != 'PRODUCTION' else False
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, threaded=True, debug=DEBUG)
