from flask import Flask, render_template, request, send_file
from weasyprint import HTML
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        profile = request.form.get('profile')
        experience = request.form.get('experience')
        education = request.form.get('education')
        skills = request.form.get('skills')
        languages = request.form.get('languages')
        template_choice = request.form.get('template', 'classic')

        html = render_template(
            'resume_template.html',
            name=name,
            email=email,
            phone=phone,
            profile=profile,
            experience=experience,
            education=education,
            skills=skills,
            languages=languages,
            template=template_choice
        )
        pdf = HTML(string=html).write_pdf()
        return send_file(
            io.BytesIO(pdf),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='resume.pdf'
        )
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
