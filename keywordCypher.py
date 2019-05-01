from CodeWarrior.Standard_Suite import character


class KeywordCypher:


    def __init__(self):
        secretKey = "KRYPTOS"
    
        self.plainTextAlphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
       #encryptedAlphabet =      ['K','R','Y','P','T','O','S','A','B','C','D','E','F','G','H','I','J','L','M','N','Q','T','U','V','W','X']
        self.encryptedAlphabet = []
        
        plainTextAlphabetIndexNumber = 0
        for firstCharacter in self.plainTextAlphabet:
            if firstCharacter not in self.encryptedAlphabet:
                try:
                    #secretKey[plainTextAlphabetIndexNumber]
                    self.encryptedAlphabet.append(secretKey[plainTextAlphabetIndexNumber])
                except IndexError:
                    for secondIterationCharacter in self.plainTextAlphabet:
                        if secondIterationCharacter not in self.encryptedAlphabet:
                            self.encryptedAlphabet.append(secondIterationCharacter)
                            break
                            
            else:       #character in plainTextAlphabet is currently present in encryptedAlphabet
                for thirdIterationCharacter in self.plainTextAlphabet:
                        if thirdIterationCharacter not in self.encryptedAlphabet:
                            self.encryptedAlphabet.append(thirdIterationCharacter)
                            break
                            
            plainTextAlphabetIndexNumber += 1
            
        user_input = raw_input("Enter a message you want to send to your frined and we will encrypt it for you :) ").upper()
        encryptedMessage = self.encrypt(user_input)
    
        print "Your Encrypted Message is: " + encryptedMessage    
        
        #print encryptedAlphabet
    
    
    """
    to encrypt the input of a plaintext
    """
    def encrypt(self, input):
        encryptedInput = ''
        for char in input:
            if char == ' ' :
                encryptedInput += ' '
            else:
                plainTextAlphabetIndexNumber = self.plainTextAlphabet.index(char.upper())
                
                encryptedInput += self.encryptedAlphabet[plainTextAlphabetIndexNumber]
                
        return encryptedInput
        
        
        
    """
    to decrypt the input of an encrypted string
    @param input: string
    """
    def decrypt(self, input):
        decryptedInput = ''
        for char in input:
            if char == ' ' :
                decryptedInput += ' '
            else:
                encryptedAlphabetIndexNumber = self.encryptedAlphabet.index(char.upper())
                
                decryptedInput += self.plainTextAlphabet[encryptedAlphabetIndexNumber]
                
        return decryptedInput
    
    
    
    
    
    
    
keywordCypherTest = KeywordCypher()
encryptedMessage = keywordCypherTest.encrypt('Hi I like cats')
print "Your Encrypted Message would be :" + encryptedMessage
print "Your Decrypted Message would be :" + keywordCypherTest.decrypt(encryptedMessage)
    