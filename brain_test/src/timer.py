import time

class Timer:
    s = 0.0 # starting time
    time = 0.0
    running = False

    def start(self):
        if self.running:
            return False
        else:
            self.s = time.time() # self.t stores the starting time
            self.running = True
            return True

    def stop(self):
        time_diff = time.time() - self.s
        if self.running:
            self.time = time_diff
            self.running = False
            return True
        else:
            return False

    def get_s(self):
        if self.running:
            self.time = time.time() - self.s
        return self.time

    def get_ms(self):
        if self.running:
            self.time = time.time() - self.s
        return 1000*self.time
