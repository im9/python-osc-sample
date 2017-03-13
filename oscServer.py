import liblo
import sys
import subprocess
import time

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

PORT = 7777

print liblo.__file__
try:
    server = liblo.Server(PORT)
except liblo.ServerError, err:
    print str(err)
    sys.exit()


def callback(path, args, types, src):
    param = args[0]
    print OKGREEN + "==> received an osc message '%s' from '%s'" % (path, src.get_url())
    for a, t in zip(args, types):
        print "argument of type '%s': %s" % (t, a)

    print ENDC + "Done!"


server.add_method(None, None, callback)

# loop and dispatch messages every 100ms
while True:
    server.recv(100)
