import csv
import os
import time
import random
from sys import stdin, stdout
#stdin.readline() #use instead of input()
#stdout.write()   #use instead of print()

start=time.time()

def capitalize(s):
    ans=""
    for i in s:
        if(i=='\n'):
            return ans
        ans+=(chr)(ord(i)+ord('A')-ord('a'))
    return ans

folder_path=r"Sem3\Python\Assignment_3\text_files"
for i in range(0,500):
    file_name=f"file_{i}.txt"
    file_path=os.path.join(folder_path,file_name)
    with open(file_path,'w') as file:
        for line in file:
            print(line)

