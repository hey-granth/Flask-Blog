from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# to run it in debug mode, use the command ```flask --app run.py --debug run```
# after creation and structuring of package, do `python3 run.py`
