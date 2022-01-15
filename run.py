import face_recognition
import cv2
from face_classifier import *
from face_scrapper import extract_faces
from draw_image import draw_labels_to_faces
from attendance_manager import *


def main():
    # Load input image
    input_image = face_recognition.load_image_file(sys.argv[1])
    input_image = cv2.cvtColor(input_image,cv2.COLOR_BGR2RGB)
    
    # Extract faces from input image
    detected_faces_encodings, faces_location = extract_faces(input_image)
    print ("Faces scraped!")
    
    # Load students' faces to encode the model.
    students_face_encodings = load_student_corpus_and_encode()
    print ("Students faces loaded!")
    
    # Classify the extracted faces to each student.
    present_student_indexes = classify_faces(students_face_encodings, detected_faces_encodings)
    present_students = map_students_to_indexes(present_student_indexes)
    print (present_students)
   
   # Draw the detected faces with labels and save the file.
    output_file_name = f"{sys.argv[1][13:]}"
    draw_labels_to_faces(present_students, faces_location, input_image, output_file_name)

    # Mark the attendance.
    my_cursor = initialize_db()
    mark_present(my_cursor, present_students)


if __name__ == "__main__":
    main()