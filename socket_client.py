import socket
import os
import time
from tqdm import tqdm

json = os.path.join("C:\\Users\\chenx\\Desktop\\1903_cloud\\python-client", "record.json")

with open(json, mode="r", encoding="utf-8") as f:
    for line in tqdm(f):
        # print(line)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("35.226.124.243", 5600))
        s.send(bytes(line, "utf-8"))
        s.close()
        time.sleep(0.01)
