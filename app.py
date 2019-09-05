from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)
@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
