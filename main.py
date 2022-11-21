import cv2 as cv
import numpy as np
import random

colors = ["red", "green","blue"]
random.shuffle(colors)

cam = cv.VideoCapture(0)

print(colors)


while True:
    ret, frame = cam.read()
    if not ret:
        continue
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    output = frame.copy()

    bin = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1.3, 200, param1=50, param2=50,minRadius=70, maxRadius=110)
    if circles is not None:
        circles = np.round(circles[0,:]).astype("int")

        for (x, y, r) in circles:
            bgr = (int(frame[y, x][0]), int(frame[y, x][1]), int(frame[y, x][2]))
            cv.circle(output, (x, y), r, bgr, -1)
        
        cv.putText(output, f"Balls = {len(circles)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
        
        if len(circles) == 3:
            ball_colors = []
            print('Colors of balls:')
            x_min = min(circles[0][0], circles[1][0], circles[2][0])
            for j in range(3):
                x_min = min(circles[0][0], circles[1][0], circles[2][0])
                for i in range(3):
                    if circles[i][0] == x_min:
                        circles[i][0] = 1000
                        y = circles[i][1]
                        ball_colors.append(frame[y, x_min])
                        print(frame[y, x_min])

            

    cv.imshow('frame', output)
    cv.imshow('binary', bin)
    k = cv.waitKey(10)
    if k > 0:
        if chr(k) == 'd':
            break

cam.release()
cv.destroyAllWindows()
