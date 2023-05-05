from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on GitHub"

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    # if request.method == "POST":
    #     pass
    print(request.form)
    session['account_no'] = request.form['account_no']
    session['mothers_maiden_name'] = request.form['mothers_maiden_name']
    session['pin'] = request.form['pin']

    #NEVER RENDER ON AN ACTION ROUTE
    # return render_template('display.html', account_no=account_no, mothers_maiden_name = mothers_maiden_name, pin=pin)

    return redirect('/display')

@app.route('/display')
def display():
    if 'account_no' in session:
        account_no = session['account_no']
    else:
        account_no = "Was not provided"

    return render_template('display.html', account_no=account_no)

@app.route('/reset') #ACTION
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)