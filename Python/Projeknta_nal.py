alles = True
work = True
xor = False
des = False
vigenere = False
cmd = ""

def xor_op(txt, key="alphabet"):
    pass

while alles:

    
    cmd = input("Enter command: ").lower
    if cmd == "test":
        xor_op("a", "bcd")
        
    while work:

        
        if cmd == "xor":
            xor = True
            work = False
        elif cmd == "des":
            des = True
            work = False
        elif work == "vigenere":
            vigenere = True
            work = False
    
    
    while xor:

        pass