"""
Ceasar Cipher and Ceasar Cipher revealer
outputs all to a text file
Benjamin D. Miller
"""

"""
Takes a message m and an integer key value(0-25)
to encode a ceasar cipher message
"""
def ceasar(m,key):
    new = ""
    for i in range(len(m)):
        if(ord(m[i])+key>90):
           letter = chr(ord(m[i]) + key - 26)
        else:
            letter = chr(ord(m[i]) + key)
        new = new + letter
    return new

"""
Reveals all 26 ceasar ciphers of
a message m writes them to 'crypts.txt'
"""
def ceasarReveal(m)
    f = open("crypts.txt",'w')
    for i in range(26):
        line = ceasar(m,i) + "\n"
        f.write(line)
    f.close()

### Test cases
# ceasarReveal("JFNCPHFJUGFNOGGHBFDJKBGGJBV")
