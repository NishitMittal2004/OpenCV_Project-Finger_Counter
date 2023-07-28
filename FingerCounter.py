import cv2
import time
import os
import math
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(10,150)
cap.set(3,wCam)
cap.set(4,hCam)

folderpath = "FingerImages"
myList = os.listdir(folderpath)
print(myList)
overlayList = []
for imgPath in myList:
    image = cv2.imread(f'{folderpath}/{imgPath}')
    # print(f'{folderpath}/{imgPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[9][1], lmList[9][2]
        length = math.hypot(x2 - x1, y2 - y1)
        # print(int(length))
        if length > 50:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 Fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers]

        cv2.rectangle(img, (20,225), (170,425), (61,49,204), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45,375), cv2.FONT_HERSHEY_DUPLEX,
                    5, (204,197,247), 20)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (440,50), cv2.FONT_HERSHEY_PLAIN,
                3, (255,0,100), 3)


    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
