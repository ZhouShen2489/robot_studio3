from math import sin, cos, pi
from pylx16a.lx16a import *
import time

M = MIDPOINT = 120
YA = YAW_ANGLE = 0
TA = THIGH_ANGLE = 8
CA = CALF_ANGLE = 8
SLEEP_TIME = 0.02
INTERVAL_TIME = 0.3


LX16A.initialize("/dev/ttyUSB2")

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

#standing up
so = servo_offset = [M-5, M-13, M+16, M+0, M+16, M-14]
sl = servo_list = [servo1, servo2, servo3, servo4, servo5, servo6]
dt1 = delay_time_1 = 1500
dt2 = delay_time_2 = 3000#robot standing up delay time 1000ms
try:
    for i in range(6):
        if i == 0:
            t = 0
            while True:
                servo_list[i].move(so[i], time=dt1)
                servo_list[i+3].move(so[i+3], time=dt1)
                time.sleep(0.03)
                t += 0.03
                if t > dt1/1000:
                    break
        if i == 1:
            t = 0
            while True:
                servo_list[i].move(so[i], time=dt2)
                servo_list[i+1].move(so[i+1], time=dt2)
                servo_list[i+3].move(so[i+3], time=dt2)
                servo_list[i+4].move(so[i+4], time=dt2)
                time.sleep(0.03)
                t += 0.03
                if t > dt2/1000:
                    break
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

time.sleep(5)
t = 0
so = servo_offset = [M-5, M-13, M+16, M+0, M+16, M-14]
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
    servo3.move(cos(t) * CA + M + 16)
    servo4.move(cos(t) * YA + M)
    servo5.move(sin(t) * TA + M + 16)
    servo6.move(cos(t) * CA + M - 14)

    time.sleep(SLEEP_TIME)
    t += INTERVAL_TIME
    if t > 500 * INTERVAL_TIME:
        break