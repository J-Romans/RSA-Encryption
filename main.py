import Keys

class Client():
    def __init__(self):
        self.__private, self.public = Keys.createKeys()
        self.e = self.public[0]
        self.n = self.public[1]
        self.phi_n = (self.__private[0]-1)*(self.__private[1]-1)
        self.f = self.__findF()

        self.byte_order = "big"
        self.byte_length = 4 
        #For Current settings, 4 is good. If there is a change in the max index in Keys.py:
        #Run: int(log(sympy.nextprime(Max Index)**2,2**8))+1

    def __findF(self):
        for f in range(3,self.phi_n):
            if (f*self.e) % self.phi_n == 1:
                return f
        return None
    
    def __Vampire(self,int_list): #Byte-ify
        print(int_list)
        return [char.to_bytes(self.byte_length,byteorder = self.byte_order) for char in int_list]

    def __Garlic(self,byte_list): #unByte-ify
        return [int.from_bytes(char, byteorder=self.byte_order) for char in byte_list]

    def getPublicKey(self):
        return self.public

    def encrypt(self,message,public_key):
        encoded_message = [ord(c) for c in message] #Encode using Unicode
        encrypted_message = [pow(char,public_key[0],public_key[1]) for char in encoded_message]
        
        return self.__Vampire(encrypted_message)
    
    def decrypt(self, encrypted_message):        
        encoded_message = [pow(char,self.f,self.n) for char in self.__Garlic(encrypted_message)]
        message = "".join([chr(char) for char in encoded_message])
        return message
    
'''
client1 = Client()
client2 = Client()

public2 = client2.getPublicKey()
x = client1.encrypt("Hello World!", public2)
print(x)
print(client2.decrypt(x))
'''