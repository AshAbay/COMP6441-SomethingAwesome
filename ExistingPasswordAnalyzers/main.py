from ExistingPasswordAnalyzers.FacebookAnalyzer import FacebookAnalyzer
from ExistingPasswordAnalyzers.GoogleAnalyzer import GoogleAnalyzer
from ExistingPasswordAnalyzers.OutlookAnalyzer import OutlookAnalyzer

if __name__ == '__main__':
    outlook_analyzer = OutlookAnalyzer()
    gmail_analyzer = GoogleAnalyzer()
    facebook_analyzer = FacebookAnalyzer()

    outlook_analyzer_passed_passwords, common_password_number, outlook_analyzer_passed_passwords_number, \
        outlook_analyzer_passed_passwords_ratio = outlook_analyzer.run_against_common_passwords()
    gmail_analyzer_passed_passwords, common_password_number, gmail_analyzer_passed_passwords_number, \
        gmail_analyzer_passed_passwords_ratio = gmail_analyzer.run_against_common_passwords()
    facebook_analyzer_passed_passwords, common_password_number, facebook_analyzer_passed_passwords_number, \
        facebook_analyzer_passed_passwords_ratio = facebook_analyzer.run_against_common_passwords()

    print("NUMBER OF COMMON PASSWORDS IN QUESTION: " + str(common_password_number))
    print("OUTLOOK PASSWORD ANALYZER RESULT")
    print("Some of the passwords that got passed: " + str(outlook_analyzer_passed_passwords))
    print("The number of the common passwords that got passed: " + str(outlook_analyzer_passed_passwords_number))
    print("Percentage of common passwords that passed: " + str(outlook_analyzer_passed_passwords_ratio))
    print("GMAIL PASSWORD ANALYZER RESULT")
    print("Some of the passwords that got passed: " + str(gmail_analyzer_passed_passwords))
    print("The number of the common passwords that got passed: " + str(gmail_analyzer_passed_passwords_number))
    print("Percentage of common passwords that passed: " + str(gmail_analyzer_passed_passwords_ratio))
    print("FACEBOOK PASSWORD ANALYZER RESULT")
    print("Some of the passwords that got passed: " + str(facebook_analyzer_passed_passwords))
    print("The number of the common passwords that got passed: " + str(facebook_analyzer_passed_passwords_number))
    print("Percentage of common passwords that passed: " + str(facebook_analyzer_passed_passwords_ratio))
