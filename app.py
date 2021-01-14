from flask import Flask, render_template

app = Flask(__name__)

@app.route("/html")
def html():
	page = render_template("index.html")
	return page

@app.route("/html/1")
def html():
	page = render_template("index1.html")
	return page

@app.route("/html/2")
def html():
	page = render_template("index2.html")
	return page

@app.route("/html/3")
def html():
	page = render_template("index3.html")
	return page

