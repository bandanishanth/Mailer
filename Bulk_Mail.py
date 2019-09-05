
# Importing the SMTP library API that will be sending the mail....
import smtplib

# A Password input module that does not display console...........
import getpass



# Mailer class.
class Mailer:

    # A class constructor that takes the arguments as apparent below.
    def __init__(self):
        pass

    def set(self, sender_mail_id, sender_mail_password, mail_subject, mail_message, mail_recepients):
        self.__sender_id = sender_mail_id
        self.__sender_password = sender_mail_password
        self.__message = mail_message
        self.subject = mail_subject
        self.recepients = mail_recepients

        # Initially Null that will later become a smtplib object.
        self.mobj = None

        # __call__=self
        return self

    def __call__(self):
        return self

    def display_data(self):
        return self.__sender_id, self.__message, self.recepients

    # We pass the host (e.g. smtp.gmail.com) and the port number as strings.
    def login(self, host, port):
        try:
            print("Attempting to connect!!!")
            self.mobj = smtplib.SMTP_SSL(host, port)
            print("Sending Hello Packets!!")
            self.mobj.ehlo()
            print("Attempting Login!")
            self.mobj.login(self.__sender_id, self.__sender_password)
            print("Logged in successfully.")
        except smtplib.SMTPHeloError as e:
            print("Server did not respond to helo packets!!")
            print("Mesage:" + str(e))
        except smtplib.SMTPServerDisconnected as e:
            print("Server Disconnected")
            print("Message:" + str(e))
        except smtplib.SMTPAuthenticationError as e:
            print("Authentication error occurred with message:" + str(e))
        except smtplib.SMTPConnectError as e:
            print("Error occurred while connecting to server with message:" + str(e))
            print("Error occurred.")

    def logout(self):
        try:
            self.mobj.quit()
        except smtplib.SMTPException as e:
            print("Something went wrong!!")
            print("Message:" + str(e))
        return True

    def send(self, recepient):
        print("Attempting to send.")
        try:
            self.mobj.sendmail(self.__sender_id, recepient, 'Subject:' + self.subject + '\n' + self.__message + '\n')
            print("Sent")
        except smtplib.SMTPException as e:
            print("Something went wrong!!")
            print("Message:" + str(e))
        except smtplib.SMTPResponseException as e:
            print("A Response exception was raised")
            print("Message:" + str(e))
            print("Error Code:" + str(e.smtp_error))
        except smtplib.SMTPSenderRefused as e:
            print("Sender refused to send.")
            print("Message:" + str(e))
        except:
            print("Something went wrong in sending mail to " + recepient)

    def send_mails(self, host, port):

        # Login first with desired host and port.
        self.login(host, port)

        # For each recipient send a mail..
        for recepient in self.recepients:
            self.send(recepient)

        # Logout
        self.logout()
        
    def send_mails(self,host,port):

        # Login first with desired host and port.
        self.login(host,port)

        # For each recipient send a mail..
        for recepient in self.recepients:
            self.send(recepient)
        
        self.logout()

    def set_message(message):
        self.__message = message

# If this module itself is being run....testing occurs with the following static arguments.
# Modify the main part for testing as needed....for now the
if __name__ == "__main__":
    sender_id = input("Enter sender ID:")
    sender_password = getpass.getpass("Enter sender password:")
    subject = input("Enter the subject:")
    message = input("Enter the message in a single line:")
    recepients = [x for x in input("Enter recipients separated with commas:").split(',')]
    m = Mailer()
    m.set(sender_id, sender_password, subject, message, recepients)
    m.send_mails("smtp.gmail.com", "465")
    input("Press any key to exit.")