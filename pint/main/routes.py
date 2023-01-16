from flask import render_template, request, Blueprint
from flask import Blueprint

main = Blueprint("main", __name__)

#  Route decorators
@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contactus")
def contactUs():
    return render_template("contactus.html")


@main.route("/donation")
def donation():
    return render_template("donation.html")


@main.route("/partners")
def partners():
    return render_template("partners.html")
