import os
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ''  # Variable to store the greeting message
    if request.method == 'POST':
        name = request.form.get('name')  # Get the name from the form input
        if name:  # Check if the name is provided
            greeting = f'Hello, {name}! Welcome to our Flask application.'  # Create the greeting
    return render_template('index.html', greeting=greeting)  # Render the index.html template

# Run the application if this script is executed
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or fallback to 5000
    app.run(host='0.0.0.0', port=port, debug=True)