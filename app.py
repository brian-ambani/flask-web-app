from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': '$ 8,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Mombasa, Kenya',
    'salary': '$ 9,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '$ 5,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Vancouver, Canada',
    'salary': '$ 10,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/json")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)