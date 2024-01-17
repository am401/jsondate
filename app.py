import datetime
import pytz
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request

app = Flask(__name__)
# Retain the order for the keys that is configured in the application
app.json.sort_keys = False

def getDate(timezone=None):
    if timezone is None:
        date = datetime.datetime.now(ZoneInfo('UTC'))
    else:
        date = datetime.datetime.now(pytz.timezone(timezone))
    dateISOFormat = date.isoformat()
    dateEpoch = int(date.timestamp())
    dateFull = date.strftime('%Y-%m-%d')
    dateYear = date.strftime('%Y')
    dateMonth = date.strftime('%b')
    dateDay = date.strftime('%a')
    hour = date.strftime('%H')
    minute = date.strftime('%M')
    seconds = date.strftime('%S')
    return date,dateISOFormat,dateEpoch,dateFull,dateYear,dateMonth,dateDay,hour,minute,seconds

@app.route("/")
def home():
    requestArg = request.args.get('timezone')
    if requestArg is not None:
        dateTuple = getDate(requestArg) 
    else:
        dateTuple = getDate()
    return jsonify(
        dateTime=dateTuple[0],
        epoch=dateTuple[1],
        date=dateTuple[2],
        year=dateTuple[3],
        month=dateTuple[4],
        day=dateTuple[5],
        hour=dateTuple[6],
        minute=dateTuple[7],
        seconds=dateTuple[8]
        )


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(
        errorMessage="The page you requested could not be found."
        ), 404
        
if __name__ == '__main__':
    app.run()
