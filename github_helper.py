 github_helper.py
import subprocess
import os
from ai_engine import AIEngine
from logger import LogManager
class GitHubHelper:
    def __init__(self, repo_url):
        self.url = repo_url
        self.ai = AIEngine()
        self.log = LogManager()
    def process_repo(self):
        print(f"[Floot] Processing GitHub repo: {self.url}")
        repo_name = self.url.rstrip("/").split("/")[-1]
        if not os.path.isdir(repo_name):
            print("[Floot] Cloning repository...")
            subprocess.run(f"git clone {self.url}", shell=True)
        print("[Floot] Checking for build scripts...")
        if os.path.isfile(f"{repo_name}/install.sh"):
            print("[Floot] Found install.sh. Running…")
            self.run_script(f"{repo_name}/install.sh")
        elif os.path.isfile(f"{repo_name}/setup.py"):
            print("[Floot] Found setup.py. Trying pip install…")
            self.run_script(f"pip install .", cwd=repo_name)
        else:
            print("[Floot] No installer found. User may need manual steps.")
    def run_script(self, command, cwd=None):
        proc = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            print(line, end="")
            result = self.ai.analyze_output(line)
            if result:
                print("\n[Floot AI] " + result + "\n")
                self.log.write(result)
