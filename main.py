import cv2
import time
import random
import dropbox

start_time=time.time()
def snapshot():
    print("taking pictures")
    number=random.randint(0,100)
    captureIObj=cv2.VideoCapture(0)
    result=True
    while(result==True):
        ret,frame=captureIObj.read()
        print(ret)
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
        

    return img_name
    captureIObj.release()
    cv2.destroyAllWindows()

def uploadpictures(img):
   token='N3bP87iPQeYAAAAAAAAAAfXEddWt2kAcpWicrdt7f96kUV3u6dBMQn1oKDEekRe3'
   file_from=img
   file_to='/pictures/'+(img)
   dbx=dropbox.Dropbox(token)
   with open(file_from,'rb') as f:
       dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if ((time.time()- start_time)>=1):
            snap=snapshot()
            uploadpictures(snap)

main()