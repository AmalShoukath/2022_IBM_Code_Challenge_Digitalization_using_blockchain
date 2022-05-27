from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/properties')
def list_properties():
    if (request.method == "GET"):
        return jsonify({"message":"Hello World"})









if __name__ == '__main__':
    app.run(debug=True)

