from flask import Flask, request, redirect, url_for, render_template, abort
from app import app
app = Flask(__name__)
app.config.from_pyfile("config.py")


if __name__ == "__main__":
    app.run()
