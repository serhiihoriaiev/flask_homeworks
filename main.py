import requests
import re
from flask import Flask, render_template

app = Flask(__name__)

#  next block of code is used to load list of vegetables from website
req1 = requests.get("https://www.lingokids.com/english-for-kids/vegetables")
req2 = requests.get("https://www.lingokids.com/english-for-kids/fruits")
myregex1 = re.compile(r'class="font-size-large">(?:<strong>)*([^<]+)')
results1 = list(set(myregex1.findall(req1.text)))
results2 = list(set(myregex1.findall(req2.text)))
veggies = [word.replace(u'\xa0', '') for word in results1 if len(word) < 20]
fruits = [word.replace(u'\xa0', '') for word in results2 if len(word) < 20]

@app.route("/")
@app.route("/home")
def get_main():
    return render_template("home.html")

@app.route("/veggies")
def get_vegs():
    return render_template("vegetables.html", lst=veggies)

@app.route("/fruits")
def get_fruits():
    return render_template("fruits.html", lst=fruits)

if __name__ == "__main__":
    app.run(debug=True)