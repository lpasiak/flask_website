from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Łukasz Pasiak',
        'title': 'Blog Post 1',
        'content': 'First post content.',
        'date_posted': 'November 12, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content.',
        'date_posted': 'November 13, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')
