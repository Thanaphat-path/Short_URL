import qrcode
from pickle import TRUE
import re
from flask import Flask, render_template, request, url_for, redirect, flash
from random import choice
import string

# from core.models import ShortUrls
from core import app

from pymongo import MongoClient
client = MongoClient(
    "mongodb+srv://admin:pxWmp2vgKiqMtjv1@cluster0.b6v1fml.mongodb.net/URL?retryWrites=true&w=majority")
db = client.URL
todos = db.ShortURL


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


def new_link_URL(url, short_id):
    add = {
        "original_url": url,
        "short_url": short_id,
        "count": 1}
    return add


def new_url_or_not(url):
    results = todos.find({"original_url": str(url)})
    for x in results:
        if url == x["original_url"]:
            return True
    return False


def update_count(os, url):
    results = todos.find({os: url})
    y = 0
    for x in results:
        y = x["count"]
        y = y+1
    return y


def get_short(url):
    results = todos.find({"original_url": url})
    STR = ""
    for x in results:
        STR = x["short_url"]
    return STR


@app.route("/", methods=['GET', 'POST'])
def main():
    from unittest import result

    if request.method == "POST" and request.form['action'] == 'button_sub':

        short_id = request.form.get("custom_id")
        url = request.form.get("Text_URL")

        if not short_id:
            short_id = generate_short_id(8)

            short_url = request.host_url + short_id

            if new_url_or_not(url):
                result = todos.update_one({"original_url": url}, {
                                          "$set": {"count": update_count("original_url", url)}})
                short_url = request.host_url+get_short(url)
                return render_template("index.html", short_url=short_url, QR=short_id+".jpg")
            QR = qrcode.make(short_url)
            QR.save("core/static/Image/"+short_id+".jpg")
            new_link = new_link_URL(url, short_id)
            result = todos.insert_one(new_link)

            return render_template("index.html", short_url=short_url, QR=short_id+".jpg")
        # return render_template("index.html")
    return render_template("index.html")


@app.route('/List')
def List():
    results = todos.find({})

    return render_template("List.html", results=results)


@app.route('/<short_url>')
def redirect_url(short_url):
    from unittest import result

    links = todos.find({"short_url": str(short_url)})
    for link in links:
        if link:
            result = todos.update_one({"short_url": short_url}, {
                                      "$set": {"count": update_count("short_url", short_url)}})
            return redirect(link["original_url"])

        else:
            flash('Invalid URL')
            return redirect(url_for('index'))
