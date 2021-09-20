from robotmodel import RobotModel


class RobotController(object):
    def __init__(self, robots):
        self.robots = robots

    def update(self, delta_time):
        for robot in self.robots:
            robot.timer += delta_time
            if robot.get_timer() >= 0.125:
                robot.next_frame()