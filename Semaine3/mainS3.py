import struct
from Crypto.Util.strxor import strxor
from PIL import Image
from numpy import *


def tableToBytes(table):
    return b"".join([struct.pack('>B', x) for x in table])

def writeInBinaryFile(data, fileDir="./reponse.7zip"):
    with open(fileDir, 'wb') as f:
        f.write(data)

def splitIV(table, position):
    IV = [table[x] for x in range(position)]
    newTable = table[position:]
    return (IV, newTable)

if __name__ == "__main__":
    img = Image.open('image-defi.png')
    numpydata = asarray(img)
    (i,j,alpha) = numpydata.shape
    print(i,j)
    print(i*j)
    for i in [1,2,0]:
        imageRed = numpydata[:, :, i]
        Image.fromarray(imageRed).save(f"./image{i}.png")
    imageRed=imageRed.reshape(-1)
    print(imageRed)
    print(imageRed.shape)

    reader = open("message-mystere.mj", "rb")
    message = reader.readline()
    reader.close()
    masque = bytes(imageRed)
    print(masque[:20])
    print(message[:20])
    print(len(message),len(masque))
    res = strxor(message,masque[:len(message)])
    print(res.decode())
    print(res)
    res = bytearray(res)
    for i in range(50):
        print(masque[i],message[i],res[i],chr(res[i]))
    #
    # reader = open("ctr-1", "rb")
    # message1 = reader.readline()
    # reader.close()
    # print(len(message1), len(masque))
    # print(strxor(message1, masque[:len(message1)]))
    #
    # reader = open("ctr-2", "rb")
    # message2 = reader.readline()
    # reader.close()
    # print(len(message2), len(masque))
    # res = strxor(message2, masque[:len(message2)])
    # index = 0


    #print(strxor(message1, message2[:len(message1)]))











