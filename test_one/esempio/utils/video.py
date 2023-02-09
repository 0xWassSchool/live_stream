# la struttura base di questo codice e' stata presa da internet ma poi modificata per renderla ottimale
import cv2 

cam = cv2.VideoCapture(0)

def camera_video():
    while True:
        x, img_frame = cam.read() 
        if not x:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', img_frame)
            img_frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_frame + b'\r\n')