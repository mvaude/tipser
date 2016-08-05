#!/usr/bin/env python

import argparse
import os
import json

from twitter import Api

# Either specify a set of keys here or use os.getenv('CONSUMER_KEY') style
# assignment:

CONSUMER_KEY = os.getenv("CONSUMER_KEY", None)
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", None)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", None)
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", None)

# Users to watch for should be a list. This will be joined by Twitter and the
# data returned will be for any tweet mentioning:
# @twitter *OR* @twitterapi *OR* @support.
USERS = ['349094942',
         '633673441',
         '4221690875',
         '3096291947',
         '2264164707']

# Since we're going to be using a streaming endpoint, there is no need to worry
# about rate limits.
api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)


def main():
    parser = argparse.ArgumentParser(description='Tipser Logger')

    args = parser.parse_args()

    with open('output.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(follow=USERS):
            f.write(json.dumps(line))
            f.write('\n')


if __name__ == '__main__':
    main()
