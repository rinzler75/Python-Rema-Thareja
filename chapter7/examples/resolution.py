def find_res(filename):
    with open(filename,'rb') as img_file:
        #height of image is at 164th position
        img_file.seek(163)
        #read the 2 bytes
        a=img_file.read(2)
        #calculate height
        height=(a[0]<<8)+a[1]
        #read next 2 bytes which stores the width
        a=img_file.read(2)
        #calculate width
        width=(a[0]<<8)+a[1]
    print("IMAGE RESOLUTION IS: ",width,"X",height)
find_res("A:\\python\\chapter7\\examples\\image.jpg")