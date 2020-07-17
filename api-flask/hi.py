from flask import Flask,render_template



app = Flask(__name__)


@app.route('/')
def dynmic():
    return "welcome to the page"


@app.route('/bobo')
@app.route('/momo')
def mo():
    return 'Hello bobo an momo'


@app.route('/realmadrid')
def real():
    return render_template('real.html',page_title='real',visitors='mohamad faidi')

@app.route('/city/<name>')
def hello(name):
    return f'welcome to {name} city'


if __name__ == "__main__":
    app.run(debug=True)