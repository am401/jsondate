class DateObject:
    def __init__(self, todaysDate, **kwargs):
        self.dateTime = todaysDate.isoformat()
        self.epoch = todaysDate.timestamp()
        self.__dict__.update(kwargs)
        for k, v in self.__dict__.items():
            setattr(self, k, todaysDate.strftime(str(v)))


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
    requestArg = request.args.get('timezone')
    if requestArg is None:
        now = datetime.datetime.now(pytz.utc)
    else:
        try:
            now = datetime.datetime.now(pytz.timezone(requestArg))
        except pytz.exceptions.UnknownTimeZoneError:
            abort(400)
    dateObject = DateObject(
        now,
        fulldate='%Y-%m-%d',
        year='%Y',
        month='%b',
        day='%a',
        hour='%H',
        minute='%M',
        second='%S'
    )
    return jsonify(
        dateTime=dateObject.dateTime,
        epoch=int(float(dateObject.epoch)),
        date=dateObject.fulldate,
        year=dateObject.year,
        month=dateObject.month,
        day=dateObject.day,
        hour=dateObject.hour,
        minute=dateObject.minute,
        second=dateObject.second
    )

if __name__ = '__main__':
	app.run()
