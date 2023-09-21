from sys import stdin, stdout
import os 
import random

def get_random_string(length):
    s=""
    while(len(s)<length):
        s+=(chr)(random.randint(ord('a'),ord('z')))
    return s

folder_path=r"Sem3\Python\Assignment_3\text_files"
num_files=int(stdin.readline())
num_lines=int(stdin.readline())
str_len=int(stdin.readline())
for i in range(0,num_files):
    file_name=f"file_{i}.txt"
    file_path=os.path.join(folder_path,file_name)
    with open(file_path,'w') as file:
            for j in range(0,num_lines):
                file.write(get_random_string(str_len)+"\n")