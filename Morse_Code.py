# Coding Challenge 2
# Name: Gaurav Thapaliya
# Student No:2059614
print('Welcome to Wolmorse \nThis program encodes and decodes morse code')  
morse_code= (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)

#==================Initial Inputs and asking whether to encode or decode==========
def get_input():
    while option():
        d=input("Would you like to encode (e) or decode (d):")
        
        while d !='e' and d !='d':
            
            print("Invalid input")
            d=input("Would you like to encode (e) or decode (d)?")
            
        if d=='e':
            d=input("Would you like to read from a file(f) or console(c)?")
            while d!='f' and d!='c':
                print('Invalid Input')
                d=input('Please enter a valid file(f) or console(c):')
            if d=='c':
                x=input("What would you like to encode:").upper()
                encode(x)
            else:
                file=input("Enter the file name/location:")
                condition='e'
                check_file_exists(file, condition)
                
        elif d=='d':
            d=input("Would you like to read from a file(f) or console(c)?")
            while d!='f' and d!='c':
                print('Invalid Input')
                d=input('Please enter a valid file(f) or console(c):')
            if d=='c':
                y=input("What would you like to decode:").upper()
                decode(y)
            else:
                file=input("Enter the file name:")
                condition='d'
                check_file_exists(file, condition)
                
                
#======================Encoder for console==========================
def encode(message):
    encoded=""
    for letters in message:
        if letters ==" ":
            encoded+="   " 
        else:
            for item in morse_code:
                if item[1]==letters:
                    encoded=encoded+item[0]+" "            
    print(encoded)      

#=====================Decoder for console============================
def decode(message):
    decoded=""
    words=message.split('  ')
    for word in words:
        z=word.split(' ')
        for char in z:
            for item in morse_code:
                if item[0]==char:
                    decoded=decoded+item[1]
        decoded+=" "
    print(decoded)

#====================Extra Credit/Encoding & Decoding File================
def process_lines(filename, mode):
    if mode=='e':
        x=open(filename, 'r')
        s=""
        new=x.readlines()
        for items in new:
            for char in items:
                if char==" ":
                    s+="   "
                else:
                    for pair in morse_code:
                        if char.upper()==pair[1]:
                            s= s+pair[0]+" "
        write_lines(s)
        
    elif mode=='d':
        x=open(filename, 'r')
        g=""
        new=x.readlines()
        for items in new:
            words=items.split('   ')
            for word in words:
                z=word.split(' ')
                for char in z:
                    for item in morse_code:
                        if item[0]==char:
                            g=g+item[1]
                g+=" "
        write_lines(g)
    
#=================New file============================================
def write_lines(lines):
    dc=open('Result.txt', "w")
    dc.write(lines)
    print("Your new file is in the same folder")
    
#==================Checking if file exists or not================================
def check_file_exists(filename,mode):
    
    import os.path

    if os.path.isfile(filename):
        process_lines(filename,mode)
            
    else:
        print ("File does not exist")

#===================Re-running the program=======================================
def option():
    a=input("Would you like to proceed through the program (y)/(n)?")
    
    while a!="y" and a!="n":
        print("Invalid input")
        a=input("Would you like to encode/decode another message?:")
        
    if(a=="y"):
        return True
    elif(a=="n"):
        return False

get_input()


print("Thank you for using Wolmorse.\nGoodbye!!")
  
