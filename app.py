from turtle import title
from flask import Flask, render_template

app = Flask("Daily Blog")

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
