# Python program to find SHA256 hexadecimal hash string of a file
import hashlib

def hash(filename):
    return hashlib.sha256(open(filename, 'rb').read()).hexdigest()

       