import hashlib
my_input = None
while my_input != "exit" :
    my_input = input ("Enter your text:")
    if my_input != "exit":
        my_encode = hashlib.md5(my_input.encode())
        print(my_encode)

