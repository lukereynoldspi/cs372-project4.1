import socket
import sys
import datetime

def NIST_seconds_since_1900():
    s = socket.socket()
    s.connect(('time.nist.gov', 37))

    time_bytes = s.recv(4096)
    seconds = int.from_bytes(time_bytes, "big")
    s.close()

    return seconds

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

NIST_seconds = NIST_seconds_since_1900()
system_seconds = system_seconds_since_1900()

print("NIST time: "+ str(NIST_seconds))
print("System time: " + str(system_seconds))