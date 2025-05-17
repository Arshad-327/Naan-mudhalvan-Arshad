import time

class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.prev_error = 0

    def compute(self, setpoint, actual, dt):
        error = setpoint - actual
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        self.prev_error = error
        return self.kp*error + self.ki*self.integral + self.kd*derivative

pid = PID(1.0, 0.1, 0.05)
actual_speed = 0
setpoint = 50
for t in range(1, 21):
    control = pid.compute(setpoint, actual_speed, 1)
    actual_speed += control * 0.1
    print(f"Time {t}s: Speed={actual_speed:.2f}")
    time.sleep(0.1)