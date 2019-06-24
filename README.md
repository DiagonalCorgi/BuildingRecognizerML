Building Recognizer Neural Network
Author: Dylan Carlyle
Date: 20/06/2019

Test examples used: eiffel tower and the sydney opera house.

Requirements needed to run:
-Follow this youtube video to install requirements:
	https://www.youtube.com/watch?v=RplXYjxgZbw

HOW TO RUN:

- Open the anaconda command prompt
- type in 'activate tensorflow1' (this is the environment I used, because I ran it off windows)
- then type "idle" to open a python script shell
- from the python script shell, open either "Object_detection_image".py, "Object_detection_video.py" or "Object_detection_webcam.py"
- From there, you can type in the image name or video to test and press F5 to run the module.
- Done.

EXTRAS:
- you can train extra images by activating a cmd into the labelImg-master folder to label the images desired.
- you can run extra training by runnning this in the command line under object_detection:

python legacy\train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config

and see the tensorboard:

tensorboard --logdir=training 

and then open the given localhost address (It should be on port 6060)
