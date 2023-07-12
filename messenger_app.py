import re


class MessagingService:
    def send_message(self):
        pass


class SMSMessagingService(MessagingService):
    def send_message(self):
        print("Sending SMS message...")


class EmailMessagingService(MessagingService):
    def send_message(self):
        print("Sending email message...")


class WhatsAppMessagingService(MessagingService):
    def send_message(self):
        print("Sending WhatsApp message...")


def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9.!#$%&’+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$"
    return bool(re.match(email_regex, email))


def is_valid_phone_number(phone_number):
    phone_regex = r"^[6-9]\d{9}$"
    return bool(re.match(phone_regex, phone_number))


if __name__ == "__main__":
    while True:
        print("\n1. SMS")
        print("2. Email")
        print("3. WhatsApp")
        print("4. Exit")
        action = input("Enter the number of the action to perform : ")

        if action == "1":
            mobile_number = input("Enter the mobile number: ")
            if is_valid_phone_number(mobile_number):
                message = input("Enter the message: ")
                sms_service = SMSMessagingService()
                sms_service.send_message()
                print("Message sent successfully!")
            else:
                print("Invalid mobile number!")
        elif action == "2":
            email = input("Enter the email address: ")
            if is_valid_email(email):
                subject = input("Enter the subject of the email: ")
                message = input("Enter the message: ")
                email_service = EmailMessagingService()
                email_service.send_message()
                print("Message sent successfully!")
            else:
                print("Invalid email address!")
        elif action == "3":
            mobile_number = input("Enter the mobile number: ")
            if is_valid_phone_number(mobile_number):
                message = input("Enter the message: ")
                whatsapp_service = WhatsAppMessagingService()
                whatsapp_service.send_message()
                print("Message sent successfully!")
            else:
                print("Your Mobile Number is Invalid")
        elif action == "4":
            break
        else:
            print("Invalid action. Please Choose among (1-4)")
