from flask import Flask, redirect, url_for, render_template, request,app,make_response
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    return render_template("about.html")

@app.errorhandler(403)
def forbidden(e):
    app.logger.error(f"Forbidden acess:{e},route:{request.url}")
    return render_template("403.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def server_error(e):
    app.logger.error(f"Server error:{e},route:{request.url}")
    return render_template("500.html")
if __name__ == '__main__':
    app.run(debug=True)