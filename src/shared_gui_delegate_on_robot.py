"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Nicholas Snow, Katana Colledge, and Zach Kelly.
  Winter term, 2018-2019.
"""

import rosebot as bot
import mqtt_remote_method_calls as com
import time
import math


class DelegateThatReceives(object):

    def __init__(self, robot):
        self.robot = bot.RoseBot()
        self.Quit=0

    def is_exit(self):
        self.stop()
        self.down()
        return self.Quit

    ##DRIVE SYSTEM
    #Handle Quit and Exit
    def command(self,argument):
        print("Command Recieved: ",argument)
        if argument == "quit":
            print("Quit")
            self.Quit = 1

        if argument == 'exit':
            print("Exit")
            pass

    def stop(self):
        print("Command Recieved: Stop")
        self.robot.drive_system.stop()


    #Handle Forward and Backward and Left and Right
    def movement(self, left_speed, right_speed):
        print("Command Recieved: Movement",left_speed,right_speed)
        self.robot.drive_system.go(int(left_speed), int(right_speed))

    ##ARM SYSTEM
    def up(self):
        print("Command Recieved: Up")
        self.robot.arm_and_claw.raise_arm()

    def down(self):
        print("Command Recieved: Down")
        self.robot.arm_and_claw.lower_arm()

    def move_to_pos(self,position):
        print("Command Recieved: Move to Position",position)
        integerposition= int(position)
        if integerposition <=10:
            integerposition = 10
        self.robot.arm_and_claw.move_arm_to_position(integerposition)

    def calibrate(self):
        print("Command Recieved: Calibrate Arm")
        self.robot.arm_and_claw.calibrate_arm()


    # IR Sensor

    def ir_forward(self, inches, speed):
        print("Command Received: Go forward until distance is less than")
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)

    def ir_backward(self, inches, speed):
        print("Command Received: Go backward until distance is greater than")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)

    def ir_within_dist(self, inches, speed):
        print("Command Received: Go until distance is within")
        self.robot.drive_system.go_until_distance_is_within(inches, speed)

    ##Sprint 1 SYSTEM

    def Forward_Time(self,speed,time):
        print("Command Recieved: Forward_Time")
        self.robot.drive_system.go_straight_for_seconds(int(time),int(speed))
    def Forward_Time_Inches(self,speed,inches):
        print("Command Recieved: Forward_Time_Inches")
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches),int(speed))
    def Forward_Inches(self,speed,inches):
        print("Command Recieved: Forward_Inches")
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches),int(speed))

    def beep_button(self,numberofbeeps):
        print("Command Recieved: Beep")
        for k in range(int(numberofbeeps)):
            self.robot.sound_system.beeper.beep()
    def tone_button(self,duration,frequency):
        print("Command Recieved: Tone")
        self.robot.sound_system.tone_maker.play_tone(frequency,duration)

    def speak_button(self,text):
        print("Command Recieved: Speak")
        self.robot.sound_system.speech_maker.speak(text)