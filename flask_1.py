from flask import Flask , render_template

app = Flask(__name__,template_folder='template')

@app.route("/index")
def hello():
    return render_template('index.html')

app.run()

