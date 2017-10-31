import  socket,pickle
class Client:
    def __init__(self,portID):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = portID
    def run(self)  :
        try:
            self.socket.connect((self.host,self.port))
        except:
            print("Server Not Available")
            return  False


    def sendto(self,mass):
       self.socket.send(pickle._dumps(mass))
    def recFrom(self):
        mass = self.socket.recv(10024)
        return  pickle.loads(mass)
    def close(self):
        self.socket.close()
