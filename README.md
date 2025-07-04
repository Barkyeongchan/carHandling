# 손동작 인식 자동차 제어 프로젝트 (with OpenCV + Arduino)

## 📌 개요

- **프로젝트 목표**  
  OpenCV를 활용해 손동작을 인식하고, 동작에 따라 **자동차를 제어**하는 시스템 제작.

- **참여 인원**  
  👤 박영찬

- **주요 기능**
  - 손동작 인식 기반 차량 제어
  - 정지 / 직진 / 좌회전 / 우회전 / 후진 제어

- **시연**

  ![결과물](https://github.com/user-attachments/assets/03240cf1-38a9-455e-a60e-0b090416ca96)

  https://github.com/user-attachments/assets/58c2f4e5-a98c-48de-97ad-e59afe157651


---

## 사용 기술 및 도구

| 항목       | 내용                       |
|------------|----------------------------|
| 언어       | Python, C++ (Arduino)      |
| 플랫폼     | Windows                    |
| 개발환경   | PyCharm, Arduino IDE       |
| 주요 라이브러리 | OpenCV, Mediapipe (cvzone 기반) |

---

## 제작 과정

1. **Raspberry Pi → Windows 전환**
   - 초기에는 Raspberry Pi 사용 계획이었으나, `Mediapipe` 설치 불가 이슈로 Windows로 변경

2. **손동작 인식 코드 적용**
   - [cvzone](https://www.computervision.zone/) 의 Hand Tracking 오픈소스를 활용하여 손가락 인식 구현

3. **파이썬 ↔ 아두이노 통신**
   - `Serial 통신`으로 Python에서 손동작을 인식 한 후 명령어를 보내고, Arduino가 모터를 제어하는 방식 구성

4. **모터 제어 로직 구현**
   - 손동작에 따라 아두이노에서 L9110S 모터드라이버를 통해 두 바퀴 회전 제어

---

## 기능 설명

- **동작에 따른 차량 제어**
  | 손동작              | 동작     |
  |----------------------|----------|
  | 주먹                  | 정지 (S) |
  | 손가락 다 펼침        | 직진 (F) |
  | 엄지만 펼침          | 좌회전 (L) |
  | 새끼손가락만 펼침     | 우회전 (R) |
  | 이 외 손동작         | 정지 (S) |
  | 손 인식 안됨         | 정지 (S) |

- **제어 흐름도**

  ![플로우차트](https://github.com/user-attachments/assets/d4633cde-a220-4bf4-8c91-dce1a07c4b42)

---

## 기타 정보

- 시리얼 통신 속도: `9600 baud`
- 모터 드라이버: `L9110S`
- 카메라 인식 시 손은 **오른손** 기준, **손등이 위**, **손바닥이 아래**를 향하게 인식

---
