from flask import Flask,url_for,redirect,render_template
app=Flask(__name__)

@app.route('/')
def yash():
    return render_template('index.html')
@app.route('/allowed/<int:age>')
def allowed(age):
    return"your allowed to enter and age is"+str(age)
@app.route('/notallowed/<int:age>')
def notallowed(age):
    return"your not allowed to enter and age is"+str(age)
@app.route('/result/<int:age>')
def result(age):
    if age>=18:
        result="allowed"
    else:
        result="notallowed"
    return redirect(url_for(result,age=age))

if __name__=='__main__':
    app.run(debug=True)
    