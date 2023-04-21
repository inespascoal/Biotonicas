
# acho que este é melhor

from Servo import *
servo=Servo()


def forward():
    # não é necessario definir os angulos iniciais porque no Servo.py já é feito
    
    try:
        for i in range(30): 
            servo.setServoAngle(12,90+i) # pata da frente direita levanta
            servo.setServoAngle(6,90+i) # pata de trás contrária levanta
            time.sleep(0.001)
            
        for i in range(30):
            # para as patas anteriores pousarem no chão
            servo.setServoAngle(3,90-i) # pata da frente esquerda anda para trás
            servo.setServoAngle(9,90-i) # para de trás direita faz o mesmo
            time.sleep(0.01)
            
        for i in range(60):
            servo.setServoAngle(3,60+i) # a pata frente esquerda anda para a frente
            servo.setServoAngle(9,60+i) # a pata trás direita anda para a frente

            servo.setServoAngle(12,120-i) # a pata da frente direita vai para tras
            servo.setServoAngle(6,120-i) # a pata de trás esquerda vai para tras
            
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")

        


def backwards():
    servo.setServoAngle(4,0)
    servo.setServoAngle(3,0)
    servo.setServoAngle(2,90)
    
    servo.setServoAngle(7,0)
    servo.setServoAngle(6,0)
    servo.setServoAngle(5,90)
    
    servo.setServoAngle(8,0)
    servo.setServoAngle(9,0)
    servo.setServoAngle(10,90)
    
    servo.setServoAngle(11,0)
    servo.setServoAngle(12,0)
    servo.setServoAngle(13,90)
    try:
        for i in range(30): 
            servo.setServoAngle(12,90-i) # anda para a frente uma pata
            servo.setServoAngle(6,90-i) # anda para a frente a para de trás contrária
            time.sleep(0.001)
            
        for i in range(30):
            servo.setServoAngle(3,90+i) # anda para a frente a outra pata
            servo.setServoAngle(9,90+i) # anda para a frente a para de trás correspondente

        for i in range(30):
            servo.setServoAngle(3,60-2*i) # a 1ª pata volta à posição inicial (como se estivesse sem resistência)
            servo.setServoAngle(9,60-i) # o mesmo

            servo.setServoAngle(12,120+i) # o correspondente para a outra pata
            servo.setServoAngle(6,120+i) # o mesmo
            
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")


def right():
    servo.setServoAngle(4,0)
    servo.setServoAngle(3,0)
    servo.setServoAngle(2,90)
    
    servo.setServoAngle(7,0)
    servo.setServoAngle(6,0)
    servo.setServoAngle(5,90)
    
    servo.setServoAngle(8,0)
    servo.setServoAngle(9,0)
    servo.setServoAngle(10,90)
    
    servo.setServoAngle(11,0)
    servo.setServoAngle(12,0)
    servo.setServoAngle(13,90)
    try:
        for i in range(30): 
            servo.setServoAngle(4,90-i) # anda para a frente uma pata
            servo.setServoAngle(7,90-i) # anda para a frente a para de trás correspondente
            time.sleep(0.01)
            
            for i in range(30):
                servo.setServoAngle(11,90-i) # anda para a frente a outra pata
                servo.setServoAngle(8,90-i) # anda para a frente a para de trás correspondente

                servo.setServoAngle(4,90+i) # a 1ª pata volta à posição inicial (como se estivesse sem resistência)
                servo.setServoAngle(7,90+i) # o mesmo
                time.sleep(0.01)
            
            servo.setServoAngle(11,90+i) # o correspondente para a outra pata
            servo.setServoAngle(8,90+i) # o mesmo
            
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")
        


def left():
    servo.setServoAngle(4,0)
    servo.setServoAngle(3,0)
    servo.setServoAngle(2,90)
    
    servo.setServoAngle(7,0)
    servo.setServoAngle(6,0)
    servo.setServoAngle(5,90)
    
    servo.setServoAngle(8,0)
    servo.setServoAngle(9,0)
    servo.setServoAngle(10,90)
    
    servo.setServoAngle(11,0)
    servo.setServoAngle(12,0)
    servo.setServoAngle(13,90)
    try:
        for i in range(30): 
            servo.setServoAngle(11,90-i) # anda para a frente uma pata
            servo.setServoAngle(8,90-i) # anda para a frente a para de trás correspondente
            time.sleep(0.01)
            
            for i in range(30):
                servo.setServoAngle(4,90-i) # anda para a frente a outra pata
                servo.setServoAngle(7,90-i) # anda para a frente a para de trás correspondente

                servo.setServoAngle(11,90+i) # a 1ª pata volta à posição inicial (como se estivesse sem resistência)
                servo.setServoAngle(8,90+i) # o mesmo
                time.sleep(0.01)
            
            servo.setServoAngle(4,90+i) # o correspondente para a outra pata
            servo.setServoAngle(7,90+i) # o mesmo
            
        print ("\nEnd of program")
    except KeyboardInterrupt:
        print ("\nEnd of program")


        
# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 
    if sys.argv[1] == 'Forward':
        forward()
    elif sys.argv[1] == 'Backwards':
        backwards()
    elif sys.argv[1] == 'Right': 
        right()              
    elif sys.argv[1] == 'Left':   
        left() 


