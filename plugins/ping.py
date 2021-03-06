# basic "is it alive" tests and simple admin
import datetime
import sys

from espresso.main import robot

@robot.respond(r"(?i)PING")
def ping(res):
    res.send("PONG")

@robot.respond(r"(?i)ECHO (?P<echotext>.*)")
def echo(res):
    res.send(res.match.group('echotext'))

@robot.respond(r"(?i)TIME\?*")
def time(res):
    res.send("Server time is {}".format(datetime.datetime.now().ctime()))

@robot.respond(r"(?i)DIE")
def die(res):
    res.send("Goodbye, cruel world.")
    sys.exit(0)
