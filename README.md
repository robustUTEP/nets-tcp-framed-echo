# nets-tcp-framed-echo
tcp echo with framing

Directory `simple-demo` includes a simple tcp echo server & client

Directory `lib` includes the params package required for many of the programs

Directory `stammer-proxy` includes stammerProxy, which is useful for demonstrating and testing framing

*   `stammerProxy.py` forwards tcp streams. It may delay the transmission of data but ensures all data will be forwarded, eventually.
   By default,
   it listens on port 50000 and forwards to localhost:50001.  Use the -?
   option for help.

Directory `framed-echo` includes code that implements framing described below

*  `framedClient.py` and `framedServer.py` are a demonstration TCP client and server which exchange frames consisting of byte arrays in the form payload_length:payload where payload_length is in decimal.

* FramedForkServer uses `fork()` to handle multiple simultaneous clients.    

*  The -? (usage) option prints parameters and default values. 

*  `framedSock.py` holds the common code used in the client and server including framed send and receive.



Your assignment is to write `fileClient.py` and `fileServer.py` which can transfer a file ("put localName remoteName") from a client to the server. Your programs should: 

* be in the file-transfer-lab subdir
* work with and without the proxy
* support multiple clients simultaneously using `fork()`
* gracefully deal with scenarios such as: 
    * zero length files
    * user attempts to transmit a file which does not exist
    * file already exists on the server
    * the client or server unexpectedly disconnect
* optional (unless you're taking this course for grad credit): be able to request ("get") files from server

