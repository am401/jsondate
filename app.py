import datetime
import pytz
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
# Retain the order for the keys that is configured in the application
app.json.sort_keys = False

def returnDateObject():
    date = datetime.datetime
    return date

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(
        errorMessage="The page you requested could not be found."
        ), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify(
        errorMessage="Unknown timezone provided."
        ), 400


@app.route("/", methods=['GET'])
def home():
    dateObject = returnDateObject()
    requestArg = request.args.get('timezone')
    if requestArg is None:
        dateObject = dateObject.now(pytz.utc)
    else:
        try:
            dateObject = dateObject.now(pytz.timezone(requestArg))
        except pytz.exceptions.UnknownTimeZoneError:
            abort(400)
    return jsonify(
        dateTime=dateObject.isoformat(),
        epoch=int(dateObject.timestamp()),
        date=dateObject.strftime('%Y-%m-%d'),
        year=dateObject.strftime('%Y'),
        month=dateObject.strftime('%b'),
        day=dateObject.strftime('%a'),
        hour=dateObject.strftime('%H'),
        minute=dateObject.strftime('%M'),
        second=dateObject.strftime('%S')
        )
    
        
if __name__ == '__main__':
    app.run()
