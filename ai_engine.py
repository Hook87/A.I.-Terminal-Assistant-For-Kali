ai_engine.py
import re
import time
class AIEngine:
    def __init__(self):
        self.model = self.load_model()
    def load_model(self):
        return "local_minimal_rule_model"
    def analyze_output(self, line):
        patterns = {
            "missing dependency": r"not found|missing|No module named",
            "compile error": r"error:|fatal error",
            "permission": r"permission denied|sudo required",
            "package issue": r"E: Unable to locate package",
            "pip fault": r"pip install failed|Could not build wheels",
        }
        for category, pattern in patterns.items():
            if re.search(pattern, line, re.IGNORECASE):
                return self.generate_response(category, line)
        return None
    def generate_response(self, category, line):
        responses = {
            "missing dependency": f"Dependency missing: '{line.strip()}'. Suggest installing with apt-get or pip.",
            "compile error": f"Compile issue detected: '{line.strip()}'. Check build dependencies.",
            "permission": f"Permission issue detected. Try re-running with sudo.",
            "package issue": f"Package not found. Run 'sudo apt update' then retry.",
            "pip fault": f"Pip error. Try installing build-essential and python3-dev.",
        }
        return responses.get(category, "Unknown issue encountered.")ai
