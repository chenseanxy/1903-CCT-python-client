import socket
import random
import sys

if len(sys.argv) < 2:
    print("Please specify ip")
    exit()

while True:
    longitude = random.random()+300
    latitude = random.random()+300
    line = '{"eid":"33041100000789","time":1496246453,"placeId":42,"address":"长虹村万安桥北侧","longitude":'+ str(longitude) +',"latitude":'+str(latitude) + "}"
    print(line)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], 5600))
    s.send(bytes(line, "utf-8"))
    s.close()
