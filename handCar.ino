int IN1 = 11;  // 오른쪽 바퀴 전진 PWM
int IN2 = 10;  // 오른쪽 바퀴 후진 PWM
int IN3 = 6;   // 왼쪽 바퀴 전진 PWM
int IN4 = 5;   // 왼쪽 바퀴 후진 PWM
char command;

int baseSpeed = 220;   // 기본 전진 속도 (0~255)
int turnSpeed = 140;   // 회전 시 느린 쪽 속도

void setup() {
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void stopMotors() {
  analogWrite(IN1, 0);
  analogWrite(IN2, 0);
  analogWrite(IN3, 0);
  analogWrite(IN4, 0);
}

void loop() {
  if (Serial.available()) {
    command = Serial.read();

    if (command == 'F') {
      // 전진: 양쪽 바퀴 모두 앞으로
      analogWrite(IN1, baseSpeed);
      analogWrite(IN2, 0);
      analogWrite(IN3, baseSpeed);
      analogWrite(IN4, 0);

    } else if (command == 'L') {
      // 좌회전: 오른쪽 바퀴 빠르게, 왼쪽 바퀴 느리게 앞으로
      analogWrite(IN1, baseSpeed);   // 오른쪽 바퀴 빠름
      analogWrite(IN2, 0);
      analogWrite(IN3, turnSpeed);   // 왼쪽 바퀴 느림
      analogWrite(IN4, 0);

    } else if (command == 'R') {
      // 우회전: 왼쪽 바퀴 빠르게, 오른쪽 바퀴 느리게 앞으로
      analogWrite(IN1, turnSpeed);   // 오른쪽 바퀴 느림
      analogWrite(IN2, 0);
      analogWrite(IN3, baseSpeed);   // 왼쪽 바퀴 빠름
      analogWrite(IN4, 0);

    } else if (command == 'B') {
      // 후진: 양쪽 바퀴 모두 뒤로
      analogWrite(IN1, 0);
      analogWrite(IN2, baseSpeed);
      analogWrite(IN3, 0);
      analogWrite(IN4, baseSpeed);

    } else {
      // 정지
      stopMotors();
    }
  }
}
