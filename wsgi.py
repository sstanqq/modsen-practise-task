from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/test')
def index():
    return '<h1 style="color: green">Test run<h1>'

@app.route('/ip')
def status():
    return f'<h1 style="color: green">Your ip: {request.remote_addr}<h1>'


if __name__ == '__main__':
    app.run()