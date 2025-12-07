from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')


def get_int(value):
    try:
        v = int(value)
        return max(v, 0)
    except Exception:
        return 0


def predict_all(form):
    # read all fields from the form and convert to int
    keys = ["mathsF","mathsH","englishL","englishLit","scienceF","scienceH",
            "biologyTriple","chemistryTriple","physicsTriple","history",
            "geography","CS","french","spanish","german"]

    vals = {k: get_int(form.get(k, 0)) for k in keys}
    results = {}

    # Maths Foundation
    m = vals['mathsF']
    if m >= 186:
        results['Maths Foundation'] = 'Grade 5 (max)'
    elif 157 <= m < 186:
        results['Maths Foundation'] = 'Grade 4-5'
    elif 117 <= m < 157:
        results['Maths Foundation'] = 'Grade 3-4'
    elif 77 <= m < 117:
        results['Maths Foundation'] = 'Grade 2-3'
    elif 37 <= m < 77:
        results['Maths Foundation'] = 'Grade 1-2'
    elif m > 0:
        results['Maths Foundation'] = 'Below Grade 1'

    # Maths Higher
    m = vals['mathsH']
    if m >= 219:
        results['Maths Higher'] = 'Grade 9'
    elif 191 <= m < 219:
        results['Maths Higher'] = 'Grade 8'
    elif 163 <= m < 191:
        results['Maths Higher'] = 'Grade 7'
    elif 129 <= m < 163:
        results['Maths Higher'] = 'Grade 6'
    elif 95 <= m < 129:
        results['Maths Higher'] = 'Grade 5'
    elif 61 <= m < 95:
        results['Maths Higher'] = 'Grade 4'
    elif 44 <= m < 61:
        results['Maths Higher'] = 'Grade 3'
    elif m > 0:
        results['Maths Higher'] = 'Below Grade 3'

    # English Language
    e = vals['englishL']
    if e >= 138:
        results['English Language'] = 'Grade 9'
    elif 125 <= e < 138:
        results['English Language'] = 'Grade 8'
    elif 112 <= e < 125:
        results['English Language'] = 'Grade 7'
    elif 102 <= e < 112:
        results['English Language'] = 'Grade 6'
    elif 92 <= e < 102:
        results['English Language'] = 'Grade 5'
    elif 82 <= e < 92:
        results['English Language'] = 'Grade 4'
    elif 73 <= e < 82:
        results['English Language'] = 'Grade 3'
    elif e > 0:
        results['English Language'] = 'Below Grade 3'

    # English Literature
    el = vals['englishLit']
    if el >= 137:
        results['English Literature'] = 'Grade 9'
    elif 121 <= el < 137:
        results['English Literature'] = 'Grade 8'
    elif 106 <= el < 121:
        results['English Literature'] = 'Grade 7'
    elif 90 <= el < 106:
        results['English Literature'] = 'Grade 6'
    elif 74 <= el < 90:
        results['English Literature'] = 'Grade 5'
    elif 58 <= el < 74:
        results['English Literature'] = 'Grade 4'
    elif 42 <= el < 58:
        results['English Literature'] = 'Grade 3'
    elif 27 <= el < 42:
        results['English Literature'] = 'Grade 2'
    elif 12 <= el < 27:
        results['English Literature'] = 'Grade 1'
    elif el > 0:
        results['English Literature'] = 'Below Grade 1'

    # Combined Science Foundation
    sf = vals['scienceF']
    if sf >= 234:
        results['Combined Science Foundation'] = 'Grade 5'
    elif 204 <= sf < 234:
        results['Combined Science Foundation'] = 'Grade 4'
    elif 174 <= sf < 204:
        results['Combined Science Foundation'] = 'Grade 3'
    elif 144 <= sf < 174:
        results['Combined Science Foundation'] = 'Grade 2'
    elif 114 <= sf < 144:
        results['Combined Science Foundation'] = 'Grade 1'
    elif sf > 0:
        results['Combined Science Foundation'] = 'Below Grade 1'

    # Combined Science Higher
    sh = vals['scienceH']
    if sh >= 306:
        results['Combined Science Higher'] = 'Grade 9'
    elif 270 <= sh < 306:
        results['Combined Science Higher'] = 'Grade 8'
    elif 234 <= sh < 270:
        results['Combined Science Higher'] = 'Grade 7'
    elif 198 <= sh < 234:
        results['Combined Science Higher'] = 'Grade 6'
    elif 162 <= sh < 198:
        results['Combined Science Higher'] = 'Grade 5'
    elif 126 <= sh < 162:
        results['Combined Science Higher'] = 'Grade 4'
    elif 90 <= sh < 126:
        results['Combined Science Higher'] = 'Grade 3'
    elif sh > 0:
        results['Combined Science Higher'] = 'Below Grade 3'

    # Triple sciences
    for subject, key in [("Biology", "biologyTriple"), ("Chemistry", "chemistryTriple"), ("Physics", "physicsTriple")]:
        sc = vals[key]
        if sc >= 180:
            results[f"{subject} Triple Science"] = 'Grade 9'
        elif 160 <= sc < 180:
            results[f"{subject} Triple Science"] = 'Grade 8'
        elif 140 <= sc < 160:
            results[f"{subject} Triple Science"] = 'Grade 7'
        elif 120 <= sc < 140:
            results[f"{subject} Triple Science"] = 'Grade 6'
        elif 100 <= sc < 120:
            results[f"{subject} Triple Science"] = 'Grade 5'
        elif 80 <= sc < 100:
            results[f"{subject} Triple Science"] = 'Grade 4'
        elif 60 <= sc < 80:
            results[f"{subject} Triple Science"] = 'Grade 3'
        elif sc > 0:
            results[f"{subject} Triple Science"] = 'Below Grade 3'

    # History
    h = vals['history']
    if h >= 117:
        results['History'] = 'Grade 9'
    elif 105 <= h < 117:
        results['History'] = 'Grade 8'
    elif 93 <= h < 105:
        results['History'] = 'Grade 7'
    elif 81 <= h < 93:
        results['History'] = 'Grade 6'
    elif 69 <= h < 81:
        results['History'] = 'Grade 5'
    elif 57 <= h < 69:
        results['History'] = 'Grade 4'
    elif 40 <= h < 57:
        results['History'] = 'Grade 3'
    elif 24 <= h < 40:
        results['History'] = 'Grade 2'
    elif 8 <= h < 24:
        results['History'] = 'Grade 1'
    elif h > 0:
        results['History'] = 'Below Grade 1'

    # Geography
    g = vals['geography']
    if g >= 202:
        results['Geography'] = 'Grade 9'
    elif 182 <= g < 202:
        results['Geography'] = 'Grade 8'
    elif 162 <= g < 182:
        results['Geography'] = 'Grade 7'
    elif 142 <= g < 162:
        results['Geography'] = 'Grade 6'
    elif 123 <= g < 142:
        results['Geography'] = 'Grade 5'
    elif 104 <= g < 123:
        results['Geography'] = 'Grade 4'
    elif 76 <= g < 104:
        results['Geography'] = 'Grade 3'
    elif 48 <= g < 76:
        results['Geography'] = 'Grade 2'
    elif 20 <= g < 48:
        results['Geography'] = 'Grade 1'
    elif g > 0:
        results['Geography'] = 'Below Grade 1'

    # Computer Science
    cs = vals['CS']
    if cs >= 144:
        results['Computer Science'] = 'Grade 9'
    elif 128 <= cs < 144:
        results['Computer Science'] = 'Grade 8'
    elif 112 <= cs < 128:
        results['Computer Science'] = 'Grade 7'
    elif 96 <= cs < 112:
        results['Computer Science'] = 'Grade 6'
    elif 80 <= cs < 96:
        results['Computer Science'] = 'Grade 5'
    elif 64 <= cs < 80:
        results['Computer Science'] = 'Grade 4'
    elif 48 <= cs < 64:
        results['Computer Science'] = 'Grade 3'
    elif 32 <= cs < 48:
        results['Computer Science'] = 'Grade 2'
    elif 16 <= cs < 32:
        results['Computer Science'] = 'Grade 1'
    elif cs > 0:
        results['Computer Science'] = 'Below Grade 1'

    # Languages
    def lang(name, score):
        if score >= 200:
            return 'Grade 9'
        elif 180 <= score < 200:
            return 'Grade 8'
        elif 160 <= score < 180:
            return 'Grade 7'
        elif 140 <= score < 160:
            return 'Grade 6'
        elif 120 <= score < 140:
            return 'Grade 5'
        elif 100 <= score < 120:
            return 'Grade 4'
        elif 80 <= score < 100:
            return 'Grade 3'
        elif score > 0:
            return 'Below Grade 3'
        return None

    results['French'] = lang('French', vals['french'])
    results['Spanish'] = lang('Spanish', vals['spanish'])
    results['German'] = lang('German', vals['german'])

    # remove None or empty results
    return {k: v for k, v in results.items() if v}


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        results = predict_all(request.form)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
