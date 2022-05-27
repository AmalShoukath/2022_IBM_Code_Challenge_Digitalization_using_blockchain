import sys
from blockchain import Block,Blockchain
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

@app.route('/show_land_trans', methods=['GET'])
def mine():
    dict={}
    i=1
    plot1 = Blockchain()
    B1=Block(1,"23/05/2022",{"amount": 4})
    plot1.addBlock(B1)
    B2=Block(1,"24/05/2022",{"amount": 10})
    plot1.addBlock(B2)
    for items in plot1.chain:
        dict[i]=str(items.data)
        i+=1
    return jsonify(dict)
    


if __name__ == '__main__':
    app.run(debug=True)

