from time import sleep
from datetime import datetime
import argparse

import life360
import programTime
import fileHandler


parser = argparse.ArgumentParser(description='Receive Credentials for Life360')
parser.add_argument('username', metavar='u', type=str,
                    help='Input username for Life360 (usually an email)')
parser.add_argument('password', metavar='p', type=str,
                    help='Input password for Life360. Input will be suppressed')
parser.add_argument('amount', metavar='n', type=str,
                    help='Input the amount you want to collect data')
parser.add_argument('unit', metavar='t', type=str,
                    help='Input the specific unit you wish for data collection time.')
args = parser.parse_args()

lifeapi = life360.logIn(args.username, args.password)

timer = programTime.getTimer(args.amount, args.unit)
stopTime = datetime.now() + timer

createdFiles = False
while stopTime >= datetime.now():
    userDict = life360.makeUserDict(lifeapi)
    startDate = str(datetime.now().date())

    if not createdFiles:
        if userDict:
            fileHandler.createFilesAndHeaders(userDict, startDate)
            createdFiles = True

    if userDict:
        fileHandler.logData(userDict, startDate)

    print()
    print('Waiting --- ')
    sleep(60*5)  # Every Five Minutes

print('---- Complete ----')
