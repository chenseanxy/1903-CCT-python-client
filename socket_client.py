import socket
import os
import time
from tqdm import tqdm
import sys
import threading

json = os.path.join(".", "record.json")

if len(sys.argv) < 2:
    print("Please specify ip")
    exit()

lines = []

with open(json, mode="r", encoding="utf-8") as f:
    print("Loading...")
    for line in tqdm(f):
        lines.append(line)


def run(lines, numThreads, threadID):
    for i in tqdm(range(int(len(lines)/numThreads))):
        line = lines[i*10 + threadID]
        # print(line)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[1], 5600))
        s.send(bytes(line, "utf-8"))
        s.close()
        # time.sleep(0.01)


numThreads = sys.argv[2]
threads = []

for threadID in range(numThreads):
    t = threading.Thread(target = run, args=(lines, numThreads, threadID))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()


