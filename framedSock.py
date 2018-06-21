import re

def framedSend(sock, payload, debug=0):
     if debug: print("framedSend: sending %d byte message" % len(payload))
     msg = str(len(payload)).encode() + b':' + payload
     while len(msg):
         nsent = sock.send(msg)
         msg = msg[nsent:]
     
rbuf = b""                      # static receive buffer

def framedReceive(sock, debug=0):
    global rbuf
    while b":" not in rbuf:
        if debug: print("framedReceive: waiting for length.  rbuf=", rbuf)
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
        if debug: print("framedReceive: %d of %d bytes rec'd" % (len(rbuf), msgLength))
        r = sock.recv(100)
        if len(r) == 0:
            print("incomplete payload.  Expected %dB, received only %dB (%s)" % (msgLength, len(rbuf), rbuf))
            return None
        rbuf += r
    payload = rbuf[0:msgLength]
    rbuf = rbuf[msgLength:]
    return payload
