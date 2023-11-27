import random
import re

class CustomerServiceBot:
    negative_commands = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_question = (
        "How can I assist you today?",
        "What brings you here?",
        "Is there anything specific you'd like help with?",
        "How may I be of service to you?",
        "Do you have any questions about our products or services?Please let us know!!"
    )

    def __init__(self):
        self.support_babble = {
            'appointment_scheduling_intent': r'.*\s*schedule.*',
        'order_tracking_intent': r'.*\s*track.*order.*',
        'general_support_intent': r'.*\s*(help|support|assistance).*',
        'product_information_intent': r'.*\s*(product|information|details).*',
        'feedback_intent': r'.*\s*(feedback|suggestions).*'
        }

    def greet(self):
        self.name = input("Welcome to Customer Service! What is your name?\n")
        print(f"Hi {self.name}")        
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Thank you. Have a great day!")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            if reply in self.negative_commands:
               print("Thank you. Have a great day!")
               break

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_babble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'appointment_scheduling_intent':
                return self.appointment_scheduling_intent()
            elif found_match and intent == 'order_tracking_intent':
                return self.order_tracking_intent()
            elif found_match and intent == 'general_support_intent':
                return self.general_support_intent()
            elif found_match and intent == 'product_information_intent':
                return self.product_information_intent()
            elif found_match and intent == 'feedback_intent':
                return self.feedback_intent()
        
        if not found_match:
                return self.no_match_intent()

    def appointment_scheduling_intent(self):
        responses = ("To schedule an appointment, visit our official website or call our customer service at 1-800-123-4567.\n",
                 "Booking appointments is a breeze! Use our online portal or reach us directly for personalized assistance.\n")
        return random.choice(responses)

    def order_tracking_intent(self):
        responses = ("To track your order, log in to your customer account on our website or contact our support team.\n",
                 "Stay updated on your order's progress! Visit our order tracking page or get in touch with us for real-time updates.\n")
        return random.choice(responses)

    def general_support_intent(self):
        responses = ("For dedicated customer support, reach us via email at support@gmail.com or call our helpline at 040-243605426.\n",
                 "Our support team is here 24/7 to assist you. Feel free to contact us with any questions or concerns.\n")
        return random.choice(responses)

    def product_information_intent(self):
        responses = ("Explore detailed product information on our website, including specifications, features, and pricing.\n",
                 "Discover everything about our products in our online catalog or get in touch with our sales team for personalized assistance.\n")
        return random.choice(responses)

    def feedback_intent(self):
        responses = ("We appreciate your feedback! Share your thoughts, suggestions, or concerns via email at feedback@gmail.com.\n",
                 "Thank you for contributing to our improvement! Your feedback helps us enhance our products and services.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("I'm sorry if I didn't quite catch that. Could you please provide more details or clarify your question?\n",
                 "I'm here to assist! Can you provide additional information or context for your inquiry?\n",
                 "It looks like I might have missed something. Could you elaborate a bit more on your question or concern?\n")
        return random.choice(responses)
bot = CustomerServiceBot()
bot.greet()
