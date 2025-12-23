


# IMPORTS
import robot

# MAIN
def main():
    start()
    park()


# UTILITY
def start():
    robot.WER_InitRobot(1,-1,2,1,1)
    robot.WER_SetMotor_T(30,30,1)
def setup():
    robot.WER_InitRobot(1,-1,2,1,1)
    robot.WER_Set_GrayscaleSensor()
def sideways():
    robot.WER_SetMotor_T(-30,-30,1)
    robot.WER_SetMotor_E(30,-30, 2, 2200)
    robot.WER_SetMotor_T(30,30,2)
    robot.WER_SetMotor_E(-30,30, 1, 2200)
    robot.WER_SetMotor_T(30,30,2.1)
    robot.WER_SetMotor_E(-30,30, 1, 2200)
    robot.WER_SetMotor_T(30,30,2.3)
"""def run_code(code):
    pos = ''
    if code[2] == '0':
        pos = code[:3]
    else:
        pos = code[:2]
    task = ''
    if len(pos) == 3:
        task = code[3:]
    else:
        task = code[2:]
    exec(pos+'('+task+')')"""
    

# TASKS
def t1():
    robot.set_motor(3, -30)
    robot.sleep(1.2)
    robot.set_motor(3, 0)
def t2():
    robot.set_motor(3, 30)
    robot.sleep(1)
    robot.set_motor(3,10)
    robot.WER_SetMotor_T(-30, -30, 0.5)
    robot.set_motor(3, 0)
    robot.WER_SetMotor_T(-10, -10, 0.3)
def t3():
    robot.set_motor(3, 60)
    robot.sleep(1.5)
    robot.set_motor(3, 0)
def t4a():
    robot.set_motor(3, 10)
    while robot.get_encoder(3) < 1100:
        pass
    robot.set_motor(3,0)
    robot.set_motor(4,-30)
    robot.sleep(1)
    robot.set_motor(4,0)
def t4b():
    robot.set_motor(3,-10)
    while robot.get_encoder(3) > -1100:
        pass
    robot.set_motor(3,0)
def t5():
    robot.set_motor(3,20)
    robot.sleep(1)
    robot.set_motor(3,0)
def t6():
    pass
def t7():
    pass

# POSITIONS
def p1(task=None):
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_Around(-30,30,0)
    robot.WER_LineWay_C(40,1,0.3)
    robot.WER_Around(-30, 30,0)
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30, -30, 0)
    robot.WER_AdvancedWay_T(30,3)
    if task != None:
        task()
        r1()
def p2(task=None):
    robot.WER_LineWay_C(60,5,0.2)
    robot.WER_Around(50,-50,0)
    robot.WER_LineWay_C(60,15,0.2)
    robot.WER_Around(-50,50,0)
    robot.WER_LineWay_C(60,1,0.3)
    robot.WER_AdvancedWay_T(30,1.2)
    if task != None:
        task()
        r2()
def p3(task=None):
    robot.WER_LineWay_C(60,5,0.3)
    robot.WER_Around(60, -60,0)
    #robot.WER_LineWay_C(60,5,0.15)
    for _ in range(8):
        #robot.WER_SetMotor_K(60,60)
        robot.WER_AdvancedWay_T(60,0.1)
    while robot.get_channel_gray(1,5) < 2000:
        robot.WER_SetMotor_K(40,40)
    robot.sleep(0.4)
    robot.WER_SetMotor_K(0,0)
    #beep(500,0.5)
    robot.WER_Around(-60, 60,0)
    robot.WER_LineWay_C(60,1,0.1)
    #beep()
    """while(robot.get_channel_gray(1, 5) < 2000):
        robot.WER_SetMotor_K(-60,60)
    robot.WER_SetMotor_K(0,0)
    while(robot.get_channel_gray(1, 3) < 2000):
        robot.WER_SetMotor_K(-60,60)
    robot.WER_SetMotor_K(0,0)"""
    robot.WER_Around(-60,60,1)
    while(robot.get_channel_gray(1, 5) < 2000):
        robot.WER_SetMotor_K(-60,-60)
    robot.sleep(0.3)
    robot.WER_SetMotor_K(0,0)
    while(robot.get_channel_gray(1, 5) < 2000):
        robot.WER_SetMotor_K(-60,-60)
    robot.WER_SetMotor_K(0,0)
    robot.WER_SetMotor_T(60, 60, 0.2)
    robot.WER_Around(60, -60, 0)
    robot.WER_AdvancedWay_T(30,2)
    if task != None:
        task()
        r3()
