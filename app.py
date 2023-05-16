from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': "HK",
    'salary': 'Rs. 100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': "HK",
    'salary': 'Rs. 100,000'
  },
]

@app.route('/')

def hello_world():
  return render_template("home.html", jobs=JOBS, company_name = "Jovian")

app.run(host="0.0.0.0", debug=True)