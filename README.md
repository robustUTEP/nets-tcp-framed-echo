# nets-tcp-framed-echo
tcp echo with framing

`framedClient.py` and `framedServer.py` are a TCP client and server which parse data in the form of "number:dataToUpperCase".

`framedSock.py` holds the common code used in the client and server including framed send and receive.

`params.py` adds the ability to configure the other python files with command-line parameters

`stammerProxy.py` forwards tcp data between two programs. It may delay the transmission of data but ensures all data will be forwarded, eventually.

Your assignment is to write `fileClient.py` and `fileServer.py` which can transfer a file from a client to the server. Your programs should: 

* work with and without the proxy
* support multiple clients simultaneously using `fork()`
* gracefully deal with scenarios such as: 
    * zero length files
    * user attempts to transmit a file which does not exist
    * file already exists on the server
    * the client or server unexpectedly disconnect
* optional: be able to request files from server