def p4(task=None):
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_Around(-30,30,0)
    robot.WER_LineWay_C(40,1,0.3)
    while(robot.get_channel_gray(1, 5) < 1000):
        robot.WER_SetMotor_K(-35,35)
    robot.WER_SetMotor_K(0,0)
    while(robot.get_channel_gray(1, 3) < 1000):
        robot.WER_SetMotor_K(-35,35)
    robot.WER_SetMotor_K(0,0)
    while(robot.get_channel_gray(1, 5) < 1000):
        robot.WER_SetMotor_K(-35,-35)
    robot.sleep(0.3)
    robot.WER_SetMotor_K(0,0)
    while(robot.get_channel_gray(1, 5) < 1000):
        robot.WER_SetMotor_K(-35,-35)
    robot.sleep(0.3)
    robot.WER_SetMotor_K(0,0)
    while(robot.get_channel_gray(1, 5) < 1000):
        robot.WER_SetMotor_K(-35,-37)
    robot.WER_SetMotor_K(0,0)
    robot.WER_SetMotor_T(40, 40, 0.3)
    robot.WER_Around(30, -30, 0)
    robot.WER_AdvancedWay_T(30,1.7)
    if task != None:
        task()
        r4()
def p5(task=None):
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_SetMotor_T(40, 40, 0.3)
    while(robot.get_channel_gray(1, 5) < 2000):
        robot.WER_SetMotor_K(60,60)
    robot.sleep(0.3)
    robot.WER_SetMotor_K(0,0)
    robot.WER_Around(-30, 30, 0)
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_AdvancedWay_T(30, 2.2)
    
    if task != None:
        task()
        r5()
"""def p6():
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_SetMotor_T(40, 40, 0.3)
    while(robot.get_channel_gray(1, 5) < 2000):
        robot.WER_SetMotor_K(35,35)
    robot.sleep(0.4)
    robot.WER_SetMotor_K(0,0)
    #robot.WER_Around(30, -30, 0)
    while robot.get_channel_gray(1,3) < 2000:
        robot.WER_SetMotor_K(30,-40)
    robot.WER_SetMotor_K(0,0)
    robot.beep(500,1)
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(-30,30,0)
    robot.WER_AdvancedWay_T(30, 2.2)
    if task != None:
        task()
        r6()"""
def p6(task=None):
    robot.WER_LineWay_C(60,5,0.2)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(60,15,0.2)
    robot.WER_Around(30, -30,0)
    robot.WER_LineWay_C(60,1,0.05)
    robot.WER_Around(-30, 30, 0)
    robot.WER_LineWay_C(60,5,0.2)
    robot.WER_SetMotor_T(30,30,0.2)
    robot.WER_LineWay_C(60,5,0.3)
    robot.WER_SetMotor_T(30,30,2.2)
    #robot.WER_Around(30, -30, 1)
    #robot.WER_AdvancedWay_T(30, 1.2)
    if task != None:
        task()
        r6()
def p7(task=None):
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_SetMotor_T(40, 40, 0.3)
    while(robot.get_channel_gray(1, 5) < 2000):
        robot.WER_SetMotor_K(60,60)
    robot.sleep(0.3)
    robot.WER_SetMotor_K(0,0)
    #robot.WER_Around(30, -30, 0)
    while robot.get_channel_gray(1,3) < 3000:
        robot.WER_SetMotor_K(40,-40)
    robot.WER_AdvancedWay_T(40,1.8)
    if task != None:
        task()
        r7()
def p8(task=None):
    robot.WER_LineWay_C(60,5,0.2)
    robot.WER_Around(50,-50,0)
    robot.WER_LineWay_C(60,15,0.2)
    #robot.WER_Around(50, -50,0)
    #robot.WER_LineWay_C(60,1,0.05)
    #robot.WER_Around(-50, 50, 0)
    #robot.WER_LineWay_C(60,5,0.2)
    #robot.WER_Around(50, -50, 1)
    #robot.WER_AdvancedWay_T(30, 1.2)
    x = robot.get_encoder(1)
    print(x)
    while robot.get_encoder(1) > x-5200:
        robot.WER_SetMotor_K(60,60)
        print(robot.get_encoder(1))
    robot.WER_SetMotor_K(0,0)
    robot.WER_Around(60,0,0)
    robot.WER_Around(60,0,0)
    robot.WER_AdvancedWay_T(30, 1.2)
    
    if task != None:
        task()
        r8()
def p9(task=None):
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_Around(30, -30,0)
    robot.WER_LineWay_C(30,1,0.3)
    robot.WER_AdvancedWay_T(20, 1.8)
    if task != None:
        task()
        r9()
def p10(task=None):
    robot.WER_LineWay_C(40,5,0.3)
    robot.WER_Around(30,-30,0)
    robot.WER_LineWay_C(40,15,0.3)
    robot.WER_Around(-30,30,0)
    robot.WER_LineWay_C(40,1,0.3)
    robot.WER_Around(-30, 30, 0)
    robot.WER_LineWay_C(40, 5, 0.3)
    robot.WER_AdvancedWay_T(30,1.2)
    if task != None:
        task()
        r10()

