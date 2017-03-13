import liblo
import sys
import argparse

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

PORT = 7777

def sendOsc(port, url, param):
    try:
        target = liblo.Address("127.0.0.1", port)
    except liblo.AddressError, err:
        print str(err)
        sys.exit()
    liblo.send(target, url, param)


if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument('--version', action='version', version='%(prog)s 0.1.0')
    p.add_argument('-p', action="store", type=int,
                    help='an integer for the accumulator')
    args = p.parse_args()

    # send OSC message
    if args.p:
        print OKBLUE + "==> send message port=" + str(PORT) + " param=" + str(args.p)
        sendOsc(PORT, "/send/start", 1)
        print ENDC + "OK!"


