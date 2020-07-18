#html documents are produced of a particular website
import urllib.request
x=urllib.request.urlopen('https://www.google.com')
print(x.read())

#little complex in that field itself
url="https://www.google.com/search?q=python"
headers={}
headers['User-Agent']="Mozilla/5.0 (X11;Linux i686) AppleWebKit/537.17 (KHTML,like Gecko) Chrome/24.0.1312.27 Safari/537.17"
Request=urllib.request.Request(url,headers=headers)
Response=urllib.request.urlopen(Request)
Data=Response.read()
with open("A:\\python\\chapter7\\examples\\URL_File.txt",'w') as file:
    file.write(str(Data))
print("Content written in file........")

