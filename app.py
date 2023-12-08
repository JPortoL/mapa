from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__)
Compress(app)  # Configura la compresión para la aplicación

@app.route("/")
def raiz():
    return render_template("inicio.html")

if __name__ == "__main__":
    app.run(debug=False)
