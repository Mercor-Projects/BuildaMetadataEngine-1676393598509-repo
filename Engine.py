
from scenedetect import open_video, ContentDetector, StatsManager
from customdetector import CustomDetector
from scene_manager import SceneManager
import numpy
# def on_new_scene(frame_img: numpy.ndarray, frame_num: int,):
#     print("New scene found at frame %d." % frame_num)
# callback=on_new_scene



class Engine :
  def __init__(self, file,yolo):
    if(type(file)==list):
      for i in file:
        name=i.split('.')[0]
        video = open_video(i)
        scene_manager = SceneManager()
        with open(f'{name}.json', 'w') as f:
          print("The json file is created")
        f.close()

        scene_manager.add_detector(CustomDetector())
        scene_manager.detect_scenes(video=video,name=name,yolo1=yolo)
        
        
    else:
      name=file.split('.')[0]
      video = open_video(file)
      scene_manager = SceneManager()
      with open(f'{name}.json', 'w') as f:
        print("The json file is created")
      f.close()

      scene_manager.add_detector(CustomDetector())
      scene_manager.detect_scenes(video=video,name=name,yolo1=yolo)
      
      
# Save per-frame statistics to disk.


