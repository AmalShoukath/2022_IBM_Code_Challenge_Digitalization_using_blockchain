from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")
if __name__ == '__main__':
   app.run()

@app.route('/adminlogin')
def adminlogin():
    return render_template("adminlogin.html")

@app.route('/userlogin')
def userlogin():
    return render_template("userlogin.html")

@app.route('/admincode',methods=['post'])
def admincode():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from adminlogin where user_name=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script> alert("Invalid User");window.location="/"; </script>'''
    elif res[3]=="admin":
        session['lid']=res[0]
        return '''<script> alert("Admin User"); window.location="/admin_home"; </script> '''

@app.route('/usercode',methods=['post'])
def usercode():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from userlogin where user_name=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script> alert("Invalid User");window.location="/"; </script>'''
    elif res[3]=="admin":
        session['lid']=res[0]
        return '''<script> alert("Admin User"); window.location="/user_home"; </script> '''