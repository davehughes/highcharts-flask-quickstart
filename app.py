import flask


# Create and configure app object
app = flask.Flask(__name__)
app.debug = True


@app.route('/')
def index():
    ctx = {}
    return flask.render_template('basic-chart.html', **ctx)


if __name__ == '__main__':
    app.run()
