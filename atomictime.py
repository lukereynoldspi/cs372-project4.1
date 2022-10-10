import socket
import sys

s = socket.socket()
s.connect(('time.nist.gov', 37))

time_bytes = s.recv(4096)
seconds = int.from_bytes(time_bytes, "big")

print(seconds)