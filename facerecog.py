import face_recognition
image = face_recognition.load_image_file("faces.jpg")
face_locations = face_recognition.face_locations(image)
