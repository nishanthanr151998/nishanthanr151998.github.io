from flask import Flask, render_template, request


app = Flask(__name__, template_folder='./templates', static_folder='./static')
reponses_map = {}

@app.route("/")
# Code for rendering the UI
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
