import zlib
t="x\x9c\x0b(\xcd\xcb,\xc9HT\xc8,VHTH/JM,Q(N\xceL\xcd+\xc9,.\x01\x00\x94U\n\x80"
d=zlib.decompress(t.decode("utf-8"))
print(d)
