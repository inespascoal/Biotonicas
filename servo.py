{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#coding:utf-8\n",
    "from PCA9685 import PCA9685\n",
    "import time \n",
    "class Servo:\n",
    "    def __init__(self):\n",
    "        self.angleMin=18\n",
    "        self.angleMax=162\n",
    "        self.pwm = PCA9685(address=0x40, debug=True)   \n",
    "        self.pwm.setPWMFreq(50)               # Set the cycle frequency of PWM\n",
    "    #Convert the input angle to the value of pca9685\n",
    "    def map(self,value,fromLow,fromHigh,toLow,toHigh):\n",
    "        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow\n",
    "    def setServoAngle(self,channel, angle):\n",
    "        if angle < self.angleMin:\n",
    "            angle = self.angleMin\n",
    "        elif angle >self.angleMax:\n",
    "            angle=self.angleMax\n",
    "        date=self.map(angle,0,180,102,512)\n",
    "        #print(date,date/4096*0.02)\n",
    "        self.pwm.setPWM(channel, 0, int(date))\n",
    " \n",
    "# Main program logic follows:\n",
    "if __name__ == '__main__':\n",
    "    print(\"Now servos will rotate to 90°.\") \n",
    "    print(\"If they have already been at 90°, nothing will be observed.\")\n",
    "    print(\"Please keep the program running when installing the servos.\")\n",
    "    print(\"After that, you can press ctrl-C to end the program.\")\n",
    "    S=Servo()\n",
    "    while True:\n",
    "        try:\n",
    "            for i in range(16):\n",
    "                S.setServoAngle(i,90)\n",
    "        except KeyboardInterrupt:\n",
    "            print (\"\\nEnd of program\")\n",
    "            break\n",
    "\n",
    "           \n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
