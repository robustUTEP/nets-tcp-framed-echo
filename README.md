# nets-tcp-framed-echo
tcp echo with framing

echoserver.py is a TCP server which reads data in the form of "5:hello" and responds "5:HELLO".

It is compatible with the provided proxy.py which sends data intermittently such that multiple message may arrive simultaneously even though they were sent individually.

Your assignment is to write fileclient.py and fileserver.py which can transfer a file from a client to the server. Your programs should 

* work with the proxy
* support multiple simultaneous clients

