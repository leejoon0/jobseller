from requests import get
from bs4 import BeautifulSoup
from extractors.naver import extract_keywords
from file import save_to_file
from flask import Flask, render_template, request, redirect, send_file

# keyword = "키보드"
# keywords = extract_keywords(keyword)

# save_to_file(keyword, keywords)

app = Flask('Scrapper')

@app.route('/')
def home():
    return render_template('home.html')

db = {}

@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect('/');
    if keyword in db:
        keywords = db[keyword]
    else:
        keywords = extract_keywords(keyword)
        db[keyword] = keywords
    return render_template('search.html', keyword = keyword, keywords = keywords)

@app.route('/export')
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect('/')
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run('0.0.0.0')