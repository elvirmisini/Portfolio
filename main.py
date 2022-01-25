from flask import Flask, redirect, url_for, render_template, request, jsonify, app,make_response
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)