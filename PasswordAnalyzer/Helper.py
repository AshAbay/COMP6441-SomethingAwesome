from functools import reduce

import enchant
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Helper:

    def __init__(self):
        self.english_dict = enchant.Dict("en-AU")

    def get_characters_freq_from_password(self, inputString):
        characters_hashmap = {}
        for char in inputString:
            if char in characters_hashmap:
                characters_hashmap[char] += 1
            else:
                characters_hashmap[char] = 1
        return characters_hashmap

    def password_has_multiple_words_no_split(self, inputString):
        if len(inputString) == 0 or self.english_dict.check(inputString):  # input string is one word
            return False
        stripped_string = inputString
        original_string = inputString
        count = 0
        while len(stripped_string) > 0:
            if (self.english_dict.check(stripped_string)):  # if it is a word
                found_word = stripped_string
                original_string = original_string[len(found_word):]
                stripped_string = original_string
                count += 1
            else:
                stripped_string = stripped_string[:-1]
        if count <= 1:
            return False
        else:
            return True

    def password_has_multiple_words_with_number_or_special(self, inputString):
        count = 0
        if len(inputString) == 0 or self.english_dict.check(inputString):  # input string is one word
            return False
        words = re.split('[^a-zA-Z]', inputString)
        print(words)
        for word in words:
            if len(word) > 0 and self.english_dict.check(word):
                count += 1
        if count <= 1:
            return False
        else:
            return True

    def remove_trailing_and_beginning_number_special(self, original_password):
        input_string = original_password
        while len(input_string) > 1:
            if not input_string[0].isalpha():
                input_string = input_string[1:]
            if not input_string[-1].isalpha():
                input_string = input_string[:-1]
            if len(input_string) > 0 and input_string[0].isalpha() and input_string[-1].isalpha():
                break
        if len(input_string) > 0 and not input_string[0].isalpha():
            input_string = input_string[1:]
        return input_string

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

    def get_letters_indices_from_password(self, inputString):
        letters_indices = []
        for i in range(len(inputString)):
            if inputString[i].isalpha():
                letters_indices.append(i)
        return letters_indices

    def get_numbers_indices_from_password(self, inputString):
        number_indices = []
        for i in range(len(inputString)):
            if inputString[i].isdigit():
                number_indices.append(i)
        return number_indices

    def get_special_chars_indices_from_password(self, inputString):
        special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        special_chars_indices = []
        for i in range(len(inputString)):
            if inputString[i] in special_characters:
                special_chars_indices.append(i)
        return special_chars_indices


    def indices_difference_is_same(self, indices_list):
        indices_difference = []
        for i in range(1, len(indices_list)):
            indices_difference.append(indices_list[i] - indices_list[i-1])

        index_difference_hashmap = {}
        for index_difference in indices_difference:
            if index_difference in index_difference_hashmap:
                index_difference_hashmap[index_difference] += 1
            else:
                index_difference_hashmap[index_difference] = 0

        for index_difference in index_difference_hashmap.keys():
            if index_difference_hashmap[index_difference] > 0.55*len(indices_difference):
                return True
        return False

    def number_difference_is_same(self, numbers_in_password):
        numbers_in_password_difference = []
        for i in range(1, len(numbers_in_password)):
            numbers_in_password_difference.append(numbers_in_password[i] - numbers_in_password[i - 1])

        number_difference_hashmap = {}
        for index_difference in numbers_in_password_difference:
            if index_difference in number_difference_hashmap:
                number_difference_hashmap[index_difference] += 1
            else:
                number_difference_hashmap[index_difference] = 0

        for index_difference in number_difference_hashmap.keys():
            if number_difference_hashmap[index_difference] > 0.55 * len(numbers_in_password_difference):
                return True

        return False

    def gcd_between_two_numbers(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd_between_two_numbers(b, a % b)

    def gcd_between_multiple_numbers(self, numbers):
        if len(numbers) <= 1:
            return numbers[0]
        if len(numbers) == 2:
            return self.gcd_between_two_numbers(numbers[0], numbers[1])
        else:
            return reduce(lambda x, y: self.gcd_between_two_numbers(x, y), numbers)

    def password_indices_follow_pattern(self, indices_list):
        if self.indices_difference_is_same(indices_list):
            return True
        if self.gcd_between_multiple_numbers(indices_list) != 1:
            return True
        return False

    def password_numbers_follow_pattern(self, inputString):
        numbers_in_password = [int(s) for s in inputString.split() if s.isdigit()]
        if self.number_difference_is_same(numbers_in_password):
            return True
        if self.gcd_between_multiple_numbers(numbers_in_password) != 1:
            return True
        return False
