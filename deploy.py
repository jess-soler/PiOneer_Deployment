"""
Name: PiOneer_Deploy.py
Author: Jessica Soler
Created: 1/10/2025
Purpose: Deployment Code for Final NASA Space Grant
"""


# EasyGoPiGo3 documentation: https://gopigo3.readthedocs.io/en/latest
# Copyright (c) 2017 Dexter Industries Released under the MIT license
# History
# ------------------------------------------------
# Author     Date       \t    Comments
# Loring     09/25/21       Convert to EasyGoPiGo3, test with Python 3.5
#
# Table Of Contents
# ------------------------------------------------
# Tkinter GUI Main Frame:
  # Navigation Frame:
    # Start/Stop Autonomous Navigation (obstacle avoidance) Button
    # Start/Stop GUI Navigation Control (screen click) Button
    # Start/Stop Keyboard Navigation Control (arrow keys) Button
    # Start/Stop Hand Navigation Control (hand gestures) Button
    # Start/Stop PS4 Controller Navigation Control (PS4 controller) Button
  # Sensor Frame:
    # Start/Stop Sensor Button
  # Video Frame:
    # Live Video Stream
  # ThingSpeak Frame:  
    # API Stuff
    
      
#TODO: add class for navigation control 
# [autonomous, GUI [opens new window], keyboard [opens new window], hand [opens new window?], PS4]
# can you have more than one type of navigation at once???
#TODO: add class for sensors [?]
#TODO: add class for video stream [?]
#TODO: add class for ThingSpeak [API]
#TODO: move sensor frame underneath navigation frame
#TODO: look into API to get ThingSpeak data in GUI


#TODO : state machine-- change toggle to do flags-- true/false
#TODO: http clickable label URL for thingspeak
#TODO: integrate live video



# LIBRARIES
import tkinter as tk
# import nav_ps4 # run as a thread------- getting stuck!
#import nav_remote
from threading import Thread
from time import sleep
     
#TODO: create deployment class
class PioneerDeploy:
    #TODO: create __init__ method
    def __init__(self, root):
        # toggles, autonomous GUI keyboard hand
        self.is_autonomous = False
        
        # Initialize class with main Tkinter window
        self.main_window = root
        
        # Set the size of the main window
        self.main_window.geometry("1200x1200")
        
        # Set title of main window
        root.title("Mars Rover Deployment: PiOneer")
        
        # Create frames
        self.create_frames()
        
        # Create widgets
        self.create_widgets()
        
#---Create Frames---------------------------------------------------------------#
    def create_frames(self):
        # Create a main frame to hold all the widgets
        self.main_frame = tk.Frame(self.main_window, bd=2, relief=tk.RAISED)
        self.main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Create a frame for the navigation buttons
        self.nav_frame = tk.Frame(self.main_frame, bd=2, relief=tk.RAISED)
        self.nav_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a frame for the sensor buttons
        self.sensor_frame = tk.Frame(self.main_frame, bd=2, relief=tk.RAISED)
        self.sensor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a frame for the video stream
        self.video_frame = tk.Frame(self.main_frame, bd=2, relief=tk.RAISED)
        self.video_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create a frame for the ThingSpeak
        self.thingspeak_frame = tk.Frame(self.main_frame, bd=2, relief=tk.RAISED)
        self.thingspeak_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
#---Create Widgets---------------------------------------------------------------#
    def create_widgets(self):
        # Create the navigation buttons
        self.nav_label = tk.Label(self.nav_frame, text="Navigation", font=("Arial", 16))
        self.nav_label.pack(pady=10)
        
        # Create the start/stop autonomous navigation button
        self.start_stop_auto_nav = tk.Button(self.nav_frame, text="Start Autonomous Navigation", font=("Arial", 12), command=self.toggle_autonomous_navigation)
        self.start_stop_auto_nav.pack(pady=10)
        
        # Create the start/stop GUI navigation control button
        self.start_stop_gui_nav = tk.Button(self.nav_frame, text="Start GUI Navigation Control", font=("Arial", 12), command=self.toggle_gui_navigation)
        self.start_stop_gui_nav.pack(pady=10)
        
        # Create the start/stop Keyboard navigation control button
        self.start_stop_keyboard_nav = tk.Button(self.nav_frame, text="Start Keyboard Navigation Control", font=("Arial", 12), command=self.toggle_keyboard_navigation)
        self.start_stop_keyboard_nav.pack(pady=10)
        
        # create the start/stop Hand navigation control button
        self.start_stop_hand_nav = tk.Button(self.nav_frame, text="Start Hand Navigation Control", font=("Arial", 12), command=self.toggle_hand_navigation)
        self.start_stop_hand_nav.pack(pady=10)
        
        # Create the start/stop PS4 controller navigation control button
        self.start_stop_ps4_nav = tk.Button(self.nav_frame, text="Start PS4 Controller Navigation Control", font=("Arial", 12), command=self.toggle_ps4_navigation)
        self.start_stop_ps4_nav.pack(pady=10)
        
        # Create the start/stop IR Remote navigation control button
        self.start_stop_ir_remote_nav = tk.Button(self.nav_frame, text="Start IR remote Control", font=("Arial", 12), command=self.toggle_ir_remote_navigation)
        self.start_stop_ir_remote_nav.pack(pady=10)
        
        # Create the start/stop sensors button
        self.start_stop_sensors = tk.Button(self.sensor_frame, text="Start Sensors", font=("Arial", 12), command=self.toggle_sensors)
        self.start_stop_sensors.pack(pady=10)
        
        # Create the video stream
        self.video_label = tk.Label(self.video_frame, text="Live Video Stream", font=("Arial", 16))
        self.video_label.pack(pady=10)
        
        # Create the ThingSpeak
        self.thingspeak_label = tk.Label(self.thingspeak_frame, text="ThingSpeak", font=("Arial", 16))
        self.thingspeak_label.pack(pady=10)

