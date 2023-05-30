from testimonials import app
from flask import render_template, abort

testimonials = [
    {"id": 10,
     "name": "Sophia",
     "message": "Your courses helped me land a role at google"
     },
    {"id": 11,
     "name": "Alwoch",
     "message": "Wonderful course"
     }
]


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
@app.route('/testimonials')
def index():
    return render_template('index.html', testimonials=testimonials)


@app.route('/testimonials/<id>')
def show_testimonial(id):
    for testimonial in testimonials:
        if testimonial.get('id') == int(id):
            return render_template('testimonial.html', testimonial=testimonial)
    abort(404)
