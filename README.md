### Programming Exercise: Create a Simple Web Application and deploy it

#### Exercise Definition
In this exercise, you will create a web application, host it locally using Flask and then deploy it with Render. 

The web application is toy one, in which the users input their name to receive a personalized greeting. 

#### Step-by-Step Instructions

1. **Set Up Your Environment**:
   - Ensure you have Python installed on your machine. 
   - Choose a development environment to write and compile your codes.
   - Open a GitHub account and a Render account.

2. **Create a Virtual Environment**:
   - On the terminal, create a new directory (e.g. greeting_app) for your project and navigate into it:
     ```bash
     mkdir greeting_app
     cd greeting_app
     ```
   - Set up a virtual environment to manage your project dependencies:
     ```bash
     python -m venv venv_hello
     source venv_hello/bin/activate  
     ```

3. **Install Flask**:
   - In the same directory, install Flask using pip:
     ```bash
     pip install Flask
     ```

4. **Create the HTML Template**:
   - Create a folder named `templates`.

     ```bash
     mkdir templates
     ```
   - In your development environment, navigate into the directory '/greeting_app/templates' and open new file.
   - Add the following code and save it as `index.html`.

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

5. **Create the Flask Application**:
   - In your development environment, navigate into the directory '/greeting_app' and open new file.
   - Add the following code and save it as `app.py`. 

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

6. **Run the Application Locally**:
   - In the terminal, navigate into the directory '/greeting_app'.
   - Start the Flask application by running the following command:
     ```bash
     python app.py
     ```
   - You will see some debug messages on the terminal (e.g. Running on http://127.0.0.1:5000)
   - Open your browser and go to `http://127.0.0.1:5000/`. You should see the greeting app. Try it.

7. **Prepare for deployment on Render**:
   - In the terminal, make sure you are under the directory '/greeting_app'.
   - Create a `requirements.txt` file to specify your project dependencies:
     ```bash
     pip freeze > requirements.txt
     ```
   - In your IDE, create a `render.yaml` file and add the following content (Render configurations):

```yaml
services:
  - type: web
    name: greeting-app
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
```

8. **Create a Repository on GitHub and Commit**:
   - Go to your project folder and initialize a repository
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     ```
   - Commit your files
     ```bash
     git remote add origin https://github.com/yourusername/your-repo.git
     git push -u origin master
     ```

9. **Deploy on Render**:
   - Go to [Render.com](https://render.com/) and create an account, if you do not have one.
   - Once logged in, click on "Projects" on the left pane and then "Deploy a Web Service"  under "Overview". 
   - Connect it to your GitHub account and select the repository containing your Flask application.
   - As start command, enter "python app.py"
   - Render will automatically detect the `render.yaml` file and set up your application.
   - After deployment, you will be provided with a live URL for your application around the upper part of the browser window.
   - Click on render icon on the upper left, find your deployment under the list, click on "..." on the right, choose "Settings" and click on "Delete Web Service" at the bottom. 


#### Conclusion
You have successfully created and deployed a simple web application that greets users based on their input. This exercise should have reinforced your understanding of Flask, HTML, and cloud deployment using Render.
