from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入簡宏宥的網站首頁</h1>"
    link += "<a href=/mis>課程</a><hr>"
    link += "<a href=/today>今天日期</a><hr>"
    link += "<a href=/about>關於宏宥</a><hr>"
    link += "<a href=/welcome?u=宏宥&dep=靜宜大學>GET傳直</a><hr>"
    link += "<a href=/account>POST傳值(帳號密碼)</a><hr>"    
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year  = str(now.year)   # 取得年份 
    month = str(now.month)  # 取得月份 
    day   = str(now.day)    # 取得日期 
    now = year + "年" + month + "月" + day + "日"
    return render_template("today.html", datetime = now)

@app.route("/about")
def about():
    return render_template("mis2a.html")



@app.route("/welcome", methods=["GET"])
def welcome():
    x = request.values.get("u")
    y = request.values.get("dep")
    return render_template("welcome.html", name = x,dep = y)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")


if __name__ == "__main__":
    app.run(debug=True)
