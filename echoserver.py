import socket
import sys

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind(("127.0.0.1", 50000))
mysocket.listen(5)
state = "init"
buff = b''
rcvd = b''

def main():
	global state
	global mysocket
	global buff
	global rcvd
	while True:
		if state == "init":
			print(state)
			(sock, address) = mysocket.accept()
			state = "length"
		elif state == "length":
			print(state)
			if b':' in rcvd:
				state = "data"
				length = int(rcvd.split(b':')[0])
				rcvd = rcvd.split(b':')[1]
				continue
			buff = sock.recv(100)
			print(rcvd)
			rcvd = rcvd + buff
			print(rcvd)
		else:
			print(state)
			if len(rcvd) >= length:
				tosend = str(length).encode() + b':' + rcvd.upper()
				print(tosend)
				sock.send(tosend)
				state = "length"
				rcvd = b''
				length = b''
				continue
			buff = sock.recv(100)
			rcvd = rcvd + buff

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		mysock.close()
		sys.exit()

