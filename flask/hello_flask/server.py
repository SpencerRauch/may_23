from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

list = ['bob','kyle','steve']

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/hello')
def hello():
    return 'Hello from the other page <a href="/getuser/0"> Go See Bob</a>'

@app.route('/greet/<name>')
def greet(name):
    return render_template('jinja_fun.html', name=name)

@app.route('/getuser/<int:index>')
def get_user(index):
    # index = int(index)
    return list[index]

@app.route('/template')
def view_temp():
    return render_template('index.html')

@app.route('/jinja_fun')
def fun():
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]

    return render_template('jinja_fun.html', name="Bob", list=['str1', 'str2'])

@app.route('/greet/<name_param>/<int:times>')
def greet_times(name_param,times):
    return render_template('say_times.html',name=name_param,times=times, color='pink')



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host='0.0.0.0')    # Run the app in debug mode.