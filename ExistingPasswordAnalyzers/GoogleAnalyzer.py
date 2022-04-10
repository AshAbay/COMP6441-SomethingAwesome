from ExistingPasswordAnalyzers.PasswordAnalyzer import PasswordAnalyzer


class GoogleAnalyzer(PasswordAnalyzer):

    def __init__(self):
        super().__init__()

    def gmail_rules(self, inputString):
        if len(inputString) < 8:
            return False
        else:
            return True

    def run_against_common_passwords(self):
        common_passwords = self.rockyou_lines + self.owasp_one_million_list_lines
        passwords_that_passed = []
        passwords_that_failed = []

        for common_password in common_passwords:
            if self.gmail_rules(common_password):
                passwords_that_passed.append(common_password)
            else:
                passwords_that_failed.append(common_password)
        passwords_that_passed_top_10 = passwords_that_passed[:10]
        return passwords_that_passed_top_10, len(common_passwords), len(passwords_that_passed), \
               (len(passwords_that_passed) / len(common_passwords)) * 100
