from datetime import date
from pathlib import Path


class StatsModel:
    def __init__(self, timer):
        self.file_url = Path(__file__).parent / "../storage/stats.txt"
        self.stats_list = []
        self.current_date = date.today()
        self.timer = timer
        self.load_stats()

    def load_stats(self):
        with open(self.file_url, 'r') as f:
            for line in f:
                self.stats_list.append(line)

        last_stat = self.stats_list[-1]
        if last_stat[0:10] == str(self.current_date):
            self.timer.hours = int(last_stat[11:13])
            self.timer.minutes = int(last_stat[14:16])
            self.timer.format_time_to_display()
        else:
            print("Not the same day starting with 00:00")

    def save_stats(self, time):
        stat = str(f"{self.current_date}|{time}\n")
        last_stat = self.stats_list[-1]
        if last_stat[0:10] != str(self.current_date):
            with open(self.file_url, 'a') as f:
                f.write(stat)
        else:
            self.stats_list[-1] = stat
            with open(self.file_url, 'w') as f:
                for line in self.stats_list:
                    f.write(line)
