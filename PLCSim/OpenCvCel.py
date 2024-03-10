import cv2
url = "http://192.168.0.107:8080"
cap = cv2.VideoCapture(url)
 
while(cap.isOpened()):
    camera, frame = cap.read()
    try:
        cv2.imshow('Imagen',
                   cv2.resize(frame,
                              600,400))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
    except cv2.error:
        print("end")
        break
cv2.destroyAllWindows()
        



 




 
 


