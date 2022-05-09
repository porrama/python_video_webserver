import imutils
import cv2
import time

vid = cv2.VideoCapture(0)

def generate_stream():
    WIDTH = 800         
    fps,st,frames_to_count,cnt = (0, 0, 20, 0)
    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            frame = imutils.resize(frame, width=WIDTH)
            frame = cv2.putText(frame,'FPS: '+str(fps), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
            
            flag, encodedImage = cv2.imencode(".jpg", frame)
            if not flag:
                break
            
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + bytearray(encodedImage) + b"\r\n")

            if cnt == frames_to_count:
                try:
                    fps = round(frames_to_count/(time.time()-st))
                    st = time.time()
                    cnt = 0
                except:
                    pass
            cnt+=1
