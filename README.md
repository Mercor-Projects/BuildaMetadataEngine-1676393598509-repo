# BuildaMetadataEngine-1676393598509-repo
Mercor Challenge Repository



# Task Overview

Type of Meta data I Used Are


1) Visual Hotspot/Deadzone Detection 
  
  - Scene Edit Detection - To complete this task i used PySceneDetect
  Adaptive or content Algorithm by minor  changing
  in the internal structure of the  pyscenedetect 
  i did try to use manual diffrent algorithm but they are not accurate
  so i went with this Pyscenedetect
  
  
  - Focus Detection - To complete this task i used Fast Fourier Transform(FFT)
  Algorthim which use Laplacian method to detect the blue on the thresold of
  10 you can change thresold acordingaly
  
2) Person Detection(per frame) - To work on this i used Yolov8 Which
is faster than any other ai model on the GPU 

If i consider only  visual hotspot detection or only Focus detection its very fast and work on Real Time Detection 
but using both the Detection Method Its make it somewhat Slower





Installation
requirement - python 3.8.0+

1) Clone the Repository 

```
git clone <git repo link>
```

2) Then install all the dependencies
```
pip install -r requirements.txt
```

3) Then Import Engine class in your Python File as like as app.py file
and add list of video path or single path in the engine class and it will generate
```
from  Engine import Engine


lists=['video.mp4','video2.mp4']

Engine(lists,yolo=True)

```

You can deselect yolo model as it take gpu to run by make the parameter yolo = False
```
Engine(lists,yolo=False)
```
It will generate Json File of Metadata of particual file with the name of the path of the file






  
  
 
