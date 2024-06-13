from flask import url_for, Flask
from flask import Flask, request, jsonify, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

@app.route('/submit', methods=['POST'])
def submit():
    # Parse the incoming JSON data
    data = request.json
    
    # Log the received data (for debugging purposes)
    print("Received data:", data)
    
    # Process the data (for example, add a new key-value pair)
    response_data = {
        "status": "success",
        "message": "Data received successfully",
        "received_data": data
    }
    
    # Return a JSON response
    return jsonify(response_data)

with app.test_request_context():
    print(url_for('home'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
if __name__ == '__main__':
    app.run(debug=True)
