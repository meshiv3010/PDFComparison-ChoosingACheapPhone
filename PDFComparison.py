import hashlib

def hash_file(fileName1, fileName2):

	h1 = hashlib.sha1()
	h2 = hashlib.sha1()

	with open(fileName1, "rb") as file:

		value = 0
		while value != b'':
			value = file.read(1024)
			h1.update(value)

	with open(fileName2, "rb") as file:
		value = 0
		while value != b'':
			value = file.read(1024)
			h2.update(value)

	return h1.hexdigest(), h2.hexdigest()


msg1, msg2 = hash_file("PDF1.pdf", "PDF2.pdf")

if(msg1 != msg2):
	print("False")
else:
	print("True")
