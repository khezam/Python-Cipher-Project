# Secret Messages

## Project Overview
Most of us have, at one time or another, wanted to pass messages to our friends that other people couldn't read. Maybe it was a note in class, a midnight rendezvous, or something more serious like invasion plans. Whatever the purpose, you'd want your message to be encoded so only the people you want to can read it. That's where ciphers come in!

Ciphers are repeatable ways to encode a message. One of the most famous is the Caesar Cipher, used by Julius Caesar for his private communications. He would take each letter of the message and change it to the letter that was three characters further on in the Roman alphabet. For example, if I was going to encode the word "dog", using the American English alphabet, I would change the "d" to "g", which is three letters further on. The "o" would become "r", and the "g" turns into "j". Instead of sending "dog" to my friend, I'd send "grj". To figure it out, my friend would move each letter back three characters.

One thing Julius Caesar didn't have, though, is a computer to do all of this encoding and decoding for him!

Your job is to take a few of the famous ciphers listed here and implement them in Python so you can quickly encode and decode secret messages. Each cipher should be created as a Python class and each has to expose two methods: encrypt and decrypt. Each of these methods should take a single string to be encoded or decoded and should return the properly encoded or decoded version of the string according to the cipher.

## Instructions
1- Choose one or more basic ciphers from the following list to implement encrypting and decrypting abilities.

  -Alberti cipher
  
  -Affine cipher
  
  -Atbash cipher
  
  -Polybius square cipher
  
  -Transposition cipher
  
  -ADFGVX cipher
  
  -Bifid cipher
  
  -Keyword cipher
  
  -Hill cipher

2- Provide a command line menu providing an option to either encrypt or decrypt a value and then a sub menu with a list of implemented ciphers.

3- Prompt the user for input to encrypt or decrypt and, if applicable, any additional input settings required to perform the cipher process.

4- The input value is correctly encrypted or decrypted using the chosen cipher and the output is displayed on the screen.

6- Remember to include informative docstrings in your functions and/or methods.
