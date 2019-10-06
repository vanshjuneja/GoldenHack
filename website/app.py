from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/pypy")
def gopy():
    import Main.py as pkg


@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
