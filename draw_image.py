import cv2
import face_recognition

# Draws labels with detected faces and saves it.

def draw_labels_to_faces(names, face_locations, input_image, output_file_name):
    for name, face_location in zip(names, face_locations):
        y1,x2,y2,x1 = face_location
        
        # draw a filled rectangle around faces.
        cv2.rectangle(input_image,(x1,y1),(x2,y2),(255,0,255),2)
        cv2.rectangle(input_image, (x1,y2-35),(x2,y2), (255,0,255), cv2.FILLED)
        
        # Add label(name) under the rectangle.
        cv2.putText(input_image, name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    
    cv2.imwrite(f"output_corpus/output_{output_file_name}", input_image)