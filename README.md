This is a python2.7 script that uses the twofish Python Package that can be
be gotten from here https://pypi.python.org/pypi/twofish. This script takes
passwords that are any length and encrypts them with twofish and can also
decrypt them.

To use pass in args of (str method, str password, str key).

method = "en":
	encrypting method that takes the password to be encrypt and the key
	to encrypt with returns the encrypted form of the password.

method = "de":
	takes in the encrypted form of the password and the key to
	decrypt the password with. returns the decrypted form of the password.


EX:
	encrypt: python twofish_Enc_Dec.py en YELLOWSUBMARINES layDqf8KPkpUBR6CFePf5Jqt3Z6pYtcR
		output: 32fd4b007ea323e2416b057f1105cbeb8e32c8ec81d270cdf8848c3b2424072f5bc632e623d5e93330273b95a58902f1d66ddd
	
	decrypt: python twofish_Enc_Dec.py de 32fd4b007ea323e2416b057f1105cbeb8e32c8ec81d270cdf8848c3b2424072f5bc632e623d5e93330273b95a58902f1d66ddd layDqf8KPkpUBR6CFePf5Jqt3Z6pYtcR
		output: YELLOWSUBMARINES
