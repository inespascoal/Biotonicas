# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:08:08 2023

@author: Utilizador
"""

import asyncio
import websockets

#coding:utf-8
from PCA9685 import PCA9685
import time 
class Servo:
    def __init__(self):
        self.angleMin=18
        self.angleMax=162
        self.pwm = PCA9685(address=0x40, debug=True)   
        self.pwm.setPWMFreq(50)               # Set the cycle frequency of PWM
    #Convert the input angle to the value of pca9685
    def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
    def setServoAngle(self,channel, angle):
        if angle < self.angleMin:
            angle = self.angleMin
        elif angle >self.angleMax:
            angle=self.angleMax
        date=self.map(angle,0,180,102,512)
        #print(date,date/4096*0.02)
        self.pwm.setPWM(channel, 0, int(date))
 

        

async def server(websocket, path):
    async for message in websocket:
        await websocket.send(f'Got your msg its: {message}')
        match message:
                case "0":
                    # Main program logic follows:
                  if __name__ == '__main__':
                      print("Now servos will rotate to 90°.") 
                      print("If they have already been at 90°, nothing will be observed.")
                      print("Please keep the program running when installing the servos.")
                      print("After that, you can press ctrl-C to end the program.")
                      S=Servo()
                      while True:
                          try:
                              for i in range(16):
                                  S.setServoAngle(i,90)
                          except KeyboardInterrupt:
                              print ("\nEnd of program")
                              break
                case "1":
                  print("back")
                case "2":
                  print("right")
                case "3":
                  print("left")



start_server=websockets.serve(server, "localhost", 5000)

loop = asyncio.get_event_loop()

loop.run_until_complete(start_server)
loop.run_forever()

# asyncio.get_event_loop.stop()
# loop.stop()

# async def main():
#     async with websockets.serve(echo, "localhost", 8765):
#         print("WebSocket server listening on ws://localhost:8765")
#         await asyncio.Future()  # run forever

# asyncio.run(main())