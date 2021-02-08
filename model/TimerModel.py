
class TimerModel:

    def __init__(self):
        self.time_to_display = "00:00"
        self.minutes = 0
        self.hours = 0

    def update_time(self):
        self.minutes += 1

        if self.minutes > 59:
            self.hours += 1
            self.minutes = 0
        self.format_time_to_display()

    def format_time_to_display(self):
        if self.hours < 10:
            self.time_to_display = "0" + str(self.hours) + ":"
        else:
            self.time_to_display = str(self.hours) + ":"

        if self.minutes < 10:
            self.time_to_display += "0" + str(self.minutes)
        else:
            self.time_to_display += str(self.minutes)

    def resume_timer(self, h, m):
        self.hours = h
        self.minutes = m
