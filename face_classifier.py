# Classifies detected faces to trained student's faces.

import cv2
import face_recognition
from face_recognition.api import face_distance
import sys
import os


def classify_faces(students_face_encodings, detected_faces_encodings):
    students_present_indexes = []

    # compare students and detected face encodings
    for detected_face_encoding in detected_faces_encodings:
        
        # to get the face with most similarity (distance)
        least_face_distance = 1
        classified_face_index = None
        face_matched = False
        for index, student_face_encoding in enumerate(students_face_encodings):
            
            # if faces match is distance is least
            if (face_recognition.compare_faces(student_face_encoding, detected_face_encoding))[0] == True:
                face_matched = True
                face_distance = face_recognition.face_distance(student_face_encoding, detected_face_encoding)
                if  face_distance < least_face_distance:
                    least_face_distance = face_distance
                    classified_face_index = index
        
        # -100 is dummy index to avoid duplication.
        if not face_matched:   
            print("No face matching!")
            students_present_indexes.append(-100)
        else:
            students_present_indexes.append(classified_face_index)
        print (students_present_indexes)    
                
    return students_present_indexes
            

def load_student_corpus_and_encode(path="face_corpus"):
    students_path = os.listdir(path)
    students_face_encodings = []
    
    for student in students_path:
        student_image = face_recognition.load_image_file(f"{path}{os.sep}{student}")

        # convert the file to RGB from BGR and load
        student_image = cv2.cvtColor(student_image, cv2.COLOR_BGR2RGB)
        student_encoding = face_recognition.face_encodings(student_image)
        students_face_encodings.append(student_encoding)
        print ("Loaded face ", student)

    return students_face_encodings


def map_students_to_indexes(student_indexes, path="face_corpus",):
    students_file_list = os.listdir(path)
    mapped_students = []
    
    # Remove last 4 chars (.jpg) from file names
    for i in range(len(students_file_list)):
        students_file_list[i] = students_file_list[i][:-4]
    
    # maps all positive indexes to students
    for index in student_indexes:
        if index > -1:
            mapped_students.append(students_file_list[index])
        else:
            mapped_students.append(None)

    return mapped_students

