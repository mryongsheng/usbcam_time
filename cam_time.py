import datetime
import time
import cv2
import numpy as np


def Setcamera(cap):
    cap.set(6,cv2.VideoWriter.fourcc('M','J','P','G'))
    cap.set(3,1920)
    cap.set(4,1080)

cap = cv2.VideoCapture(0)
Setcamera(cap)


fx = 1.308216739155389e+03
cx = 9.145809351163745e+02
fy = 1.308809351908079e+03
cy = 4.622537203449925e+02
k1, k2, p1, p2, k3 = -0.395685031140606,0.160358422413760,0.001647777791774,-5.270874798988524e-04,0.0


k = np.array([
    [fx, 0, cx],
    [0, fy, cy],
    [0, 0, 1]
])

d = np.array([
    k1, k2, p1, p2, k3
])

t = 0.1 
counter = 0
fps = 0
start_time = time.time()
 
#undistort
def undistort(img):
    h, w = img.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
 
while(True):    
    ret, frame = cap.read()  
    frame = undistort(frame)
    current_time = time.time()
    seconds = int(current_time)
    mseconds= int(current_time*1000)
    timestr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')      
    im_dir = '/home/fansne/Desktop/usbcam/pic/'+timestr+'.jpg'
    cv2.imwrite(im_dir,frame)
    
    counter += 1    
    if (time.time() - start_time) > t:
        fps = counter / (time.time() - start_time)
        fps = str(fps)
        counter = 0
        start_time = time.time()       
    cv2.putText(frame, "FPS {0}" .format(fps), (10, 30), 1, 1.5, (255, 0, 255), 2)
        
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF ==27:
        break
 
cap.release()
cv2.destroyAllWindows()




'''
#static CvCapture * cap;        
#cap = cvCaptureFromCAM(cam_index);
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while(True):
    ret, frame = cap.read()  # ret==True/False: read successfully or not; frame: image

    if not ret:
        print("Failed to read the image.")
        break
    # display image

    print (timestr)
    cv2.imshow('Video', frame)

    # press ESC key to exit
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
'''
     


'''
dt = '2019-02-12 14:32:15'
ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
print(ts)
 
ts = 1549953233.456123
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
print(dt)
'''
