#! /usr/bin/env python3
import sys, re, socket, params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50000),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)
debug, listenPort = paramMap['debug'], paramMap['listenPort']

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(("127.0.0.1", 50001))
mysocket.listen(5)

def main():
    global state
    global mysocket
    state = "init"
    rcvd = b''                  # buffer for rec'd bytes
    (sock, address) = mysocket.accept()
    state = "length"

    while sock:
        if debug: print("state=", state)
        if state == "length":
            match = re.match(b'([^:]+):(.*)', rcvd)
            if match:
                lengthStr, rcvd = match.groups()
                try: 
                    length = int(lengthStr)
                except:
                    if len(recv):
                        print("badly formed message length:", lengthStr)
                    sock = None
                state = "data"
                continue
            buff = sock.recv(100)
            rcvd = rcvd + buff
            if debug: print("read ", buff, 'rcvd=', rcvd)
            if len(buff) == 0:
                print("Socket closed with partial message: %s" % rcvd)
                sock.close()
                sock = None
        else:
            if len(rcvd) >= length:
                sendBytes = rcvd[0:length]
                sendBytes = sendBytes.upper()
                rcvd = rcvd[length:]
                tosend = str(length).encode() + b':' + sendBytes
                if debug: print("about to send %d byte message [%s]" % (length, tosend))
                sock.send(tosend)
                state = "length"
                continue
            buff = sock.recv(100)
            if len(buff) == 0:
                remaining = length - len(rcvd)
                print("socket closed prematurely.  Expected %d bytes, received only %d bytes: %s" % (length, len(rcvd), rcvd))
                sock = None
                continue
            rcvd = rcvd + buff

if __name__ == "__main__":
    main()
    # try:
    # except KeyboardInterrupt:
    #     sys.exit()

