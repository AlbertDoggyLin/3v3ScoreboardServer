from flask import Flask, render_template
from gevent import pywsgi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

if __name__=='__main__':
    import sys
    try:
        port = int(sys.argv[1])
    except:
        port = 5000
    server = pywsgi.WSGIServer(('0.0.0.0', port), app)
    server.serve_forever()