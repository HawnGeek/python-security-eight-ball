import socket
import _thread #import all functions from the thread library by their own name
host = '127.0.0.1'
port = 4444

def clientthread(conn):
    #Send a message back to the user that connected over this socket connection
    conn.send(b'You have summoned the Security Eight Ball, what is your question?\n')
   
    while True:
        #Receive new messages from the client
        data = conn.recv(1024)
        reply = (b'You asked: ' + data)
        if not data:
            break
        conn.sendall(reply)
    conn.close() #close only this connection

def create_server():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind to the host and port
    s.bind((host, port))
    # listen and accept a max of 5 connections
    s.listen(5)


    while True:
    # Wait for someone to try to connect and accept the connection
    c, addr = s.accept()
    print('Got connection from', addr)
    # send a response
    _thread.start_new_thread(clientthread, (c, ))
    # close the connection
    c.close()

if __name__ == '__main__':
  create_server()

