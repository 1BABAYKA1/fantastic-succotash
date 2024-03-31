from flask import redirect, Flask, render_template, jsonify, request, session
from flask_restful import Api
from flask_jwt_simple import JWTManager
import flask
from backend import get_info


app = Flask(__name__)
api = Api(app)
app.jwt = JWTManager(app)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    print(request.form)
    if flask.request.method == 'POST':
        Date = request.form['datestamp']
        n = Date
        year = n.split('-')[0][2:]
        month = n.split('-')[1]
        day = n.split('-')[2]
        light, rooms = get_info(day=day, month=month, year=year)
        print(light)
        return render_template('main.html', title="Wonder Windows", lights=light, rooms=rooms)
    return render_template('start_main.html', title="Wonder Windows")


def main():
    app.run()


if __name__ == '__main__':
    main()