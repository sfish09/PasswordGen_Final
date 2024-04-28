from flask import Flask, render_template
import random
import string

app = (__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('generates')
def gens():
    return render_template('generator.html')

@app.route('/checker')
def check():
    return render_template('checker.html')

if __name__ == "__main__":
    app.run(debug=True)