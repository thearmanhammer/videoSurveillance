import cv2
import numpy as np
import time
import requests

global i
i=0

while True:
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)
    # Check if camera opened successfully
    if (cap.isOpened() == False): 
    	print("Unable to read camera feed")
  
    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    #name the file
    name = ('static/output'+str(i)+'.mp4')

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter(name,cv2.VideoWriter_fourcc('X', '2', '6', '4'), 7, (frame_width,frame_height))

    f = 0
    while (f<100):
        ret, frame = cap.read()
        if ret == True:
            # Write the frame into the file 'output.avi'
            out.write(frame)

            f = f+1

            # Display the resulting frame    
            cv2.imshow('frame',frame)

            # Press Q on keyboard to stop recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break 

    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    r = requests.post('https://peaceful-sierra-83628.herokuapp.com/feed', files={'clip':open(name,'rb')})
    print('POSTED')

    # Closes all the frames
    cv2.destroyAllWindows()
    i = i+1