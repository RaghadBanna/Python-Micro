


from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
import validators
import shortuuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(255), nullable=False, unique=True)
    short_code = db.Column(db.String(8), nullable=False, unique=True)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json.get('long_url')

    if not validators.url(long_url):
        return 'Invalid URL', 400

    existing_url = URL.query.filter_by(long_url=long_url).first()
    if existing_url:
        return existing_url.short_code

    short_code = generate_short_code()
    new_url = URL(long_url=long_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    return short_code

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url.long_url)

def generate_short_code():
    return shortuuid.uuid()[:8]

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
