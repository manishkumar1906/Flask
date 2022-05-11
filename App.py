# Flask is used to create apis
from flask import Flask, request, jsonify
#constructor of the flask class,name of the current module stored in __name__
app = Flask(__name__) 
#define a route
@app.route('/') #route function of flask class is a decorator which tells app which url and point should call the associated function
def hello_world(): #associated in our function hello_world
    return 'hello world'

if __name__=='__main__':
    app.run(debug = True)