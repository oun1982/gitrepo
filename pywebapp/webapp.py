from flask import Flask

app = Flask('beagle')

@app.route('/')
def hello():
    return '<center>' \
           '<h1 style="font-size:100px">' \
           'Hello World' \
           '</center>' \
           '</h1>'

app.run()