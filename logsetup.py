from datetime import datetime
import sys

class Logger:
    def __init__(self, logfile="tp_log.txt"):
        self.terminal = sys.stdout
        self.log = open(logfile, "a", encoding="utf-8")

    def write(self, message):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        if message.strip():  # undvik tomma rader med bara \n
            self.terminal.write(message)
            self.log.write(timestamp + message)
        else:
            self.terminal.write(message)
            self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger()
