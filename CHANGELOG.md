# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2024-09-14
### Changed
- Moved code from `app.py` to `project/__init__.py`
- Cleaned up `requirements.txt`

### Added
- Dockerfile and Docker Compose file for setting up with Docker

## [0.0.4] - 2024-08-01
### Changed
- Replaced the `returnDateObject()` function using `DateObject` Class instead

## [0.0.3] - 2024-01-18
### Added
- Error handling for incorrect timezones via HTTP 400 error
- Specifying `GET` request method for main app

### Changed
- Function now returns datetime object which is then used to format and alter the time within the main app's return

### Fixed
- Order of data returned was off due to returning extra variable from date function
- Fixed handling timezone argument

## [0.0.2] - 2024-01-17
### Added
- Function to return all the data
- Accepting arguments for timezones
- Added epoch, date, breakdown by day, month, year, hour, minute, seconds

## [0.0.1] - 2024-01-16
### Added
- Initial commit
