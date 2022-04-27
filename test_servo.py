from math import sin, cos, pi
from pylx16a.lx16a import *
import time

M = MIDPOINT = 120
YA = YAW_ANGLE = 0
TA = THIGH_ANGLE = 8
CA = CALF_ANGLE = 8
SLEEP_TIME = 0.01
INTERVAL_TIME = 0.1


LX16A.initialize("/dev/ttyUSB1")

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
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
so = servo_offset = [-5, -13, 16, 0, 16, -14]
while True:
    """
    #servo1: - left, + right
    #servo2: - down, + up
    #servo3: - up, + down
    #servo4: - right, + left
    #servo5: - up, + down
    #servo6: - down, + up
    """
    servo1.move(sin(t) * YA + M - 5)
    servo2.move(sin(t) * TA + M - 13)
    servo3.move(cos(t + pi/2) * CA + M + 16)
    servo4.move(cos(t) * YA + M)
    servo5.move(sin(t) * TA + M + 16)
    servo6.move(cos(t + pi/2) * CA + M - 14)

    time.sleep(SLEEP_TIME)
    t += INTERVAL_TIME
    if t > 500 * INTERVAL_TIME:
        break