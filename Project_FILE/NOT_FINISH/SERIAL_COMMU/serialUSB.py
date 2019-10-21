import serial

send_data=""
arduino = serial.Serial('COM1', 9600, timeout=.1)
def Serial_reading_():
    while(True):
        
        string_answer_from_serial = arduino.readline()
        if 'O' in string_answer_from_serial:
            print("Detection")
            send_data= "O"
        else:
            print("No Detection")
            send_data= "N"
