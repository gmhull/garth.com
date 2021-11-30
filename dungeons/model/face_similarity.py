import face_recognition
from pathlib import Path
from PIL import Image
import cv2

def get_img_encoding():
    # Load the image of the person we want to find similar people for
    known_image = face_recognition.load_image_file("People_Pics/My Face.JPG")

    # Encode the known image
    known_image_encoding = face_recognition.face_encodings(known_image)[0]

    return known_image_encoding

def take_screenshot(arg):
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()

        if ret:
            img = cv2.imwrite("screenshot.png", frame)

        cv2.imshow('frame', frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

    return img

def compare_face():
    known_image_encoding = get_img_encoding()
    screenshot = take_screenshot()

    # Get the location of faces and face encodings for the current image
    face_encodings = face_recognition.face_encodings(screenshot)

    # Get the face distance between the known person and all the faces in this image
    face_distance = face_recognition.face_distance(face_encodings, known_image_encoding)[0]

    return face_distance

if __name__ == "__main__":
    face_dist = compare_face()

    if face_dist > 0.6:
        print("This is the same person.")
    else:
        print("This is not the same person.")
