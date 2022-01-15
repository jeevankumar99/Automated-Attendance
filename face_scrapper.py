# Extracts detected_faces from images and returns a list of face images.

import cv2
import sys
import os
import face_recognition

def extract_faces(image_path):
    
    # # read image from path
    # image = cv2.imread(image_path)
    # grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # output_img = cv2.imwrite("grayscale_img.jpg", grayscale_img)
    # # print ("Output Image saved!\n")

    # # Find detected_faces using pre trained cascade model.
    # faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # detected_faces = faceCascade.detectMultiScale(
    #     grayscale_img,
    #     scaleFactor=1.3,
    #     minNeighbors=3,
    #     minSize=(30, 30)
    # )

    # print ("Found {0} detected_faces".format(len(detected_faces)))

    # # Draw a rectangle around the face.
    # for (x, y, w, h) in detected_faces:
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # # Save the output image to corpus
    # ouput_path = f'output_corpus{os.sep}output_{image_path[13:]}'
    # output_img = cv2.imwrite(ouput_path, image)
    # print ("Detected Faces image saved!\n")
    # return detected_faces

    input_image =face_recognition.load_image_file(image_path)

    # Convert input image to RGB
    input_image = cv2.cvtColor(input_image,cv2.COLOR_BGR2RGB)
    
    # Extract Faces from image
    detected_faces = face_recognition.face_locations(input_image)
    output_image = input_image.copy()
    
   # Draw rectangle around detected faces.
    for face in detected_faces:
        cv2.rectangle(output_image, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
    cv2.imshow('Detected Faces', output_image)
    cv2.waitKey(0)

    return detected_faces



if __name__ == "__main__":
    extract_faces(sys.argv[1])