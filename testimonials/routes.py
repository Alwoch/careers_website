from testimonials import app

@app.route('/')
def index():
    return 'Hello'

@app.route('/api/testimonials')
def testimonials():
    return {"testimonials":["great","its okay"]}