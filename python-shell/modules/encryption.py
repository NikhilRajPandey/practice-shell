"""
encryption.py - Python Shell

A module created for supplying the required functions to the shell application. The functions and classes defined in this module ease many tasks at the shell application, in general way they are used in executing the task assigned by the user via the commands. This module contains functions and classes related to directory handling and other such stuff.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : June 13, 2021

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : June 13, 2021

Changes made in the last modification :
1. Added the code for serving the functionality of encryption as well as decryption in the class 'StringEncrypter'.

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	from base64 import b64encode, b64decode
	import hashlib
except Exception as e:
	# If there are any errors during the importing of the modules, then we display the error on the console screen

	input(f'\n[ Error : {e} ]\nPress enter key to continue...')
	exit()

class StringEncrypter:
	""" """

	def __init__(self, text = None, password = None):
		# Setting the user entered arguments to this function as the default arguments
		self.text = text
		self.password = password

	def generatekey(self):
		""" This method / function serves the purpose of generating a special key for the encryption and decryption using the user entered password. This function takes the value of the user entered password from the class variable self.password.
		The key is generated in such an algorithm, that the key remains possitive integer.

		This function returns the int format key back after the generation. """

		# Generating the key from the encryption using the user entered password for encryption / decryption
		key = 0
		isEven = True

		for i in self.password:
			# Iterating over each character in the encrypted key entered by the user
				
			if isEven:
				# If the current iteration is even number, then we add the char code value

				key += ord(i)
			else:
				# If the current iteration is odd number (not even), then we subtract the char code value

				key -= ord(i)
		del isEven

		# Making the key possitive
		if key < 0:
			# If the key value is less than 0, then we change the negative sign to possitive by simply multiplying it with -1

			key *= (-1)

		# Adding the length of the password to itself
		key += len(self.password)

		# Returning the generating key
		return key

	def encrypt(self):
		""" This method / function serves the functionality of encrypting the user specified string / text using the user specified password. This function uses the value of text and password stored in the class variables self.text, self.password. """

		# Generating the key for the encryption
		key = self.generatekey()

		# Converting each character in the user entered text to cipher format
		text = ''
		for character in self.text:
			# Iterating through each character

			text += chr((ord(character) + key) % 256)

		# Encoding the cipher text into base64 format
		text = b64encode(text.encode()).decode()

		# Setting the encrypted text as the class variable self.text
		self.text = text
		del key, text
		return self.text

	def decrypt(self):
		""" This method / function serves the functionality of decrypting the user specified string / text using the user specified password. This function uses the value of text and password stored in the class variables self.text, self.password. """

		# Generating the key for the encryption
		key = self.generatekey()

		# Decoding from the base64 format to cipher format
		self.text = b64decode(self.text.encode()).decode()

		# Converting each character from cipher text to plain format
		text = ''
		for character in self.text:
			# Iterating through each character

			text += chr((ord(character) - key) % 256)

		# Setting the decrypted text as the class variable self.text
		self.text = text
		del text, key
		return self.text