from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/pass/<float:marks>')
def success(marks):
    if marks>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={"marks":marks,"res":res}
    return render_template('result.html', result=exp)

@app.route('/fail/<float:marks>')
def fail(marks):
    result = {
        "marks": marks,
        "res": "FAIL"
    }
    return render_template('result.html', result=result)



@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        datascience = float(request.form['datascience'])

        total_score = (science + maths + datascience) / 3

        if total_score >= 30:
            return redirect(url_for('success', marks=total_score))
        else:
            return redirect(url_for('fail', marks=total_score))

    return redirect(url_for('welcome'))

if __name__ == "__main__":
    app.run(debug=True)
