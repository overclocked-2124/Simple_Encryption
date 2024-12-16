import string
import random

print("Choose mode of operation:")
print("Enter 'e' for Encryption and 'd' for decription")
mode=str(input())
mode=mode.lower()

sentance=""
enc_sentance=""
key=""
alpha=string.ascii_lowercase
Enc_Dict={}



if(len(mode)!=1):
    print("Invalid input! , enter only 1 charecter")

if(mode=="e"):
    key=''.join(random.sample(string.ascii_lowercase,k=26))
    
    Enc_Dict={a:b for a,b in zip(alpha,key)}
    
    sentance=str(input("Please input the deisred string to be encrypted here: "))
    sentance=sentance.lower()
    for letter in sentance:
        if letter in alpha:
            enc_sentance+=Enc_Dict[letter]
        else:
            enc_sentance+=letter
    
    print("The encrypted sentance is: "+enc_sentance)
    print("the key for the encrypted sentace is:"+ key)
    
if(mode=="d"):
    enc_sentance=str(input("Enter the encrypted sentence here: "))
    key=str(input("Enter the encription key here: "))
    Enc_Dict={a:b for a,b in zip(key,alpha)}
    
    for letter in enc_sentance:
         if letter in alpha:
            sentance+=Enc_Dict[letter]
         else:
            sentance+=letter
            
    print("The decrypted sentence is: "+sentance)

else:
    print("Invalid input! , selected choice does not exist")