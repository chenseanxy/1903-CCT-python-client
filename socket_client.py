import socket
import os
import time
from tqdm import tqdm
import sys

json = os.path.join(".", "record.json")

if len(sys.argv) < 2:
    print("Please specify ip")
    exit()

lines = []

with open(json, mode="r", encoding="utf-8") as f:
    print("Loading...")
    for line in tqdm(f):
        lines.append(line)

for line in tqdm(lines):
    # print(line)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], 5600))
    s.send(bytes(line, "utf-8"))
    s.close()
    # time.sleep(0.01)
