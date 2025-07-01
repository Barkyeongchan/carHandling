import cv2
import mediapipe as mp
import time
import serial

# 아두이노 시리얼 연결 (COM 포트 환경에 맞게 변경하세요)
arduino = serial.Serial('COM5', 9600)

class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.7, trackCon=0.6):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=False):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            h, w, c = img.shape
            for id, lm in enumerate(myHand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmList

def fingersUp(lmList):
    tipIds = [4, 8, 12, 16, 20]
    fingers = []

    # 엄지 (오른손, 손등 위 → 엄지 x좌표 비교, 엄지가 오른쪽에 있으므로 x가 크면 펼친 상태)
    if lmList[4][1] > lmList[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # 나머지 손가락: y좌표 비교 (펼친 상태면 팁 y좌표가 마디 y좌표보다 작음)
    for id in range(1, 5):
        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def getPalmOrientation(lmList):
    # 엄지(4번)와 중간손가락 첫 마디(9번)의 x좌표 비교
    if lmList[4][1] > lmList[9][1]:
        return "palm_down"  # 손등 위
    else:
        return "palm_up"    # 손바닥 위


def main():
    pTime = 0
    cap = cv2.VideoCapture(1)  # 카메라 인덱스 조정 필요
    detector = handDetector()
    prevCommand = ""

    while True:
        success, img = cap.read()
        if not success:
            print("카메라 읽기 실패")
            break

        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if len(lmList) != 0:
            fingers = fingersUp(lmList)

            # 손가락 상태 출력
            print(f"Fingers state: {fingers}", end=' ')

            if fingers == [0, 1, 1, 1, 1]:
                command = 'S'  # 주먹 - 정지
            elif fingers == [1, 1, 1, 1, 1]:
                command = 'L'  # 다 펼침 - 직진
            elif fingers == [1, 0, 0, 0, 0]:
                command = 'F'  # 엄지만 펴짐 - 좌회전
            elif fingers == [0, 1, 1, 1, 0]:
                command = 'R'  # 약지만 펴짐 - 우회전
            elif fingers == [0, 0, 0, 1, 1]:
                command = 'B'  # 검지, 중지만 펴짐 - 후진
            else:
                command = 'S'  # 그 외 모두 정지

            print(f"=> Command: {command}")
        else:
            command = 'S'  # 손 없으면 정지
            print("No hand detected => Command: S")

        if command != prevCommand:
            arduino.write(command.encode())
            prevCommand = command

        # FPS 계산
        cTime = time.time()
        fps = 1 / (cTime - pTime) if cTime != pTime else 0
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
