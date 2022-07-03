from flask import Flask, render_template,session,redirect
app = Flask(__name__)
app.secret_key = "queen"

@app.route('/')        
def count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0    
    return render_template('counter.html', count = session['count'])

@app.route('/destroy_session')
def destroy_session():
    session.pop('count')		
    return redirect('/')

@app.route('/plus_two')
def plus_two():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()		
    return redirect('/')   
    
if __name__=="__main__":     
    app.run(debug=True)   

