# Echo server program
import socket

clientHost = ''                 # Symbolic name meaning all available interfaces
clientPort = 50006              # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((clientHost, clientPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

conn, addr = s.accept()  # wait until incoming connection request (and accept it)
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    sendMsg = "Echoing %s" % data
    print "Received '%s', sending '%s'" % (data, sendMsg)
    conn.send(sendMsg)
conn.close()

