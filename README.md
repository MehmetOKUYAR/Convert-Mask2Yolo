# Convert-Mask2Yolo

 The purpose of these studies is to handle cases where pre-prepared and collected projects have masks used for segmentation tasks. However, with the advent of architectures like YOLO, detection processes have been confronted with different label requirements. Consequently, an image processing-based algorithm has been developed to convert mask labels to the YOLO format.

 This developed algorithm transforms mask labels used in previous segmentation tasks into a format compatible with YOLO's label requirements. As a result, pre-prepared datasets can be used with YOLO-like detection-focused architectures.
 
 In conclusion, these studies enable compatibility between various detection architectures and label formats, allowing existing datasets and projects to be utilized with a wider range of detection algorithms. This, in turn, aims to achieve more effective and efficient solutions in the fields of computer vision and object detection.
<br><br>
<p align="center">
  <img src="https://github.com/MehmetOKUYAR/Convert-Mask2Yolo/blob/main/images/diagram.png" alt="Görüntü Açıklaması">
</p>

<br>
 The image above shows how it is converted from the mask format to the YOLO label format, as seen. The outputs will be as shown in the visual below.
 <br><br>
<div style="display: flex;">
  <img src="https://github.com/MehmetOKUYAR/Convert-Mask2Yolo/blob/main/images/mask.jpg" alt="Görsel 1" width="250" height="200">
  <img src="https://github.com/MehmetOKUYAR/Convert-Mask2Yolo/blob/main/images/output.png" alt="Görsel 2" width="250" height="200">
  <img src="https://github.com/MehmetOKUYAR/Convert-Mask2Yolo/blob/main/images/output-txt.png" alt="Görsel 3" width="300" height="200">
</div>
<br><br>
And now, your mask labels are ready to be trained in YOLO format.
<br><br>
<p align="center">
  <img src="https://github.com/MehmetOKUYAR/Convert-Mask2Yolo/blob/main/images/labelconv.png" alt="Görüntü Açıklaması">
</p>
<br><br>

When you run the code with `python3 main.py` you will be greeted with a window as shown below. Here, you will select the paths of your label files and assign their class IDs. After that, you will choose the destination path for saving the results. Once you start the program, your outputs will be saved in YOLO format at the specified location.
<br><br>
<p align="center">
  <img src="https://github.com/MehmetOKUYAR/Convert-Mask2Yolo/blob/main/images/arayuz.jpeg" alt="Görüntü Açıklaması"width="500" height="300">
</p>

# Paper

[A new data label conversion algorithm for YOLO segmentation of medical images](https://doi.org/10.1140/epjs/s11734-024-01338-5)

[A new deep learning-based GUI design and implementation for automatic detection of brain strokes with CT images](https://doi.org/10.1140/epjs/s11734-024-01423-9)

Note: We kindly ask you not to forget to reference your work. We wish you success and enjoyable work!


