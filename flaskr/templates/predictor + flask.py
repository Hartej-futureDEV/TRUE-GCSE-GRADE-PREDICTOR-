from flask import Flask, render_template, request
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

subjects = ["mathsF","mathsH","englishL","englishLit","scienceF","scienceH",
                           "biologyTriple","chemistryTriple","physicsTriple","history",
                           "geography","CS","french","spanish","german"]

def load_boundaries():
    base = os.path.dirname(__file__)
    path = os.path.join(base, 'boundaries.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # ensure thresholds are sorted descending by min
            for v in data.values():
                if isinstance(v, dict) and 'thresholds' in v:
                    v['thresholds'].sort(key=lambda t: t.get('min', 0), reverse=True)
            return data
    except Exception:
        return {}


BOUNDARIES = load_boundaries()


def get_int(value):
    try:
        v = int(value)
        return max(v, 0)
    except Exception:
        return 0


def get_grade_from_boundaries(key, score):
    if not score or score <= 0:
        return None
    spec = BOUNDARIES.get(key)
    if not spec:
        return None
    for thr in spec.get('thresholds', []):
        if score >= thr.get('min', 0):
            return thr.get('grade')
    return spec.get('below')


def predict_all(form):
    # read all fields from the form and convert to int
    keys = ["mathsF", "mathsH", "englishL", "englishLit", "scienceF", "scienceH",
            "biologyTriple", "chemistryTriple", "physicsTriple", "history",
            "geography", "CS", "french", "spanish", "german"]

    vals = {k: get_int(form.get(k, 0)) for k in keys}
    results = {}

    for k in keys:
        grade = get_grade_from_boundaries(k, vals.get(k, 0))
        if grade:
            display = BOUNDARIES.get(k, {}).get('display_name', k)
            results[display] = grade

    # remove None or empty results (and keep original behavior of skipping zeros)
    return {k: v for k, v in results.items() if v}


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        results = predict_all(request.form)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
