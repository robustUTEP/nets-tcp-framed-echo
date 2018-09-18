# Echo client program
import socket
import sys

serverHost = 'localhost'
serverPort = 50006

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print "creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto)
        s = socket.socket(af, socktype, proto)
    except socket.error, msg:
        print " error: %s" % msg
        s = None
        continue
    try:
        print " attempting to connect to %s" % repr(sa)
        s.connect(sa)
    except socket.error, msg:
        print " error: %s" % msg
        s.close()
        s = None
        continue
    break

if s is None:
    print 'could not open socket'
    sys.exit(1)

outMessage = "Hello world!"

print "sending '%s'" % outMessage
s.send(outMessage)

data = s.recv(1024)
print "Received '%s'" % data

print "sending '%s'" % outMessage
s.send(outMessage)

s.shutdown(socket.SHUT_WR)      # no more output

while 1:
    data = s.recv(1024)
    print "Received '%s'" % data
    if len(data) == 0:
        break
print "Zero length read.  Closing"
s.close()
