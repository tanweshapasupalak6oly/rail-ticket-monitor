# rail-ticket-monitor

A scheduled Python project for checking ticket availability and fares on a route, then alerting when a better option appears.

## Current status

- GitHub Actions workflow runs every 15 minutes
- Python entrypoint is in `src/main.py`
- Dependencies are listed in `requirements.txt`

## Next steps

- Add ticket checking logic
- Store previous results
- Send alerts when fares drop or seats open up
