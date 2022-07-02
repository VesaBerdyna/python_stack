from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')        
def first():
    return render_template('box.html',num = 3, color= "blue")

@app.route('/play/<int:num>')        
def second(num):
    return render_template('box.html',num = num,color="blue")

@app.route('/play/<int:num>/<string:color>')        
def third(num,color):
    return render_template('box.html',num = num, color= color)


if __name__=="__main__":     
    app.run(debug=True)   

