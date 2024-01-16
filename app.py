import datetime
from zoneinfo import ZoneInfo

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    todaysDate = datetime.datetime.now(ZoneInfo('UTC'))
    todaysDateJSON = todaysDate.isoformat()
    return jsonify(
        dateTime=todaysDateJSON
        )

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(
        errorMessage="The page you requested could not be found."
        ), 404
        
if __name__ == '__main__':
    app.run()
