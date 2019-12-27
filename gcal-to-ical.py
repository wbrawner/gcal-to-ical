#!/usr/bin/env python3

from urllib.parse import urlparse,parse_qsl
import sys
from pprint import pprint

ICAL_FORMAT = 'https://calendar.google.com/calendar/ical/{}/public/basic.ics'

def main(cli_input):
    gcal_url = o = urlparse(cli_input)
    query_string = gcal_url.query
    src = parse_qsl(query_string)
    for pair in parse_qsl(query_string):
        if pair[0] == 'src':
            print(ICAL_FORMAT.format(pair[1]))
            return

if __name__ == '__main__':
    main(sys.argv[1])

