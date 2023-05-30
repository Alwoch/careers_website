from flask import Flask

app = Flask(__name__)

import testimonials.routes #This has to be at the botton of the flask instance to avoid circular imports