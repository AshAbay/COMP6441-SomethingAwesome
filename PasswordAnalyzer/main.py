from PasswordAnalyzer.PasswordAnalyzer import PasswordAnalyzer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    password_analyzer = PasswordAnalyzer()
    print("Password is: " + "" + " " + str(password_analyzer.rate_password("")))  # not safe- empty string

    print("Password is: " + "Hi" + " " + str(password_analyzer.rate_password("Hi")))  # not safe, size is only 2

    print("Password is: " + "hel###$123ooo" + " " + str(
        password_analyzer.rate_password("hel###$123ooo")))  # not safe, no uppercase letter

    print("Password is: " + "Hello1" + " " + str(
        password_analyzer.rate_password("Hello1")))  # not safe, doees not have special characters

    print("Password is: " + "]Hello" + " " + str(password_analyzer.rate_password(
        "]Hello")))  # not safe, does not have any special characters or numbers in the middle

    print("Password is: " + "Hello1#" + " " + str(
        password_analyzer.rate_password("Hello1#")))  # not safe, does not have any special characters in the middle

    print("Password is: " + "Hello123]]]" + " " + str(password_analyzer.rate_password("Hello123]]]"))) #not safe, only trailing number and special characters

    print("Password is: " + "12345323$$$" + " " + str(password_analyzer.rate_password("12345323$$$"))) #not safe, no letters

    print("Password is: " + "Hello12#Yp123" + " " + str(password_analyzer.rate_password("Hello12#Yp123")))# not safe only one word
    print("Password is: " + "Hello12#123" + " " + str(password_analyzer.rate_password("Hello12#123")))# not safe only one word
    print("Password is: " + "He12#llo123" + " " + str(password_analyzer.rate_password("He12#llo123")))# not safe only one word
    print("Password is: " + "Abccc1#Abcc1#" + " " + str(password_analyzer.rate_password("Abccc1#Abcc1#")))# not safe only one word
    print("Password is: " + "Hello12#orange123" + " " + str(password_analyzer.rate_password("Hello12#orange123")))# not safe only one word

    print(password_analyzer.rate_password(input("Enter a password to test: ")))




