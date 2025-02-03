from sensors.imu import SimulatedIMU, ArduinoIMU
# Baudrate = 115520 ?
from sensors.servo import Servo
import time
import sys

if __name__ == "__main__":
    # Parse arguments
    iterations = int(sys.argv[1])

    # Setup
    imu = SimulatedIMU("data/sample_data.csv")
    yaw_servo = Servo("yaw")
    pitch_servo = Servo("pitch")

    # Track total elapsed time and loop count
    elapsed_time = 0
    iteration_count = 0
    abs_error = 0
    
    while iteration_count < iterations:
        # Read from sensor
        # print(f'{iterations}\n')

        # Measure how long the update took to run
        start = time.time()
        imu.update()
        end = time.time()
        elapsed_time += end-start

        # pitch, roll, yaw
        angles = imu.get_angles()
        yaw_angle = angles[2]
        pitch_angle = angles[0]
        if type(imu) is SimulatedIMU:
            abs_error = imu.get_abs_error()

       #  How long does it take to process data and remove noise?
        # How well does it remove noise?

        # Send command
        yaw_servo.write(yaw_angle)
        pitch_servo.write(pitch_angle)

        print(f'Time for update: {end-start}')
        print(f'Angles: {angles}')
        print(f'Total elapsed time: {elapsed_time}')
        if type(imu) is SimulatedIMU:
            print(f'Running absolute error: {abs_error}\n')

        iteration_count += 1

    # Output MAE at the end 
    if type(imu) is SimulatedIMU:
        mae = abs_error/iterations
        print(f'Mean absolute error: {mae}')
