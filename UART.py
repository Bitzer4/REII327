import time
import serial
import io

print ("Starting program")

ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_55639313333351D03120-if00', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )

counter = 0;
while 1:
    
    if counter == 0:
        sss = "1"
    if counter == 1:
        sss = "2"

    counter = counter + 1;
    if counter == 2:
        counter = 0;

    print ("Write")
    ser.write(sss.encode())
    

    time.sleep(1)

    if ser.inWaiting() > 0:
        line = ser.readline()
        lineS = line.decode("utf-8")
        print(line)
        print(lineS[0])
        
        if lineS[0] == 'T':
            print (lineS[1:len(lineS)-2])

        if lineS[0] == 'C':
            print (lineS[1:len(lineS)-2])
