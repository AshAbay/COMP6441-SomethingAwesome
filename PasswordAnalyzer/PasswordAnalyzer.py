from PasswordAnalyzer.RuleChecker import RuleChecker

class PasswordAnalyzer:

    def __init__(self):
        pass

    def check_if_password_is_acceptable(self, password):
        rule_checker = RuleChecker(password)
        list_of_issues = set()
        if len(password) < 6:
            return False, "Password needs to be of 6 characters or more."
        else:
            uppercase_result, uppercase_reason = rule_checker.has_uppercase_letter()
            lowercase_result, lowercase_reason = rule_checker.has_lowercase_letter()
            number_special_result, number_special_reason = rule_checker.has_one_number_and_special_character()
            middle_number_special_result, middle_number_special_reason = rule_checker.middle_char_number_special()
            common_password_result, common_password_reason = rule_checker.password_is_too_common()
            if not uppercase_result:
                list_of_issues.add(uppercase_reason)
            if not lowercase_result:
                list_of_issues.add(lowercase_reason)
            if not number_special_result:
                list_of_issues.add(number_special_reason)
            if not middle_number_special_result:
                list_of_issues.add(middle_number_special_reason)
            if not common_password_result:
                list_of_issues.add(common_password_reason)

            if len(list_of_issues) > 0:
                return False, list_of_issues

            return True, list_of_issues

    def rate_password(self, password):
        rule_checker = RuleChecker(password)
        password_is_acceptable, password_unacceptable_reasons = self.check_if_password_is_acceptable(password)
        if not password_is_acceptable:
            return -1, "Password is unacceptable", password_unacceptable_reasons

        improvements_list = set()
        password_strength = 1
        password_is_one_word_result, password_is_one_word_reason = rule_checker.password_is_one_word()
        password_is_one_word_with_number_special_in_middle_result, password_is_one_word_with_number_special_in_middle_reason = \
            rule_checker.password_is_one_word_with_number_special_in_middle()
        password_has_multiple_words_result, password_has_multiple_words_reason = \
            rule_checker.password_has_multiple_words()
        password_has_frequent_characters_result, password_has_frequent_characters_reason = \
            rule_checker.password_has_frequent_characters()
        password_has_pattern_result, password_has_pattern_reason = rule_checker.password_has_pattern()
        password_is_similar_to_common_passwords_result, password_is_similar_to_common_passwords_reason =\
            rule_checker.password_is_similar_to_common_passwords()

        if password_is_one_word_result and password_is_one_word_with_number_special_in_middle_result:
            password_strength += 1
        else:
            if not password_is_one_word_result:
                improvements_list.add(password_is_one_word_reason)
            if not password_is_one_word_with_number_special_in_middle_result:
                improvements_list.add(password_is_one_word_with_number_special_in_middle_reason)

        if password_has_multiple_words_result:
            password_strength += 1
        else:
            improvements_list.add(password_has_multiple_words_reason)

        if password_has_frequent_characters_result:
            password_strength += 1
        else:
            improvements_list.add(password_has_frequent_characters_reason)

        if password_has_pattern_result:
            password_strength += 1
        else:
            improvements_list.add(password_has_pattern_reason)

        if password_is_similar_to_common_passwords_result:
            password_strength += 3
        else:
            improvements_list.add(password_is_similar_to_common_passwords_reason)

        return password_strength, "Password is acceptable", improvements_list
