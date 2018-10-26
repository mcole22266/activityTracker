from datetime import datetime

def createFilesAndHeaders(userDict, startDate):
    for user in userDict:
        filename = f'./Logs/{user}Log{startDate}.csv'
        print(f'Creating {user}\'s log file.')
        with open(filename, 'a+') as f:
            f.write('datetime')
            f.write(', ')
            for feature in userDict[user].keys():
                f.write(feature)
                f.write(', ')
            f.write('\n')

def logData(userDict, startDate):
    logTime = str(datetime.now())
    for user in userDict:
        filename = f'./Logs/{user}Log{startDate}.csv'
        print(f'Logging {user}\'s data.')
        with open(filename, 'a+') as f:
            f.write(logTime)
            f.write(', ')
            for info in userDict[user].values():
                f.write(str(info))
                f.write(', ')
            f.write('\n')
