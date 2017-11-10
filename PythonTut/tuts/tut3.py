'''
Created on Oct 17, 2017

@author: aleksandar.novic
'''

# sample_string = "This is very shitty string"
# 
# # A - Z 65 - 90
# # a - z 97 122
# 
# print("A =", ord("A"))
# print("65 =", chr(65))


sample_str = input("Enter a string to hide in uppercase: ").upper()

secret_string = ""

for char in sample_str:
    secret_string = secret_string + str(ord(char))
    
print("Secret message: ", secret_string)

sample_str = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
     
    sample_str = sample_str + chr(int(char_code))
    
    
print("Original message: ", sample_str)
# print(secret)
# print(sample_str)












