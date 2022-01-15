# Classifies detected faces to trained student's faces.

import cv2
import face_recognition
from face_recognition.api import face_distance
from face_scrapper import extract_faces
import sys
import os

def classify_faces(students_face_encodings, detected_faces_encodings):
    students_present_indexes = []
    for detected_face_encoding in detected_faces_encodings:
        least_face_distance = 1
        print ("Face change!")
        print (students_present_indexes)
        classified_face_index = None
        for index, student_face_encoding in enumerate(students_face_encodings):
            if (face_recognition.compare_faces(student_face_encoding, detected_face_encoding))[0] == True:
                face_distance = face_recognition.face_distance(student_face_encoding, detected_face_encoding)
                if  face_distance < least_face_distance:
                    least_face_distance = face_distance
                    classified_face_index = index
        students_present_indexes.append(classified_face_index)
                

    return students_present_indexes
            

def load_student_corpus_and_encode(path="face_corpus"):
    students_path = os.listdir(path)
    students_face_encodings = []
    for student in students_path:
        student_image = face_recognition.load_image_file(f"{path}{os.sep}{student}")
        student_image = cv2.cvtColor(student_image, cv2.COLOR_BGR2RGB)
        student_encoding = face_recognition.face_encodings(student_image)
        students_face_encodings.append(student_encoding)
        print ("Loaded face ", student)

    return students_face_encodings


def map_students_to_indexes(student_indexes, path="face_corpus",):
    students_file_list = os.listdir(path)
    mapped_students = []
    for i in range(len(students_file_list)):
        students_file_list[i] = students_file_list[i][:-4]
    
    for index in student_indexes:
        mapped_students.append(students_file_list[index])

    return mapped_students

if __name__ == "__main__":
    detected_faces_encodings, faces_location = extract_faces(sys.argv[1])
    print ("Faces scraped!")
    students_face_encodings = load_student_corpus_and_encode()
    print ("Students faces loaded!")
    present_student_indexes = classify_faces(students_face_encodings, detected_faces_encodings)
    present_students = map_students_to_indexes(present_student_indexes)
    print (present_students)
