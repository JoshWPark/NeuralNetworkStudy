import time
import RPi.GPIO as GPIO    
import multiprocessing
import CAMERA
import DISTANCE
import LED

led = 6  # GPIO6 핀
trig = 20
echo = 16
button = 21  # Move the button definition here

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정

def switch_status(button, picture_trigger):
    if(GPIO.input(button) == 1):
        picture_trigger.value = True

def PHOTOBOOTH(picture_trigger):
    on_off = 1  # 1은 디지털 출력 값. 1 = 5V
    while True:
        
        # DISTANCE
        distance = DISTANCE.measureDistance(trig, echo)
        print("물체와의 거리는 %fcm 입니다." % distance)
        if (distance > 50):
            LED.led_on_off(led, on_off)  # led가 연결된 핀에 1 또는 0 값 출력
            time.sleep(1)  # 1초 동안 잠자기
            on_off = 0 if on_off == 1 else 1  # 0과 1의 토글링
        else:
            LED.led_on_off(led, on_off)  # led가 연결된 핀에 1 또는 0 값 출력
            on_off = 1
            switch_status(button, picture_trigger)
            

if __name__ == "__main__":

    picture_trigger = multiprocessing.Value('b', False)

    process_camera = multiprocessing.Process(target = CAMERA.NOWCAMERA, args=(picture_trigger,))
    process_photobooth = multiprocessing.Process(target = PHOTOBOOTH, args=(picture_trigger,))

    process_camera.start()
    process_photobooth.start()

    try:
        # Wait for both processes to finish (this won't happen in this example as the tasks run indefinitely)
        process_camera.join()
        process_photobooth.join()
    except KeyboardInterrupt:
        # If the user interrupts (Ctrl+C), terminate the processes
        process_camera.terminate()
        process_photobooth.terminate() 
    GPIO.cleanup()