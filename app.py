# Домашняя работа - 10.
from flask import Flask, render_template
from utils import candidates

app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template('page_index.html', candidates=candidates())


@app.route("/candidates/<int:id>")
def page_candidates(id):
    return render_template('page_candidates.html', candidate=candidates()[id-1])


@app.route("/skills/<skill>")
def page_skills(skill):
    return render_template('page_skills.html', candidates=candidates(), skill=skill)

app.run()
