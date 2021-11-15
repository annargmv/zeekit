from flask import Flask
from utils.db import db
from utils.http_auth import auth


from views import (
    blogpost_api,
    products_api,
)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zeekit@localhost:5432/zeekit'

db.init_app(app)

app.register_blueprint(blogpost_api, url_prefix='/blogpost')
app.register_blueprint(products_api, url_prefix='/product')

POSTGRES = {
    'user': 'postgres',
    'pw': 'zeekit',
    'db': 'zeekit',
    'host': 'localhost',
    'port': '5432',
}


@app.route('/login')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


def main():
    app.run("0.0.0.0", port=3000)


if __name__ == "__main__":
    main()
