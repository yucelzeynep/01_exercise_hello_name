### Programming Exercise: Create a Simple Flask Web Application with Render

#### Exercise Definition
In this exercise, you will create a simple web application using Flask that allows users to input their name and receive a personalized greeting. The application will be hosted on Render, a cloud service that simplifies deployment.

#### Step-by-Step Instructions

1. **Set Up Your Environment**:
   - Ensure you have Python installed on your machine. 
   - Create a new directory for your project and navigate into it:
     ```bash
     mkdir flask_greeting_app
     cd flask_greeting_app
     ```

2. **Create a Virtual Environment**:
   - Set up a virtual environment to manage your project dependencies:
     ```bash
     python -m venv venv
     source venv/bin/activate  
     ```

3. **Install Flask**:
   - Install Flask using pip:
     ```bash
     pip install Flask
     ```

4. **Create the Flask Application**:
   - Create a file named `app.py` and add the following code:

```python
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
            greeting = f'Hello, {name}! Welcome to my Flask application.'  # Create the greeting
    return render_template('index.html', greeting=greeting)  # Render the index.html template

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
```

5. **Create the HTML Template**:
   - Create a folder named `templates` and inside it create a file named `index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Greeting App</title>
</head>
<body>
    <h1>Welcome to the Flask Greeting App</h1>
    <form method="POST">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
    {% if greeting %}
        <h2>{{ greeting }}</h2>  <!-- Display the greeting message if available -->
    {% endif %}
</body>
</html>
```

6. **Run the Application Locally**:
   - Start the Flask application by running the following command in your terminal:
     ```bash
     python app.py
     ```
   - Open your browser and go to `http://127.0.0.1:5000/`. You should see the greeting app.

7. **Prepare for Deployment on Render**:
   - Create a `requirements.txt` file to specify your project dependencies:
     ```bash
     pip freeze > requirements.txt
     ```
   - Create a `render.yaml` file for Render configuration:

```yaml
services:
  - type: web
    name: flask-greeting-app
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
```

8. **Create a Repository on GitHub and Commit**:
   - Open a GitHub account if you do not have one.
   - Go to your project folder and initialize a repository
   - Commit your files

9. **Deploy on Render**:
   - Go to [Render.com](https://render.com/) and create an account if you don't have one.
   - Once logged in, click on "Projects" on the left pane and then "Deploy a Web Service"  under Overview. 
   - Connect it to your GitHub account and select the repository containing your Flask application.
   - As start command, enter "python app.py"
   - Render will automatically detect the `render.yaml` file and set up your application.
   - After deployment, you will be provided with a live URL for your application around the upper part of the browser window.
   - Click on render icon on the upper left, find your deployment under the list, click on "..." on the right, choose "Settings" and click on "Delete Web Service" at the bottom. 


#### Conclusion
You have successfully created and deployed a simple Flask web application that greets users based on their input. This exercise should have reinforced your understanding of Flask, HTML, and cloud deployment using Render.
