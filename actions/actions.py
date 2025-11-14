from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionGiveWellnessTip(Action):

    def name(self) -> str:
        return "action_give_wellness_tip"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        user_message = tracker.latest_message.get('text', '').lower()

        # Mood-based message categories
        sad_tips = [
            "It's okay to feel sad 🌧️. Try writing down what’s bothering you — it helps clear the mind.",
            "Even rainy days pass 🌦️. Take a short walk, breathe deeply, and let yourself rest.",
            "You’ve overcome hard days before — you’ll do it again 💪.",
            "Listen to calming music or call someone who makes you smile 💙."
        ]

        happy_tips = [
            "That’s wonderful! 🌞 Keep doing what brings you joy.",
            "I love hearing that! 💫 Celebrate your happiness and share it with others.",
            "Keep the positivity flowing 🌻. Maybe spread a little kindness today.",
            "Happiness looks great on you 😄 — enjoy the moment!"
        ]

        anxious_tips = [
            "It’s okay to feel anxious 🫶. Try breathing in for 4 seconds and out for 6.",
            "You are safe in this moment 🌿. Focus on something you can see, touch, and hear.",
            "When your thoughts race, slow them down by grounding yourself — one step at a time.",
            "Remember, anxiety doesn’t define you. You’re doing your best 🌸."
        ]

        stressed_tips = [
            "Take a deep breath 🌬️. Step away for a few minutes and relax your shoulders.",
            "Remember to pause — you can’t pour from an empty cup ☕.",
            "Organize your thoughts, do one thing at a time 💼.",
            "Even a 5-minute break can refresh your mind 🧘."
        ]

        general_tips = [
            "You are enough, exactly as you are 🌈.",
            "Be kind to your mind — it’s doing its best 💫.",
            "Small steps forward still count as progress 🌿.",
            "Don’t be afraid to rest — your body and mind deserve it 💖.",
            "Healing takes time. You’re doing great, even if it doesn’t feel like it 🕊️."
        ]

        # Mood detection keywords
        sad_words = ["sad", "down", "depressed", "unhappy", "cry", "lonely", "upset"]
        happy_words = ["happy", "excited", "joyful", "good", "great", "amazing"]
        anxious_words = ["anxious", "nervous", "worried", "scared", "panic"]
        stressed_words = ["stressed", "tired", "exhausted", "pressure", "burnt out"]

        # Choose response category based on user text
        if any(word in user_message for word in sad_words):
            message = random.choice(sad_tips)
        elif any(word in user_message for word in happy_words):
            message = random.choice(happy_tips)
        elif any(word in user_message for word in anxious_words):
            message = random.choice(anxious_tips)
        elif any(word in user_message for word in stressed_words):
            message = random.choice(stressed_tips)
        else:
            message = random.choice(general_tips)

        dispatcher.utter_message(text=message)
        return []
