from flask import Flask, render_template

from google_sheets import people, papers, alumni, news, cal_mmrg

app = Flask(__name__)


@app.route("/")
def index():
    list_of_news = news.get_news()
    return render_template("index.html", news=list_of_news);


@app.route("/people.html")
def peoples():
    list_of_people = people.get_people()
    return render_template("people.html", people=list_of_people);


@app.route("/alumni.html")
def alum():
    list_of_alumni = alumni.get_alumni()
    return render_template("alumni.html", people=list_of_alumni);


@app.route("/contact.html")
def contact():
    return render_template("contact.html");

@app.route("/mmrg.html")
def mmrg():
    list_of_books = cal_mmrg.get_books()
    return render_template("mmrg.html", books=list_of_books);

@app.route("/research.html")
def research():
    list_of_papers = papers.get_papers()
    return render_template("research.html", paper=list_of_papers);


@app.route("/positions.html")
def position():
    return render_template("positions.html");


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
