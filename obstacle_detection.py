import serial

def read_distance(serial_port='/dev/ttyUSB0'):
    try:
        ser = serial.Serial(serial_port, 9600, timeout=1)
        if ser.in_waiting > 0:
            distance = ser.readline().decode('utf-8').strip()
            print(f"Distance: {distance} cm")
            return float(distance)
    except Exception as e:
        print(f"Serial error: {e}")
    return None