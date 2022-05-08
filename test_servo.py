from math import sin, cos, pi
from pylx16a.lx16a import *
import time

M = MIDPOINT = 120
YA = YAW_ANGLE = 0
TA = THIGH_ANGLE = 0
CA = CALF_ANGLE = 0
SLEEP_TIME = 0.01
INTERVAL_TIME = 0.1


LX16A.initialize("/dev/ttyUSB0")

try:
    servo1 = LX16A(1)
    servo2 = LX16A(7)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(8)
    servo6 = LX16A(6)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
so = servo_offset = [-5, 25, 65, 0, 38, -19]
while True:
    """
    #servo1: - left, + right
    #servo2: - up, + down
    #servo3: - down, + up
    #servo4: - right, + left
    #servo5: - up, + down
    #servo6: - down, + up
    """
    servo1.move(sin(t) * YA + M + so[0])
    servo2.move(sin(t) * TA + M + so[1])
    servo3.move(cos(t + pi/2) * CA + M + so[2])
    servo4.move(cos(t) * YA + M + so[3])
    servo5.move(sin(t) * TA + M + so[4])
    servo6.move(cos(t + pi/2) * CA + M + so[5])

    time.sleep(SLEEP_TIME)
    t += INTERVAL_TIME
    if t > 100 * INTERVAL_TIME:
        break
