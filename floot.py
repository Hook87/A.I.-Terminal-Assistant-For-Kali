floot.py
#!/usr/bin/env python3
import argparse
from terminal_monitor import TerminalMonitor
from github_helper import GitHubHelper
from autofix_engine import AutoFixEngine
def main():
    parser = argparse.ArgumentParser(description="Floot AI Terminal Assistant")
    parser.add_argument("--monitor", action="store_true", help="Start real-time terminal assistant mode")
    parser.add_argument("--github", type=str, help="Provide a GitHub repo URL for guided setup")
    parser.add_argument("--autofix", action="store_true", help="Enable auto-fix suggestions queue")
    args = parser.parse_args()
    if args.monitor:
        monitor = TerminalMonitor()
        monitor.start()
    if args.github:
        helper = GitHubHelper(repo_url=args.github)
        helper.process_repo()
    if args.autofix:
        AutoFixEngine.enable()
if __name__ == "__main__":
    main()
