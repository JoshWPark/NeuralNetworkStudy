# pin에 연결된 LED에 value(0/1) 값을 출력하여 LED를 켜거나 끄는 함수
import RPi.GPIO as GPIO  

def led_on_off(pin, value):
    GPIO.output(pin, value)