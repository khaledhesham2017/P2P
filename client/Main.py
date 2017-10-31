import Client ,Server,_thread
from CONST import *
import  pickle
ser = Server.Server(Client2Port)
ser.start()
downloadDir = 'downloaded'

while True:
    x = input("welcome  to p2p ...... \n 1-register \n 2-search \n"
              " 3-download from peer \n 4-exit\n ")
    if( x == REGISTER ) :
        client = Client.Client(PORT)
        client.run()
        client.sendto(REGISTER)
        size = input("enter number of file you want register  : ")
        filesName =[]
        for i in range(0,int(size)):
            massage =" enter file name number " + str(i+1)  + " : "
            fileName = input(massage)
            filesName.append(fileName)
        massage = (Client1Port,filesName)
        client.sendto(mass=massage)
        #for i in range(0, int(size)):
        massage = client.recFrom()
        print(massage)
        client.close()
    elif(x==SEARCH):
        client = Client.Client(PORT)
        client.run()
        fileName = input("enter file  name you want search : ")
        client.sendto(SEARCH)
        client.sendto(mass=fileName)
        massage = client.recFrom()
        print(massage)
        client.close()
    elif x == DOWNLOAD:
        peer = input("Enter the peer that you want download from : ")
        client = Client.Client(int(peer))
        client.run()
        fileName = input("Enter the file that you want download  : ")
        client.sendto(fileName)
        inp = client.recFrom()
        fo = open(fileName + "downloaded", 'w+')
        fo.write(inp)
        fo.close()

    else:
        print("thanks!!!")
        break