# RETURNS
def r1():
    robot.WER_SetMotor_T(-50, -60, 2.2)
def r2():
    while(robot.get_channel_gray(1, 1) < 2000):
        robot.WER_SetMotor_K(-60,-60)
    robot.sleep(0.2)
    while(robot.get_channel_gray(1, 1) < 2000):
        robot.WER_SetMotor_K(-60,-60)
    robot.WER_SetMotor_K(60, 60)
    robot.sleep(0.2)
    robot.WER_SetMotor_K(0,0)
    robot.WER_Around(-60, 60, 0)
    robot.WER_LineWay_C(60, 1, 0.2)
    robot.WER_Around(-60, 60, 0)
    robot.WER_LineWay_C(60, 15, 0.3)
def r3():
    while robot.get_channel_gray(1, 5) < 2000:
        robot.WER_SetMotor_K(-60, -60)
    robot.WER_SetMotor_T(-60, -60, 0.3)
    while robot.get_channel_gray(1, 5) < 2000:
        robot.WER_SetMotor_K(-60, -60)
    robot.WER_SetMotor_T(60,60,0.3)
    robot.WER_Around(-60, 60, 0)
    robot.WER_LineWay_C(60,15,0)
    robot.WER_SetMotor_T(60, 60, 0.3)
    while robot.get_channel_gray(1, 1) < 2000:
        robot.WER_SetMotor_K(60, 60)
    robot.WER_SetMotor_K(0,0)
    robot.WER_SetMotor_T(-60, 60, 0.4)
    robot.WER_SetMotor_T(60, 60, 0.3)
def r4():
    while robot.get_channel_gray(1, 1) < 2000:
        robot.WER_SetMotor_K(-30, -30)
    robot.WER_SetMotor_T(-30, -30, 0.3)
    while robot.get_channel_gray(1, 5) < 2000:
        robot.WER_SetMotor_K(-30, -30)
    robot.WER_SetMotor_T(30,30,0.3)
    robot.WER_Around(-30, 30, 0)
    robot.WER_LineWay_C(40,15,0)
    robot.WER_SetMotor_T(30, 30, 0.3)
    while robot.get_channel_gray(1, 1) < 2000:
        robot.WER_SetMotor_K(30, 30)
    robot.WER_SetMotor_K(0,0)
    robot.WER_SetMotor_T(-30, 30, 0.5)
    robot.WER_SetMotor_T(30, 30, 0.3)
def r5():
    robot.WER_SetMotor_T(-54,-50,5.5)
def r6():
    while robot.get_channel_gray(1,1) < 2000:
        robot.WER_SetMotor_K(-50,-50)
    while robot.get_channel_gray(1,1) >= 2000:
        robot.WER_SetMotor_K(-50,50)
    while robot.get_channel_gray(1,1) < 2000:
        robot.WER_SetMotor_K(-50,50)
    while robot.get_channel_gray(1,3) < 2000:
        robot.WER_SetMotor_K(-50,50)
    #robot.WER_LineWay_C(60,1,0)
    robot.WER_LineWay_C(60,15,0.3)
    while robot.get_channel_gray(1,1) < 2000:
        robot.WER_SetMotor_K(60,60)
    robot.sleep(0.2)
    robot.WER_SetMotor_T(-50,50,0.5)
    robot.WER_SetMotor_T(50,50,0.3)
def r7():
    #robot.WER_SetMotor_T(-50,-37,4.0)
    #robot.WER_SetMotor_T(-40,-40,1.5)
    while robot.get_channel_gray(1,1) < 2000:
        robot.WER_SetMotor_K(-40, -40)
    robot.WER_SetMotor_T(40,40,0.3)
    robot.WER_Around(40,-40,0)
    robot.WER_LineWay_C(50, 15,0.3)
    while robot.get_channel_gray(1,3) < 2000:
        robot.WER_SetMotor_K(40,40)
    robot.sleep(0.3)
    robot.WER_SetMotor_K(0,0)
    robot.WER_Around(-30,30,0)
    robot.WER_SetMotor_T(30,30,0.5)
def r8():
    robot.WER_SetMotor_T(-90,-60,4)
def r9():
    while robot.get_channel_gray(1, 1) < 2000:
        robot.WER_SetMotor_K(-30, -30)
    robot.WER_SetMotor_T(30, -30, 0.5)
    robot.WER_SetMotor_T(30, 28, 3)
def r10():
    while robot.get_channel_gray(1,5) < 2000:
        robot.WER_SetMotor_K(-30, -30)
    robot.WER_SetMotor_T(-30, 30, 0.3)
    robot.WER_SetMotor_T(30, 30, 3)

def park():
    robot.WER_SetMotor_T(30, -30, 0.5)
    robot. WER_SetMotor_T(100, 100, 2.7)

# START
main()#program entry