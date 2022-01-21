# File: SubstitutionCipher.py
# Student: Taran Nudurumati

# Date Created:4/10/21
# Date Last Modified: 4/12/21
# Description of Program: This program takes a string and performs several functions to encrypt and decrypt the message
    
import random

# A global constant defining the alphabet. 
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"
UCLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# You are welcome to use the following two auxiliary functions, or 
# define your own.   You don't need to understand this code at this
# point in the semester. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt. 

class SubstitutionCipher:
    key = None
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.__currentKey = key 
    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        return self.__currentKey

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(newKey) == True:
            self.__currentKey = newKey
            
    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""
        encryptedResult = ""
        key = self.__currentKey
        index = None
        newLetter = ""
        found = False
        for i in range(len(plaintext)): #Checks among range of plaintext
            for j in range(len(LCLETTERS)): #Checks among range of lowercase letters
                if plaintext[i] == LCLETTERS[j]: 
                   index = j
                   newLetter = key[index]
                   newLetter = newLetter.replace(plaintext[i], newLetter)
                   encryptedResult+=newLetter
                   found = True
                   break
                elif plaintext[i] == UCLETTERS[j]:
                    index = j
                    newLetter = key[index].upper()
                    newLetter = newLetter.replace(plaintext[i], newLetter)
                    encryptedResult+=newLetter
                    found = True
                    break
                else: 
                    found = False 
            if found == False:
                encryptedResult = encryptedResult + plaintext[i]
            continue
        
        print("    The encrypted text is: " + encryptedResult)
        return encryptedResult
            
    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        key = self.__currentKey
        decryptedResult = ""
        newLetter = ""
        found = False
        for i in range(len(ciphertext)): #Checks among range of plaintext
            for j in range(len(key)): #Checks among range of lowercase letters

               if ciphertext[i] == key[j]: 
                   index = j
                   newLetter = LCLETTERS[index]
                   newLetter = newLetter.replace(ciphertext[i], newLetter)
                   decryptedResult+=newLetter
                   found = True
                   break
               elif ciphertext[i] == key[j].upper():
                    index = j
                    newLetter = UCLETTERS[index]
                    newLetter = newLetter.replace(ciphertext[i], newLetter)
                    decryptedResult+=newLetter
                    found = True
                    break
               else:
                    found = False
            if found == False:
                decryptedResult = decryptedResult + ciphertext[i]
            continue
        print("    The decrypted text is: " + decryptedResult)
        return decryptedResult

def main():

    """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: getKey, changeKey,
    encrypt, decrypt, quit"""
    end = 0
    a = SubstitutionCipher()
    keyChanged = 0
    while end != 1:
        data = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
        if data.lower() == "getkey":
            print("  Current cipher key: " + a.getKey())
        elif data.lower() == "changekey":
            while keyChanged != 1:
                var = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                if isLegalKey(var.lower()):
                    a.setKey(var)
                    print("    New cipher key: " + a.getKey())
                    keyChanged = 1
                elif isLegalKey(var.lower()) == False and var.lower() != "random" and var.lower() != "quit":
                    print("    Illegal key entered. Try again!")
                    continue
                elif var.lower() == "random":
                     a.setKey(makeRandomKey())
                     print("    New cipher Key: " + a.getKey())
                     keyChanged = 1
                elif var.lower() == "quit":
                    keyChanged = 1
                    break
            keyChanged = 0
        elif data.lower() == "encrypt":
            normal = input("  Enter a text to encrypt: ")
            a.encryptText(normal)
        elif data.lower() == "decrypt":
            coded = input("  Enter a text to dycript: ")
            a.decryptText(coded)
        elif data.lower() == "quit":
            print("Thanks for visiting!")
            end = 1
        else:
            print("  Command not recognized. Try again. ")
main()

