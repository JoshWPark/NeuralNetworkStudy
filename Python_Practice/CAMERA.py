# 실시간 카메라를 보여주고 버튼이 눌렸을 시 사진을 저장하는 함수
import cv2
import os
import time

def NOWCAMERA(picture_trigger):
    camera = cv2.VideoCapture(0, cv2.CAP_V4L)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    while True:
        ret, frame = camera.read()
        if ret:
            cv2.imshow('카메라 미리보기', frame)
            key = cv2.waitKey(1)
            if picture_trigger.value:
                current_directory = os.path.dirname(os.path.abspath(__file__))
                timestamp = time.strftime('%Y%m%d%H%M%S')
                image_name = f'촬영된_이미지_{timestamp}.jpg'
                
                image_path = os.path.join(current_directory, image_name)
                cv2.imwrite(image_path, frame)
                print(f'이미지를 저장했습니다: {image_path}')
                captured_image = cv2.imread(image_path)
                cv2.imshow('Captured Image', captured_image)
                picture_trigger.value = not picture_trigger.value
                
            elif key == 27 : 
                break

    camera.release()
    cv2.destroyAllWindows() 
