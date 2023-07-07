# Image Face Detection and Bounding Box Program

This is a Python program that uses OpenCV to detect faces in an image and draw bounding boxes around them.

## Description

The Image Face Detection and Bounding Box Program is a Python script that utilizes the OpenCV library to perform face detection on an image. It uses the Haar cascade classifier trained for face detection to identify faces in the image. Once a face is detected, a bounding box is drawn around it. The processed image with the bounding box is displayed and saved as a new image file.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python and OpenCV installed.
3. Download the `haarcascade_frontalface_default.xml` file from the OpenCV GitHub repository and place it in the same directory as the script.
4. Replace `'test.jpg'` with the path to your own image file.
5. Run the program using `face_detection.py`.
6. The program will display the original image with bounding boxes around detected faces.
7. The processed image with bounding boxes will be saved as `face_detected.jpg` in the same directory.

## Example

```python
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()

cv2.imwrite("face_detected.jpg", img)
```

## Requirements
- Python 3.x
- OpenCV library (`pip install opencv-python`)


## License
[MIT Licence] (e.g., MIT License)

[The MIT license gives express permission for users to reuse code for any purpose, sometimes even if code is 
part of proprietary software. As long as users include the original copy of the MIT license in their
distribution, they can make changes or modifications to the code to suit their own needs.]



## Contribution
Contributions are welcome! If you have any suggestions, bug fixes, or new features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request, explaining the changes you have made.


Please ensure that your contributions adhere to the coding conventions and follow the project's guidelines.

## Author
[Soorjyakanta](https://github.com/soorjya): Project developer and maintainer
