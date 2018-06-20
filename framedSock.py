import re

def framedSend(sock, payload):
     msg = str(len(payload)).encode() + b':' + payload
     sock.send(msg)
     
rbuf = b""                      # static receive buffer

def framedReceive(sock):
    global rbuf
    while b":" not in rbuf:
        r = sock.recv(100)
        if len(r) == 0:
            if len(rbuf) != 0:
                print("incomplete message length (sock closed):", rbuf)
            return None 
        rbuf += r
    match = re.match(b'([^:]+):(.*)', rbuf) # look for colon
    lengthStr, rbuf = match.groups()
    try: 
        msgLength = int(lengthStr)
    except:
        if len(rbuf):
            print("badly formed message length:", lengthStr)
            return None
    while len(rbuf) < msgLength:
        r = sock.recv(100)
        if len(r) == 0:
            print("incomplete payload.  Expected %dB, received only %dB: %s" % (msgLength, len(r), r))
            return None
    payload = rbuf[0:msgLength]
    rbuf = rbuf[msgLength:]
    return payload
