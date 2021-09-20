class RobotModel(object):
    def __init__(self, x, y, frame, speed):
        self.x = x
        self.y = y
        self.frame = frame
        self.speed = speed
        self.timer = 0

    def set_position(self, new_position):
        self.x, self.y = new_position

    def get_position(self):
        return (self.x, self.y)

    def get_frame(self):
        return self.frame

    def next_frame(self):
        self.timer = 0
        self.frame += 1
        self.frame %= 4

    def get_timer(self):
        return self.timer

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
        