#---TOGGLES-----------------------------------------------------------------------------------#
#---Toggle Function, Button Commands to stop/start mutli threading ---------------------------#
#---Autonomous Navigation (threaded)----------------------------------------------------------#
# WHYYYYYY?!!!??!?!?!?!
    def toggle_autonomous_navigation(self):        
        # Toggle function for autonomous navigation
        if self.is_autonomous == True:
            self.start_stop_auto_nav.config(text="Stop Autonomous Navigation")
            print("Autonomous navigation started.")
            # start a thread for the obstacle avoidance
            #self.start_thread_obstacle_avoidance()
            self.is_autonomous = False
            
        else:
            self.is_autonomous = True
            self.start_stop_auto_nav.config(text="Start Autonomous Navigation")
            print("Autonomous navigation stopped.")
            # stop the thread for the obstacle avoidance
            #self.stop_thread_obstacle_avoidance()


#---GUI Navigation Control (threaded)---------------------------------------------------------#
    def toggle_gui_navigation(self):
        # Toggle function for GUI navigation control
        if self.start_stop_gui_nav['text'] == "Start GUI Navigation Control":
            self.start_stop_gui_nav.config(text="Stop GUI Navigation Control")
            print("GUI navigation control started.")
            # start a thread for the GUI navigation
            self.start_gui_navigation()
        else:
            self.start_stop_gui_nav.config(text="Start GUI Navigation Control")
            print("GUI navigation control stopped.")
            # stop the thread for the GUI navigation
            self.stop_gui_navigation()
            
#---Keyboard Navigation Control (threaded)----------------------------------------------------#
    def toggle_keyboard_navigation(self):
        # Toggle function for Keyboard navigation control
        if self.start_stop_keyboard_nav['text'] == "Start Keyboard Navigation Control":
            self.start_stop_keyboard_nav.config(text="Stop Keyboard Navigation Control")
            print("Keyboard navigation control started.")
            # start a thread for the keyboard navigation
            self.start_keyboard_navigation()
        else:
            self.start_stop_keyboard_nav.config(text="Start Keyboard Navigation Control")
            print("Keyboard navigation control stopped.")
            # stop the thread for the keyboard navigation
            self.stop_keyboard_navigation()
            
#---Hand Navigation Control (threaded)------------------------------------------------------#
    def toggle_hand_navigation(self):
        # Toggle function for Hand navigation control
        if self.start_stop_hand_nav['text'] == "Start Hand Navigation Control":
            self.start_stop_hand_nav.config(text="Stop Hand Navigation Control")
            print("Hand navigation control started.")
            # start a thread for the hand navigation
            self.start_hand_navigation()
        else:
            self.start_stop_hand_nav.config(text="Start Hand Navigation Control")
            print("Hand navigation control stopped.")
            # stop the thread for the hand navigation
            self.stop_hand_navigation()
            
#---PS4 Controller Navigation Control (threaded)--------------------------------------------#
    def toggle_ps4_navigation(self):
        # Toggle function for PS4 controller navigation control
        if self.start_stop_ps4_nav['text'] == "Start PS4 Controller Navigation Control":
            self.start_stop_ps4_nav.config(text="Stop PS4 Controller Navigation Control")
            print("PS4 controller navigation control started.")
            # start a thread for the PS4 controller navigation
            self.start_ps4_navigation()

        else:
            self.start_stop_ps4_nav.config(text="Start PS4 Controller Navigation Control")
            print("PS4 controller navigation control stopped.")
            # stop the thread for the PS4 controller navigation
            self.stop_ps4_navigation()
            
#---IR Remote Navigation Control (threaded)------------------------------------------------------#
    def toggle_ir_remote_navigation(self):
        # Toggle function for IR remote controller navigation control
        if self.start_stop_ir_remote_nav['text'] == "Start IR remote Controller Navigation Control":
            self.start_stop_ir_remote_nav.config(text="Stop IR remote Controller Navigation Control")
            print("IR remote controller navigation control started.")
            # start a thread for the IR remote controller navigation
            self.start_ir_remote_navigation()

        else:
            self.start_stop_ir_remote_nav.config(text="Start IR remote Controller Navigation Control")
            print("IR remote controller navigation control stopped.")
            # stop the thread for the IR remote controller navigation
            self.stop_ir_remote_navigation()
            
            
