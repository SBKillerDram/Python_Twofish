# encoding: utf-8
from twofish import Twofish
import os
import struct
import random
import sys
import binascii

def prep_en(x, t):
    tmp = rando(20)
    tmp1 = tmp[:10]
    tmp2 = tmp[10:]
    x = tmp1 + x + tmp2
    tmp3 = ''
    #now rip into 16byte chunks then encrypt
    if len(x)%16 == 0:
        for i in range(1, len(x)/16+1, 1):
            tmp3 += encrypt(x[i*16-16:i*16], t).strip()
    else:
        swtch = 16 - (len(x)%16)

        if swtch == 1:
            x += struct.pack('1B',*([1]*1))
        elif swtch == 2:
            x += struct.pack('2B',*([2]*2))
        elif swtch == 3:
            x += struct.pack('3B',*([3]*3))
        elif swtch == 4:
            x += struct.pack('4B',*([4]*4))
        elif swtch == 5:
            x += struct.pack('5B',*([5]*5))
        elif swtch == 6:
            x += struct.pack('6B',*([6]*6))
        elif swtch == 7:
            x += struct.pack('7B',*([7]*7))
        elif swtch == 8:
            x += struct.pack('8B',*([8]*8))
        elif swtch == 9:
            x += struct.pack('9B',*([9]*9))
        elif swtch == 10:
            x += struct.pack('10B',*([10]*10))
        elif swtch == 1:
            x += struct.pack('11B',*([11]*11))
        elif swtch == 12:
            x += struct.pack('12B',*([12]*12))
        elif swtch == 13:
            x += struct.pack('13B',*([13]*13))
        elif swtch == 14:
            x += struct.pack('14B',*([14]*14))
        elif swtch == 15:
            x += struct.pack('15B',*([15]*15))
        else:
            print("it broked")

        for i in range(1, len(x)/16+1, 1):
            tmp3 += encrypt(x[i*16-16:i*16], t).strip()

    tmp3.strip()
    return tmp3

def rando(i):
    ran = ""
    chars = "abcdefghijklmnopqrstuvwxyz!$%^&*()_+|~-=`{}[]:;<>?,./ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for i in range(i):
        ran+=chars[random.randint(0,len(chars)-1)]

    return ran

def encrypt(passW, key):
    t = Twofish(key)
    x = t.encrypt(passW)
    x = binascii.hexlify(x)
    l3n = len(x)
    x = str(l3n) + x
    return x

def prep_de(tmp, key):
    finP = ''
    for i in range(0, len(tmp)-16, int(tmp[0:2])):
        x = tmp[0:2]
        if x == '':
            break
        else:
            #print("tmp: ",tmp)
            tmp2 = int(tmp[0:2])
            #print tmp2
            tmp3 = tmp[2:tmp2+2]
            #print tmp3
            tmp = tmp[tmp2+2:]
            tmp3 = decrypt(tmp3, key)
            tmp3 = stripPadd(tmp3)
            finP += tmp3.strip()
            #print finP
    finP = finP[10:len(finP)-10]
    return finP

def stripPadd(strs):
    if strs.find('\x01') != -1:
        return strs[:strs.find('\x01')]
    elif strs.find('\x02') != -1:
        return strs[:strs.find('\x02')]
    elif strs.find('\x03') != -1:
        return strs[:strs.find('\x03')]
    elif strs.find('\x04') != -1:
        return strs[:strs.find('\x04')]
    elif strs.find('\x05') != -1:
        return strs[:strs.find('\x05')]
    elif strs.find('\x06') != -1:
        return strs[:strs.find('\x06')]
    elif strs.find('\x07') != -1:
        return strs[:strs.find('\x07')]
    elif strs.find('\x08') != -1:
        return strs[:strs.find('\x08')]
    elif strs.find('\x09') != -1:
        return strs[:strs.find('\x09')]
    elif strs.find('\x10') != -1:
        return strs[:strs.find('\x10')]
    elif strs.find('\x11') != -1:
        return strs[:strs.find('\x11')]
    elif strs.find('\x12') != -1:
        return strs[:strs.find('\x12')]
    elif strs.find('\x13') != -1:
        return strs[:strs.find('\x13')]
    elif strs.find('\x14') != -1:
        return strs[:strs.find('\x14')]
    elif strs.find('\x15') != -1:
        return strs[:strs.find('\x15')]
    else:
        return strs.strip()

def decrypt(passW, key):
    t = Twofish(key)
    x = t.decrypt(binascii.unhexlify(passW))
    return x

def main(arg1,arg2,arg3):
    tmp = ''

    if arg1 == "en":
        tmp = prep_en(arg2, arg3)
        print(tmp)
        sys.stdout.flush()
    elif arg1 == "de":
        tmp = prep_de(arg2, arg3)
        print(tmp)
        sys.stdout.flush()
    else:
        pass

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])

#These lines were used for inital testing and debugging uncomment one of them and comment out the 
#two lines above this and run python twofish_Enc_Dec.py from command line.

#main('en', 'YELLOWSUBMARINES', 'layDqf8KPkpUBR6CFePf5Jqt3Z6pYtcR')
#main('de','32da5a7a9e62df208f9a2234a4efec7aee3242c61162267f805d0817d3008ec656bc322f4ce033c6668c91a0285f8c4f351e29','layDqf8KPkpUBR6CFePf5Jqt3Z6pYtcR')

