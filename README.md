# CV/Resume Generator

This Flask application collects resume information via a form and generates a PDF using WeasyPrint.

## Setup

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
python3 app.py
```

Visit `http://localhost:5000` in your browser to generate a resume.

Select a template from the drop-down menu to switch between the "Classic" and
"Modern" styles.

## Package the app

To create a zip archive for distribution, run:

```bash
zip -r resume_app.zip .
```

Users can unzip the archive, install the requirements, and run the app locally
with the commands above.