#---Sensors (threaded)----------------------------------------------------------------------------#
    def toggle_sensors(self):
        # Toggle function for sensors
        if self.start_stop_sensors['text'] == "Start Sensors":
            self.start_stop_sensors.config(text="Stop Sensors")
            print("Sensors started.")
            # start a thread for the sensors
            self.start_sensors()
        else:
            self.start_stop_sensors.config(text="Start Sensors")
            print("Sensors stopped.")
            # stop the thread for the sensors
            self.stop_sensors()

#--THREADING--------------------------------------------------------------------------------------------#
#--Threading (obstacle avoidance)-----------------------------------------------------------------------#
    def obstacle_avoidance(self):
        while not self.stop_thread:
            print("Obstacle Avoidance!!!!!!")
            sleep(1)
        
    def start_thread_obstacle_avoidance(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.obstacle_avoidance, # funciton to run in the thread
            daemon=True                     # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_thread_obstacle_avoidance(self):
        self.stop_thread = True
        self.thread.join() # join means to join your multithread back into the main program

#--Threading (GUI navigation)---------------------------------------------------------------------------#
    def gui_navigation(self):
        while not self.stop_thread:
            print("GUI Navigation!!!!!!!")
            sleep(1)
        
    def start_gui_navigation(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.gui_navigation,     # funciton to run in the thread
            daemon=True                     # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_gui_navigation(self):
        self.stop_thread = True
        self.thread.join()
        
#--Threading (Keyboard navigation)---------------------------------------------------------------------#
    def keyboard_navigation(self):
        while not self.stop_thread:
            print("Keyboard Navigation!!!!!!!")
            sleep(1)
    
    def start_keyboard_navigation(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.keyboard_navigation, # funciton to run in the thread
            daemon=True                      # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_keyboard_navigation(self):
        self.stop_thread = True
        self.thread.join()

#--Threading (Hand navigation)-------------------------------------------------------------------------#
    def hand_navigation(self):
        while not self.stop_thread:
            print("Hand Navigation!!!!!!!")
            sleep(1)
        
    def start_hand_navigation(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.hand_navigation, # funciton to run in the thread
            daemon=True                  # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_hand_navigation(self):
        self.stop_thread = True
        self.thread.join()
        
#--Threading (PS4 controller navigation)---------------------------------------------------------------#
    def ps4_navigation(self):
        while not self.stop_thread:
            print("PS4 Controller Navigation!!!!!!!")
            sleep(1)
        # Add code to initiate PS4 controller navigation control here
        #self.ps4 = nav_ps4 # start/stop #Need a function to start/stop the controller
        #self.ps4
        
    def start_ps4_navigation(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.ps4_navigation, # funciton to run in the thread
            daemon=True                 # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_ps4_navigation(self):
        self.stop_thread = True
        self.thread.join()
        
#--Threading (IR Remote navigation)--------------------------------------------------------------------#
    def ir_remote_navigation(self):
        while not self.stop_thread:
            print("IR Remote Navigation!!!!!!!")
            sleep(1)
        # print("IR remote controller navigation control started.")
        # nav_remote.run_remote()
        
    def start_ir_remote_navigation(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.ir_remote_navigation, # funciton to run in the thread
            daemon=True                       # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_ir_remote_navigation(self):
        self.stop_thread = True
        self.thread.join()
        
#--Threading (Sensors)----------------------------------------------------------------------------------#
    def sensors(self):
        while not self.stop_thread:
            print("Sensors!!!!!!!")
            sleep(1)
        
    def start_sensors(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.sensors, # funciton to run in the thread
            daemon=True         # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_sensors(self):
        self.stop_thread = True
        self.thread.join()
        
#--Threading (Video Stream)----------------------------------------------------------------------------#
    def video_stream(self):
        while not self.stop_thread:
            print("Video Stream!!!!!!!")
            sleep(1)
        
    def start_video_stream(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.video_stream, # funciton to run in the thread
            daemon=True               # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_video_stream(self):
        self.stop_thread = True
        self.thread.join()
        
#--Threading (ThingSpeak)------------------------------------------------------------------------------#
    def thingspeak(self):
        while not self.stop_thread:
            print("ThingSpeak!!!!!!!")
            sleep(1)
        
    def start_thingspeak(self):
        self.stop_thread = False
        # create a new thread object
        self.thread = Thread(
            target=self.thingspeak, # funciton to run in the thread
            daemon=True            # thread stops when program ends
        )
        # start the thread's execution
        self.thread.start()
        
    def stop_thingspeak(self):
        self.stop_thread = True
        self.thread.join()
        

        
        
        
        
        
        
            
#---Main Function---------------------------------------------------------------#
def main():
    # Create the main window
    root = tk.Tk()
    
    # Create the deployment object
    deploy = PioneerDeploy(root)
    
    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
