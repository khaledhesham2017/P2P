import socket, _thread,pickle, threading
from  CONST import *
class Server(threading.Thread):
   def __init__(self, portID):
      super().__init__()
      serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.port = portID
      self.host = socket.gethostname()
      serverSocket.bind((self.host,self.port))
      serverSocket.listen(10)
      self.socket = serverSocket
      print("server run with ip: ",self.host," and  port : ",self.port)
   def threadRun(self,connection,adder):
      fileName = self.recFrom(connection)
      fo = open(fileName,'r+')
      data = fo.read()
      fo.close()
      self.sendTo(connection,data)

   def run(self):
       while True :
        clientSocket,connection = self.socket.accept()
        print("connect with client  have ip : ",connection[0]," and  port ",connection[1])
        _thread.start_new_thread(self.threadRun,(clientSocket,connection))

   def recFrom(self,connection):
       msg = connection.recv(1024)
       return pickle.loads(msg)
   def sendTo(self,connection,mass):
       connection.send(pickle.dumps(mass))
