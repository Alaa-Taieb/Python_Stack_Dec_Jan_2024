from flask import Flask , render_template , request , redirect , session


app = Flask(__name__)
app.secret_key = "aksudhoelisfkjlsdjfe"


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/new_user' , methods = ['POST'])
def new_user():
    # Save data in session storage
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # Redirect the user to another page
    return redirect('/display_information')

@app.route('/display_information')
def display():
    # Return the 'info.html' web page with name and email from session storage
    return render_template('info.html' , name = session['name'] , email = session['email'])

if __name__ == "__main__":
    app.run(debug=True)