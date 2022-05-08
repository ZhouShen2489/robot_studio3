from math import sin, cos, pi
from pylx16a.lx16a import *
import time

"""
walking best parameters:
YA = YAW_ANGLE = 0
TA = THIGH_ANGLE = 8
CA = CALF_ANGLE = 13
SLEEP_TIME = 0.005
INTERVAL_TIME = 0.08

so = servo_offset = [M-5, M+25, M+65, M+0, M+38, M-19]

servo1.move(sin(t) * YA + so[0])
servo2.move(sin(t) * TA + so[1])
servo3.move(sin(t + pi/2) * CA + so[2])
servo4.move(cos(t) * YA + so[3])
servo5.move(sin(t + pi) * TA + so[4])
servo6.move(sin(t + pi + pi/2) * CA + so[5])
"""


M = MIDPOINT = 120
YA = YAW_ANGLE = 0
TA = THIGH_ANGLE = 8
CA = CALF_ANGLE = 13
SLEEP_TIME = 0.005
INTERVAL_TIME = 0.08

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

#standing up
#[-5, 20, 72, 0, 25, -10]
    """
    #servo1: - left, + right
    #servo2: - up, + down
    #servo3: - down, + up
    #servo4: - right, + left
    #servo5: - up, + down
    #servo6: - down, + up
    """
so = servo_offset = [M-5, M+25, M+65, M+0, M+38, M-19]
sn = servo_normal_position = [so[0], so[1]-7, so[2]+8, so[3], so[4]-7, so[5]+8]
sl = servo_list = [servo1, servo2, servo3, servo4, servo5, servo6]
dt1 = delay_time_1 = 1000
dt2 = delay_time_2 = 800#robot standing up delay time 1000ms
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
while True:
    servo1.move(sin(t) * YA + so[0])
    servo2.move(sin(t) * TA + so[1])
    servo3.move(sin(t + pi/2) * CA + so[2])
    servo4.move(cos(t) * YA + so[3])
    servo5.move(sin(t + pi) * TA + so[4])
    servo6.move(sin(t + pi + pi/2) * CA + so[5])

    time.sleep(SLEEP_TIME)
    t += INTERVAL_TIME
    if t > 2000 * INTERVAL_TIME:
        break

#rest mode
dt1 = delay_time_1 = 1000
dt2 = delay_time_2 = 800#robot standing up delay time 1000ms
try:
    for i in range(6):
        if i == 0:
            t = 0
            while True:
                servo_list[i].move(sn[i], time=dt1)
                servo_list[i+3].move(sn[i+3], time=dt1)
                time.sleep(0.03)
                t += 0.03
                if t > dt1/1000:
                    break
        if i == 1:
            t = 0
            while True:
                servo_list[i].move(sn[i], time=dt2)
                servo_list[i+1].move(sn[i+1], time=dt2)
                servo_list[i+3].move(sn[i+3], time=dt2)
                servo_list[i+4].move(sn[i+4], time=dt2)
                time.sleep(0.03)
                t += 0.03
                if t > dt2/1000:
                    break
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()