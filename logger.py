logger.py
import time
class LogManager:
    def __init__(self, logfile="floot.log"):
        self.file = logfile
    def write(self, text):
        with open(self.file, "a") as f:
            f.write(f"[{time.ctime()}] {text}\n")
