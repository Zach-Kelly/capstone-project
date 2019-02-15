"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Nicholas Snow.
  Winter term, 2018-2019.
"""
import rosebot as bot
import mqtt_remote_method_calls as com
import time
import m1_personal_delegate




def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """

    robot = bot.RoseBot()
    delegate=m1_personal_delegate.ROBOT_DelegateThatReceives(robot)
    mqtt_reciever=com.MqttClient(delegate)
    mqtt_reciever.connect_to_pc()
    time.sleep(0.05)
    mqtt_reciever.send_message('status',["Online!"])
    while True:
        time.sleep(0.01)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<5:
            robot.sound_system.speech_maker.speak("I'm Going to Crash")
            print("I'm Going to Crash","Crashing!")
            mqtt_reciever.send_message('status',["I'm Going to Crash"])

        if delegate.is_done()==1:
            print('Path Sucessful')
            mqtt_reciever.send_message('status', ["Path Sucessful"])



        if delegate.is_Quit()==1:
            print("Quit Sucessful")
            mqtt_reciever.send_message('status', ["Quit Sucessful"])
            break;

        if delegate.is_Exit()==1:
            print("Exit Sucessful")
            mqtt_reciever.send_message('status', ['Exit Sucessful'])
            break;
    print("Program Has Ended")
    mqtt_reciever.send_message('status', ["Program Has Ended"])

    robot.arm_and_claw.calibrate_arm()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.sound_system.speech_maker.speak("I DID IT!")



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()