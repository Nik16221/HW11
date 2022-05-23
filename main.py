import utils
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    candidates = utils.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>/")
def page_get_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    if candidate is None:
        return "Нет такого кандидата"
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>/")
def page_get_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    number_candidates = len(candidates)
    return render_template("search.html",
                           candidates=candidates,
                           number_candidates=number_candidates
                           )


@app.route("/skills/<skill_name>/")
def page_get_candidate_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    number_candidates = len(candidates)
    if candidates is None:
        return "Такого кандидата нет!"
    return render_template("skills.html",
                           candidates=candidates,
                           number_candidates=number_candidates,
                           skill_name=skill_name
                           )


if __name__ == "__main__":
    app.run(debug=True)