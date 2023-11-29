# 초음파 센서로 거리를 측정하고 반환 해주는 함수

import time
import RPi.GPIO as GPIO  

def measureDistance(trig, echo):
    time.sleep(0.5)  # 0.5초 간격으로 거리 측정
    GPIO.output(trig, 1)  # trig 핀 신호 High
    time.sleep(0.00001)  # 10 마이크로초 동안 대기
    GPIO.output(trig, 0)  # trig 핀 신호 Low

    while GPIO.input(echo) == 0:  # echo 핀 값이 1로 바뀔때까지 대기
        pass

    pulse_start = time.time()  # 초음파 발사 시간 기록
    while GPIO.input(echo) == 1:  # echo 핀 값이 0이 될때까지 대기
        pass

    pulse_end = time.time()  # 초음파 수신 시간 기록
    pulse_duration = pulse_end - pulse_start  # 경과 시간 계산
    distance = pulse_duration * 340 * 100 / 2  # 거리 계산 (단위: cm)
    return distance  