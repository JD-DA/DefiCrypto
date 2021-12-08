import struct
from Crypto.Util.strxor import strxor
from PIL import Image
import numpy as np


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
    numpydata = np.asarray(img)
    (i,j,alpha) = numpydata.shape
    print(i,j)
    print(i*j)
    '''for component in [1,2,0]:
        imageRed = numpydata[:, :, component]
        Image.fromarray(imageRed).save(f"./image{component}.png")'''
    imageRed = numpydata[:, :, 0]
    print("Avant")
    print(imageRed)
    print(imageRed.shape)
# on inverse l'image sur la diagonale pour pouvoir lire les colonnes une par une au lieu des lignes une par une
    #imageRed = np.reshape(imageRed,(1500, 1154), order='F')
    print("apres")
    print(imageRed)
    print(imageRed.shape)
    imageRed = imageRed.reshape(-1)
    print("ligne")
    print(imageRed)
    print(imageRed.shape)

    reader = open("message-mystere.mj", "rb")
    message = reader.readline()
    reader.close()
    masque = bytes(imageRed)
    print(masque[:20])
    print(message[:20])
    size = len(message)
    print(size,len(masque))
    res = strxor(message, masque[:size])
    print(res.decode())


    """print(res)
    for i in range(size,len(masque)-size,size):
        print("")
        res = strxor(message,masque[i:i+size])
        try:
            print(res.decode())
            print(res)
        except:
            print(i," ",end=" ")
"""
    # res = strxor(message, masque[size:2*size])
    # print(res.decode())
    # print(res)
    # res = bytearray(res)
    # for i in range(50):
    #     print(masque[i],message[i],res[i],chr(res[i]))
    #
    # test = []
    # index = 0
    # for l in range(0,i*j,j):
    #     print(l)
    #     print(masque[l],struct.pack(">B",masque[l]))
    #     print(message[index],struct.pack(">B",message[index]))
    #     test = strxor(struct.pack(">B",masque[l]),struct.pack(">B",message[index]))
    #     print(masque[l], message[index],test)
    #     index+=1

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











