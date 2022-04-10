from ExistingPasswordAnalyzers.PasswordAnalyzer import PasswordAnalyzer


class OutlookAnalyzer(PasswordAnalyzer):

    def __init__(self):
        super().__init__()

    def has_uppercase_letter(self, inputString):
        for ele in inputString:
            if ele.isupper():
                return True
        return False

    def has_lowercase_letter(self, inputString):
        for ele in inputString:
            if ele.islower():
                return True
        return False

    def has_numbers(self, inputString):
        for char in inputString:
            if char.isdigit():
                return True
        return False

    def has_special_characters(self, inputString):
        special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        for char in inputString:
            if char in special_characters:
                return True
        return False

    def outlook_rules(self, inputString):
        if len(inputString) < 8:
            return False
        rules_count = 0

        if self.has_lowercase_letter(inputString):
            rules_count += 1
        if self.has_uppercase_letter(inputString):
            rules_count += 1

        if rules_count >= 2:
            return True

        if self.has_numbers(inputString):
            rules_count += 1

        if rules_count >= 2:
            return True

        if self.has_special_characters(inputString):
            rules_count += 1

        if rules_count >= 2:
            return True
        else:
            return False

    def run_against_common_passwords(self):
        common_passwords = self.rockyou_lines + self.owasp_one_million_list_lines
        passwords_that_passed = []
        passwords_that_failed = []

        for common_password in common_passwords:
            if self.outlook_rules(common_password):
                passwords_that_passed.append(common_password)
            else:
                passwords_that_failed.append(common_password)
        passwords_that_passed_top_10 = passwords_that_passed[:10]
        return passwords_that_passed_top_10, len(common_passwords), len(passwords_that_passed), \
               (len(passwords_that_passed) / len(common_passwords)) * 100
