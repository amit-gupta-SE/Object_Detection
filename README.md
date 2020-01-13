If you hearing about "You Only Look Once" first time, you should know that it is an algorithm that uses convolutional neural networks for object detection. 
You only look once, or YOLO, is one of the fastest object detection algorithms out there. 
Though it is not the most accurate object detection algorithm, but it is a very good choice when we need real-time detection, without loss of too much accuracy.

### Prerequisites
There is a requirements.txt file containing all the prerequisites instaled in your pc.

### Downloading official pretrained weights
Next we need to download official weights pretrained on COCO dataset. You can do this two ways. You can download it manually on same link below, create "weights" folder in repository and copy downloaded weights to that folder. Or you can simply do it with this command: 
```
wget -P weights https://pjreddie.com/media/files/yolov3.weights
```

### Convert weights into TensorFlow format
Now you need to run `load_weights.py` script, to convert downloaded weights to TensorFlow format.
```
python load_weights.py
```

## Running the model
Now you are ready to run the model using `detect_image.py` or `detect_video.py`script. 
You can try to play around with iou_threshold and confidence_threshold parameters.
My example images and video is in `input` folder. So you can put your examples there also or use different location.

### Image usage example
If you'll open `detect_image.py` script at the last line you'll see:
```
main(0.5, 0.5, "input/office.jpg")
```
Here you can play with iou_threshold, confidence_threshold parameters and try you image for detection.<br><br>
Here is few examples:
```
main(0.5, 0.5, "input/office.jpg")
```
```
main(0.5, 0.5, "input/cars.jpg")
```
```
main(0.5, 0.5, "input/zebra.jpg")
```

### Video usage example
If you'll open `detect_video.py` script at the last line you'll see:
```
main(0.5, 0.5, "input/driving.mp4")
```

### Webcam usage example
Just run `webcam.py` script and it will automatically open your webcam and start detecting objects in webcam video input.

### if you want to use the gui
Just run the `object detection application.py` script. It will open a window for you. You can use this gui for image and webcam detection. Video detection is not linked with this gui.
