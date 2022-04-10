from pathlib import Path


class PasswordAnalyzer:

    def __init__(self):
        self.rockyou_lines = Path('./passwordFiles/rockyou.txt').read_text(encoding='latin-1').splitlines()
        self.owasp_one_million_list_lines = Path('./passwordFiles/owasp_one_million_list.txt').read_text().splitlines()