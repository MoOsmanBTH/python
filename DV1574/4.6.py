import hashlib

create_file = open("createdfile.txt", "w+")
create_file.write("This message will be hashed with sha1()")
create_file.close()

read_binary = open("createdfile.txt", "rb")
binary_signature = hashlib.sha1(read_binary.read())
print(binary_signature.hexdigest())