# TRUE-GCSE-GRADE-PREDICTOR-

This repo contains a small Flask web app that predicts GCSE/mock grades from numeric inputs.

Local run
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Deploying to PythonAnywhere (short guide)
- Create a PythonAnywhere account and sign in.
- Push this repo to GitHub (or zip/upload files) so you can get them onto PythonAnywhere.

On PythonAnywhere:
1. In "Files" or a Bash console, clone your repo: `git clone <your-repo-url>`
2. Create a virtualenv in the same Python version as your web app, e.g.: `python3.10 -m venv myvenv`
3. Activate and install: `source myvenv/bin/activate` then `pip install -r requirements.txt`
4. Go to the "Web" tab and create a new web app. Choose "Flask" and the correct Python version.
5. Set the source code directory to the directory where `app.py` is located.
6. Edit the WSGI configuration file (PythonAnywhere provides a link) to point to `app.py`. For example, set the Flask app by adding:

```python
import sys
path = '/home/yourusername/path/to/cloned/repo'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

7. Reload the web app from the PythonAnywhere Web tab.

Notes and troubleshooting
- Make sure `templates/` and `static/` folders are present at the project root on PythonAnywhere.
- If CSS doesn't load, check the static path in the Web tab and that `static/css/style.css` exists.
- Check error logs (on the Web tab) if the app fails to start; they usually tell what's wrong.
