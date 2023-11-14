from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.get("/")
def home():
  return render_template('index.html')

@app.route("/create", methods=["POST"])
def generateQR():
  memory = BytesIO()
  if request.method == 'POST':
    data = request.form["link"]
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode("ascii")

    return render_template("index.html", data=base64_img)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug=True)
