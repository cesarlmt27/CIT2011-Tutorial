import threading
import os
import digest
import config
import sys

ROOT_PATH = sys.argv[1] if len(sys.argv) == 2 else config.ROOT_PATH

# Formato:
# {
#  nombre: str, ext: str, hash: hex str, threat: bool  
# }
DATA_FILES = []
mutex = threading.Lock()


def recursiveThreading(MYROOT_PATH):
    file_list = os.listdir(MYROOT_PATH)
    
    for fileName in file_list:
        curPath = f"{MYROOT_PATH}/{fileName}"
        if not os.path.isfile(curPath):
            t = threading.Thread(target=recursiveThreading, args=(curPath,))
            t.start()
            t.join()
            
        else:
            mutex.acquire()
            res = digest.formatAndGetData(curPath)
            DATA_FILES.append(res)  
            mutex.release()  

# INI THREAD
# Usamos abs path
if ROOT_PATH != os.path.abspath(ROOT_PATH):
    ROOT_PATH = os.path.abspath(ROOT_PATH)
ROOT_PATH = ROOT_PATH.replace("\\", "/")

t = threading.Thread(target=recursiveThreading, args=(ROOT_PATH,))
t.start()
t.join()

for fileName in DATA_FILES:
    print(f"{fileName}\n\n")