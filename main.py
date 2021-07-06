import cv2, dlib, sys
import numpy as np
#스케일러를 통해 비디오 크기를 줄여준다.
scaler = 0.3

detector = dlib.get_frontal_face_detector()
#d아래의 shape머시기는 머신러닝으로 학습된 파일임. 구글링해서 다운 받았음.
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#캡 함수로 비디오 링크를 넣는다.
cap = cv2.VideoCapture('samples/girl.mp4')

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy()

    #detect faces
    faces = detector(img)
    face = faces[0]

    #얼굴 특이점을 추출하기 위해 프레딕터 사용
    dlib_shape = predictor(img, face)
    #연산을 쉽게하기위해 numpy사용 그리고 shape_2d함수에 넣는다.
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])

    
    #visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), color=(255, 255, 255),
    thickness=2, lineType=cv2.LINE_AA)
    
    #for문을 돌면서 68개의 점이 그려진다
    for s in shape_2d:
        cv2.circle(img, center=tuple(s), radius=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    #Imshow함수로 화면 출력. 앞에는 출력 타이틀 이름 뒤에는 imread의 리턴 값
    cv2.imshow('img', img)
    cv2.waitKey(1)