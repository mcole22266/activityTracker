from life360API import life360
import datetime

def logIn(username, password):
    '''Gets Username and Password from user and returns api information.'''
    authorization_token = "cFJFcXVnYWJSZXRyZTRFc3RldGhlcnVmcmVQdW1hbUV4dWNyRUh1YzptM2ZydXBSZXRSZXN3ZXJFQ2hBUHJFOTZxYWtFZHI0Vg=="

    print()
    print('Connecting...')
    api = life360(authorization_token=authorization_token,
                  username=username, password=password)

    if not api.authenticate():
        print('Failed to connect. Did you input the correct credentials?')
        print('Quitting')
        quit()

    else:
        print('Connected!')
        return api

def getUserInfo(api):
    '''Takes api information from logIn() and returns a list of users' information.'''
    circles = api.get_circles()
    id = circles[0]['id']
    circle = api.get_circle(id)
    members = circle['members']
    print()
    print('Retrieving information for:')
    users = []
    for n in range(3):
        users.append(members[n])
        firstName = members[n]['firstName']
        print(firstName)
    return users

def getName(user):
    '''Returns user first name.'''
    firstName = user['firstName']
    return firstName

def getBatteryInfo(user):
    '''Returns battery percentage and charging status of user.'''
    battery = 'battery', int(user['location']['battery'])
    charging = 'charging', bool(int(user['location']['charge']))
    return battery, charging

def getLocationInfo(user):
    '''Returns location name, street(?), city(?),
     and whether or not user is driving (bool).'''
    location = 'location', user['location']['name']  # location Name - empty string if None
    address1 = 'address1', user['location']['address1']  # street?
    address2 = 'address2', user['location']['address2']  # city?
    driving = 'driving', bool(int(user['location']['isDriving'])) # driving - true or false
    return location, address1, address2, driving

def getAllUserInfo(user):
    '''Returns list results of all functions above.'''
    name = getName(user)
    battery, charging = getBatteryInfo(user)
    location, address1, address2, driving = getLocationInfo(user)
    info = [battery, charging, location, address1,
            address2, driving]
    userInfo = []
    for feature in info:
        userInfo.append(feature)
    return userInfo

def makeUserDict(api):
    users = getUserInfo(api)
    userDict = {}
    for user in users:
        print()
        name = getName(user)
        print(f'{name}:')
        info = getAllUserInfo(user)
        userDict[name] = {}
        for feature in info:
            userDict[name][feature[0]] = feature[1]
            print(f'{feature[0]}: {feature[1]}')
    return userDict
