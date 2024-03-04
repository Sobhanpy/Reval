from melipayamak.melipayamak.melipayamak import Api
from os import environ


def SendSMSTokenView(target, message):
    username = environ.get("SMS_USERNAME")
    password = environ.get("SMS_PASSWORD")
    api = Api(username, password)
    sms = api.sms()
    to = target[0]
    _from = "50002710036456"
    response = sms.send("09100536456", _from, message)
    print(response)
    print(to)
    print(_from)
