def sendAll(sock, buf):
    while len(buf):
        print(f"trying to send <{buf}>...")
        nbytes = sock.send(buf)
        print(f" {nbytes} bytes sent, {len(buf) - nbytes} bytes remain")
        buf = buf[nbytes:]

