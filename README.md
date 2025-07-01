#openCV를 활용한 손동작 자동차 제어

[목차]
- 개요
- 기술 및 도구
- 제작 과정
- 기능

1. 개요

프로젝트 목표 : openCV를 활용하여 손 동작을 인식 한 후 각 동작에 따라 자동차를 제어한다.

참여인원 : 박영찬

주요 기능
 - 손동작에 따라 정지, 직진, 좌회전, 우회전, 후진한다.

결과물

![Image](https://github.com/user-attachments/assets/03240cf1-38a9-455e-a60e-0b090416ca96)


2. 기술 및 도구

언어 : Python, C++(Arduino)

환경 : Window, Arduino

라이브러리 : Pycharm, openCV


3. 제작 과정

° 최초 Raspberry Pi와 Arduino를 활용하여 제작하려 했지만 Raspberry Pi에서 Python 패키지 중 하나인 Mediapipe가 설치되지않아 Window로 변경

° cvzone(https://www.computervision.zone/) 에서 Hand Tracking 오픈소스 채용

° Serial통신을 사용해 Python과 Arduino를 연결

° Python에서 손동작 인식 후 Arduino에서 모터를 제어하는 방식으로 제작


4. 기능

플로우 차트


