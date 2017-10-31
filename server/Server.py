import socket, _thread,pickle
from  CONST import *

share = {}
class Server:
   def __init__ (self,portID):
      serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.port = portID
      self.host = socket.gethostname()
      serverSocket.bind((self.host,self.port))
      serverSocket.listen(10)
      self.socket = serverSocket
      print("server run with ip: ",self.host," and  port : ",self.port)
   def threadRun(self,connection,adder):
       choose = self.recFrom(connection)
       print(choose)
       if(choose == REGISTER):
           registerFiles  = self.recFrom(connection)
           peer = registerFiles[0]
           successsaved = " "
           faildSaved = " "
           for fileName in registerFiles[1]:
               result = self.register(fileName,peer)
               if result:
                    successsaved = successsaved + " , "+fileName

               else:
                    faildSaved = faildSaved + "," + fileName

           massage = "File  Saved  is " + successsaved +" and  file added  before  is " + faildSaved
           self.sendTo(connection,massage)
       else:
           fileName = self.recFrom(connection)
           search = self.search(fileName)
           if(search == True):
               self.sendTo(connection,share[fileName])
           else:
               self.sendTo(connection,"SORRY NO file with this name")
       print(share)
   def run(self):
       while True :
        clientSocket,connection = self.socket.accept()
        print("connect with client  have ip : ",connection[0]," and  port ",connection[1])
        _thread.start_new_thread(self.threadRun,(clientSocket,connection))

   def search(self,index):
       if(index in share.keys()):
          return  True
       else : return False


   def recFrom(self,connection):
       msg = connection.recv(4069)
       return pickle.loads(msg)
   def sendTo(self,connection,mass):
       connection.send(pickle.dumps(mass))
   def register(self,fileName,peer):
       if (self.search(fileName)):
           oldValue = share.get(fileName)
           if peer in oldValue:
               return  False
           else:
               share[fileName] = oldValue + [peer]
               return  True

       else:
           share[fileName] = [peer]
           return  True
