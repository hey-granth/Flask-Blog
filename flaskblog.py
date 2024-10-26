from flask import Flask, render_template, url_for
# import lorem


app = Flask(__name__)

posts = [
    {
        'author': 'Granth Agarwal',
        'title': 'Blog Post 1',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed odio lorem, ornare nec iaculis non, maximus eget augue. Phasellus elementum ultrices justo ut aliquet. Ut consequat tortor ac commodo porttitor. Aenean facilisis enim nibh, nec commodo risus interdum porta. Suspendisse diam urna, lobortis id ligula tristique, semper varius lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin vel diam risus. Vestibulum a quam eget mi vestibulum malesuada. Curabitur varius in enim eu varius. Integer vestibulum augue at enim efficitur auctor. Etiam non leo at nunc mattis consequat. ''',
        'date_posted': "October 23rd, 2024"
    },
    {
        'author': 'Ayush Jain',
        'title': 'Blog Post 2',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed odio lorem, ornare nec iaculis non, maximus eget augue. Phasellus elementum ultrices justo ut aliquet. Ut consequat tortor ac commodo porttitor. Aenean facilisis enim nibh, nec commodo risus interdum porta. Suspendisse diam urna, lobortis id ligula tristique, semper varius lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin vel diam risus. Vestibulum a quam eget mi vestibulum malesuada. Curabitur varius in enim eu varius. Integer vestibulum augue at enim efficitur auctor. Etiam non leo at nunc mattis consequat. ''',
        'date_posted': "October 24th, 2024"
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

# to run it in debug mode, use the command ```flask --app flaskblog.py --debug run```