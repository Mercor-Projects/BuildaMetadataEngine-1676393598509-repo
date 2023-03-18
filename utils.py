import matplotlib.pyplot as plt
import numpy as np
import cv2
import imutils
from customdetector import CustomDetector
from ultralytics import YOLO
from collections import Counter

def detect_blur(image, size=60, thresh=10, vis=False):
    frame = imutils.resize(image, width=500)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
	# convert the frame to grayscale and detect blur in it
    
    
	# grab the dimensions of the image and use the dimensions to
	# derive the center (x, y)-coordinates
    (h, w) = image.shape
    (cX, cY) = (int(w / 2.0), int(h / 2.0))
 	# compute the FFT to find the frequency transform, then shift
	# the zero frequency component (i.e., DC component located at
	# the top-left corner) to the center where it will be more
	# easy to analyze
    fft = np.fft.fft2(image)
    fftShift = np.fft.fftshift(fft)
    	# check to see if we are visualizing our output
    if vis:
		# compute the magnitude spectrum of the transform
        magnitude = 20 * np.log(np.abs(fftShift))
    	# display the original input image
        (fig, ax) = plt.subplots(1, 2, )
        ax[0].imshow(image, cmap="gray")
        ax[0].set_title("Input")
        ax[0].set_xticks([])
        ax[0].set_yticks([])
		# display the magnitude image
        ax[1].imshow(magnitude, cmap="gray")
        ax[1].set_title("Magnitude Spectrum")
        ax[1].set_xticks([])
        ax[1].set_yticks([])
		# show our plots
        plt.show()
  
    	# zero-out the center of the FFT shift (i.e., remove low
	# frequencies), apply the inverse shift such that the DC
	# component once again becomes the top-left, and then apply
	# the inverse FFT
    fftShift[cY - size:cY + size, cX - size:cX + size] = 0
    fftShift = np.fft.ifftshift(fftShift)
    recon = np.fft.ifft2(fftShift)
    magnitude = 20 * np.log(np.abs(recon))
    mean = np.mean(magnitude)
    
    return mean, mean <= thresh
	# the image will be considered "blurry" if the mean value of the
	# magnitudes is less than the threshold valu




# def adaptivedetector(frame_no,frame_img):
#     cuts =   CustomDetector().process_frame(frame_no, frame_img)
    
    
    
#     print(cuts)
def yolo(image,model):
    res = model.predict(image, classes=[0],verbose=False,show = True,device="0",conf=0.6)
    res = list(res)[0]
    current_no_class = []
    for c in res.boxes.cls:
        conf = res.boxes.conf
        cls = res.boxes.cls
        for  cnf, cs in zip(conf, cls):
                
            if cnf > 0.3:
                    
                current_no_class.append([model.names[int(cs)]])
    
                    
    class_fq = dict(Counter(i for sub in current_no_class  for i in set(sub) if i=='person' ))
    lis=list(class_fq.values())
    for i in lis:
        return i
    
    
    



# vid = cv2.VideoCapture('video2.mp4')
# print(vid.get(cv2.CAP_PROP_FPS))
# frameno =0
# model = YOLO(f"yolov8n.pt",)
# while(vid.isOpened()):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#     if ret:
  
#     # Display the resulting frame
#         frameno=frameno+1
#         res = model.predict(frame, save=False, classes=[0],verbose=False,show = True)
#         res = list(res)[0]
#         current_no_class = []
#         for c in res.boxes.cls:
#             conf = res.boxes.conf
#             cls = res.boxes.cls
#             for  cnf, cs in zip(conf, cls):
                
#                 if cnf > 0.3:
                    
#                     current_no_class.append([model.names[int(cs)]])
#     else :
#         break
                    
#     class_fq = dict(Counter(i for sub in current_no_class  for i in set(sub) if i=='person' ))
#     lis=list(class_fq.values())
#     for i in lis:
        
        
    
        
#         # print(detect_blur_fft(frame))
    
    
     
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break  