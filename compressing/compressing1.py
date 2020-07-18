import re
from ast import literal_eval
import os
def compress():
        
        try:
                fileName=input("Enter the filename to be compressed: ")
                fileName="A:\\python\\compressing\\"+fileName
                file=open(fileName)
                text=file.read()
                file.close()
                p=re.compile(r'[\w]+|[\W]')
                split=p.findall(text)
                print(split)
                b=[]
                wordList=[]
                for word in split:
                        try:
                                r=wordList.index(word)+1 #searching for a word which is non existent
                        except ValueError:
                                wordList.append(word)
                                r=len(wordList)
                
                        b.append(r)
                file=open('A:\\python\\compressing\\compressed.txt','w')
                file.write(str(wordList)+'\n'+str(b))
                file.close()
        except:
                print("File does not exist")

def decompress():
        try:
                fileName=input("Enter the name of the file to be decompressed: ")
                fileName="A:\\python\\compressing\\"+fileName
                file=open(fileName)
        except:
                print("File does not exist")
        print("Content of the compressed file is: ")
        words=literal_eval(file.readline().rstrip('\n'))
        print(words)
        pos=literal_eval(file.readline())
        print(pos)
        temp=[]
        for index in pos:
                temp.append(words[index-1])
        sentence=''.join(temp)
        print(sentence)
compress()
decompress()                
