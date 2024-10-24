from flask import Flask, render_template
import lorem


app = Flask(__name__)

posts = [
    {
        'author': 'Granth Agarwal',
        'title': 'Blog Post 1',
        'content': lorem.paragraph(),
        'date_posted': "October 23rd, 2024"
    },
    {
        'author': 'Ayush Jain',
        'title': 'Blog Post 2',
        'content': lorem.paragraph(),
        'date_posted': "October 24th, 2024"
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

# to run it in debug mode, use the command ```flask --app flaskblog.py --debug run```