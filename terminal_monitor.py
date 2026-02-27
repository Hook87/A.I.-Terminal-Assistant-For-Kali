 terminal_monitor.py
import subprocess
import sys
from ai_engine import AIEngine
from logger import LogManager
class TerminalMonitor:
    def __init__(self):
        self.ai = AIEngine()
        self.log = LogManager()
    def start(self):
        print("[Floot] Monitoring terminal. Type commands below.\n")
        while True:
            cmd = input("▶ ")
            if cmd.strip().lower() in ["exit", "quit"]:
                print("Exiting Floot assistant.")
                break
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(line, end="")
                result = self.ai.analyze_output(line)
                if result:
                    print("\n[Floot AI] " + result + "\n")
                    self.log.write(result)
