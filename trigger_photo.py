"""
Sven Nelson
4/9/2018
RootBot Farmware to send and recieve serial to/from 2nd raspberry pi
"""
# Need this for sending serial data
#import serial as s # Looks like FarmBot has removed serial again??? Switch to print statements 10/7/2019
#from time import sleep # Does not appear nececssary anymore

# Open serial connection with second raspberry pi
#ser = s.Serial("/dev/ttyAMA0", 115200, timeout=10) # Open port (was ttyS0), gave it a 10 sec timeout if not enough bytes read.

# Send "ON" signal to initiate photo taking process
#ser.write("RootCamONRootCamON".encode())
print("RootCamONRootCamON") # Print statement instead of serial call, since FarmBot appears to have removed pyserial again...

# Check to see if the CameraPi has sent "OFF" to confirm photography complete
#data = ser.read(8) # read up to 32 bytes (set to 8 bytes) 

#complete = False 
#while not complete:
#    if data is not None and "OFF" in data:
#      complete = True
#    else:
#      data = ser.read(ser.inWaiting())
