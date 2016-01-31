#!/usr/bin/python3

import os
import sys
import csv
import datetime
import time
import twitter

from secrets import *


def tweet(down, up, location):
    try:
        my_auth = twitter.OAuth(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)

        tweet = "Hey @Comcast @ComcastCares why is my internet down?\
                I pay for {0} down\\{1} up in {2}? #comcastoutage \
                #comcast".format(str(down), str(up), str(location))
        twit.statuses.update(status=tweet)
        print("Status updated")
    except:
        print('Error tweeting')


def test():
    # run speedtest-cli
    print('Running Speed Test... Please Wait')
    speed_test_result = os.popen("speedtest-cli --simple").read()

    # split the 3 line result (ping,down,up)
    lines = speed_test_result.split('\n')
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # if speedtest could not connect set the speeds to 0
    if 'Cannot' in speed_test_result:
        ping = 100
        down_speed = 0
        up_speed = 0

    # extract the values for ping down and up values
    else:
        ping = lines[0][6:11]
        down_speed = lines[1][10:14]
        up_speed = lines[2][8:12]
    print("Date: {0} \nPing: {1} \nDown: {2} \nUp: {3}\n".format(str(date), str(ping), str(down_speed), str(up_speed)))

    # save the data to file for local network plotting
    with open('data.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow((ts*1000, ping, down_speed, up_speed))

    # try to tweet if speedtest couldnt even connect.
    # Probably wont work if the internet is down
    if 'Cannot' in speed_test_result:
        tweet(150, 10, 'Washington DC')

    # tweet if down speed is less than whatever I set
    elif eval(down_speed) < 50:
        # i know there must be a better way than to do (str(int(eval())))
        tweet(
            str(int(eval(down_speed))),
            str(int(eval(up_speed))),
            'Washington DC')


if __name__ == '__main__':
    try:
        test()
        print('Completed')
    except KeyboardInterrupt:
        print('\nCancelling')
