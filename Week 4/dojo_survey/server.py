from flask import Flask, render_template, session, redirect,request
app = Flask(__name__)
app.secret_key="King"

@app.route('/')
def index():
    return render_template("form.html")


@app.route('/submit',methods=['POST'])
def submit_ninja():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def ninja_details():
    return render_template('ninja_details.html',name = session['name'], location =  session['location'], language =  session['language'], comment =  session['comment'])
    
if __name__=="__main__":
    app.run(debug=True)