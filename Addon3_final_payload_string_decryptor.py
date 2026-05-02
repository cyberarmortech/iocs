def decrypt(enc_buffer):
    s=""
    key = "xnasff3wcedj"
    i=0
    for x in enc_buffer:
        s=s+chr(x^ord(key[i%len(key)]))
        i=i+1
    return s

enc_buffer = b'\x2c\x0b\x0d\x16\x01\x14\x52\x1a\x43\x21\x01\x19\x13\x1a\x0e\x03'
print(decrypt(enc_buffer))