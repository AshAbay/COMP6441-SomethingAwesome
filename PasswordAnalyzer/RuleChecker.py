import enchant

from Helper import Helper
from pathlib import Path
import difflib
import nltk


class RuleChecker:

    def __init__(self, *args):
        if len(args) == 1:
            self.password = args[0]
        else :
            self.password = ""
        self.helper = Helper()
        self.rockyou_lines = Path('../passwordFiles/rockyou.txt').read_text(encoding='latin-1').splitlines()
        self.owasp_one_million_list_lines = Path('../passwordFiles/owasp_one_million_list.txt').read_text().splitlines()
        self.english_dict = enchant.Dict("en-AU")


    def has_uppercase_letter(self):
        for ele in self.password:
            if ele.isupper():
                return True, "Success"
        return False, "Password needs to have at least one upper case letters."

    def has_lowercase_letter(self):
        for ele in self.password:
            if ele.islower():
                return True, "Success"
        return False, "Password needs to have at least one lower case letters."

    def has_one_number_and_special_character(self, input_string = ""):
        password = self.password.lower() if input_string == "" else input_string
        if not self.helper.has_numbers(password):
            return False, "Password needs to have at least one number."
        if not self.helper.has_special_characters(password):
            return False, "Password needs to have at least one special character."
        return True, "Success"


    def middle_char_number_special(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        input_string = self.helper.remove_trailing_and_beginning_number_special(password)
        has_number_or_special_result, has_number_special_reason = self.has_one_number_and_special_character(input_string=input_string)
        if not has_number_or_special_result:
            return False, "Password should be have at least one special character or number in the middle."
        else:
            return True, "Success"

    def password_is_too_common(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        if password in self.rockyou_lines or password in self.owasp_one_million_list_lines:
            return False, "Password is too common"
        return True, "Success"

    def password_is_one_word(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        removed_trailing = self.helper.remove_trailing_and_beginning_number_special(password)
        if len(removed_trailing) == 0:
            return False, "Password needs to have at least one alphabet. "
        if self.english_dict.check(password) or self.english_dict.check(removed_trailing):
            return False, "Password is unsafe, as it is found in dictionary."
        else:
            return True, "Success"

    def password_has_multiple_words(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        if not (self.helper.password_has_multiple_words_no_split(password) or
                self.helper.password_has_multiple_words_with_number_or_special(password)):
            return False, "Password is unsafe, as it is found in dictionary."
        else:
            return True, "Success"

    def password_is_one_word_with_number_special_in_middle(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        password_only_letters = ''.join([i for i in password if i.isalpha()])
        if len(password_only_letters) == 0:
            return False, "Password needs to have at least one alphabet. "
        if self.english_dict.check(password_only_letters):
            return False, "Password is unsafe, as it is found in dictionary."
        else:
            return True, "Success"

    def password_has_frequent_characters(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        characters_hashmap = self.helper.get_characters_freq_from_password(password)
        for char in characters_hashmap.keys():
            if characters_hashmap[char] >= 0.35*len(password):
                return False, "Password seems to have the same character(s) repeated too many times"
        return True, "Success"


    def password_has_pattern(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        number_indices = self.helper.get_numbers_indices_from_password(password)
        letters_indices = self.helper.get_letters_indices_from_password(password)
        special_chars_indices = self.helper.get_special_chars_indices_from_password(password)

        if self.helper.password_indices_follow_pattern(letters_indices) or self.helper.password_indices_follow_pattern(number_indices) \
                or self.helper.password_indices_follow_pattern(special_chars_indices):
            return False, "Password seems to be following a pattern."

        if self.helper.password_numbers_follow_pattern(password):
            return False, "Password seems to be following a pattern"

        return True, "Success"

    def password_is_similar_to_common_passwords(self):
        if len(self.password) == 0:
            return False, "Password needs to be of 6 characters or more."
        password = self.password.lower()
        common_passwords = self.rockyou_lines + self.owasp_one_million_list_lines
        for common_password in common_passwords:
            nltk_distance = nltk.edit_distance(password, common_password)
            if nltk_distance <= 0.5*len(password):
                return False, "Password seems to be similar to a common password"
            seq = difflib.SequenceMatcher(None, common_password, password)
            difflib_ratio = seq.quick_ratio()
            if (difflib_ratio > 0.5) :
                return False, "Password seems to be similar to a common password"
        return True, "Success"



