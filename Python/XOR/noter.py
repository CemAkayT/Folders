#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

#binary
b = bin(32)
print(b) # med binary prefix
print(b[2:]) # uden binary prefix
print(int(b[2:],2))

print('==================')

#hexadecimal
h = '0x7f'
print(h) # med hex prefix
print(h[2:]) # uden hex prefix
print(int(h,16))

print('================')

string1 = "sami"
string2 = "esila"

# Convert each character in the strings to ASCII values
ascii_values1 = [ord(char) for char in string1]
ascii_values2 = [ord(char) for char in string2]
print(ascii_values1)
print(ascii_values2)

print('================')

print(ord('a'))
print(chr(97))

print('================')
# Convert each ascii value to their respective characters

xorresult = [22,18,4,5,65]
charvalue = [chr(val) for val in xorresult]
print(charvalue)

print('=================🥰')
print(f'XOR 10 and 6: ', 10 ^ 6)




