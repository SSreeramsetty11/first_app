from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Greet route
@app.route('/greet')
def greet():
    return render_template('greet.html')

# Form route
@app.route('/form')
def form():
    return render_template('form.html')

# Form submission route
@app.route('/form_submit', methods=['POST'])
def form_submit():
    name = request.form.get('name')  # Get the 'name' field from the form data
    if name is None:
        return "Error: 'name' field is required."
    return f"Hello {name}! Nice to meet you!"

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Start the server