# Extracts detected_faces from images and returns a list of face images.

import cv2
import sys
import os
import face_recognition
from face_recognition.api import face_encodings

def extract_faces(image_path):

    input_image = face_recognition.load_image_file(image_path)

    # Convert input image to RGB
    input_image = cv2.cvtColor(input_image,cv2.COLOR_BGR2RGB)
    
    # Extract Faces from image
    faces_location = face_recognition.face_locations(input_image)
    output_image = input_image.copy()
    
   # Draw rectangle around detected faces.
    for face in faces_location:
        cv2.rectangle(output_image, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
    cv2.imshow('Detected Faces', output_image)
    cv2.waitKey(0)

    faces_encodings = face_recognition.face_encodings(input_image)
    return (faces_encodings, faces_location)


if __name__ == "__main__":
    extract_faces(sys.argv[1])