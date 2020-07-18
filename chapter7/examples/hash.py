import hashlib
def hash_file(filename):
    hash=hashlib.sha1()
    with open(filename,"rb") as file:
        chunk=''
        while chunk!= b'':
            chunk=file.read(1024)
            hash.update(chunk)
        return hash.hexdigest()
text=hash_file("A:\\python\\chapter7\\examples\\file1.txt") 
print("Hash of file is: ",text)
        