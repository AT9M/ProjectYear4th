import serial

send_data=""
arduino = serial.Serial('COM1', 9600, timeout=.1)
def Serial_reading_():
    while(True):
        
        string_answer_from_serial = arduino.read(10)
        if 'O' in string_answer_from_serial:
            print("Detection")
            send_data= "O"
            sensor_id=[pos for pos, char in enumerate(string_answer_from_serial) if char == send_data]
            print("Id  of the sensor who have a detection",sensor_id)
           
        else:
            print("No Detection")
            send_data= "N"

        