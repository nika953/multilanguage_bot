"""Module RASA that provides actions."""
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from googletrans import Translator


class CustomTranslator:
    """A class for translating text and defining language."""

    def __init__(self):
        """Initializes a translator instance and a variable to store the detected language."""
        self.translator = Translator()
        self.detected_lang = None

    def detect_language(self, text: str) -> str:
        """Detects the language of the input text.

        Args:
            text (str): Text to define the language.

        Returns:
            str: The detected language of the text.
        """
        self.detected_lang = self.translator.detect(text).lang
        return self.detected_lang

    def translate_text(self, reply: str) -> str:
        """Translates the text into the detected language.

        Args:
            reply (str): Text to translate.

        Returns:
            str: The translated text.
        """
        if not self.detected_lang:
            print("Language not detected.")
            return reply

        result = self.translator.translate(reply, dest=self.detected_lang)
        return result.text


class ActionGetResponse(Action):
    """Represents an action to receive and send a translated response."""

    def name(self) -> Text:
        """Getter of action name in RASA.

        Returns:
            Text: action name.
        """
        return "action_get_translated_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
             Performs the action: translates and sends a response to the user's request.

             Args:
                 dispatcher (CollectingDispatcher): Used to send messages to the user.
                 tracker (Tracker): Rasa tracker to access the current state of the dialog.
                 domain (Dict[Text, Any]): A dictionary containing responses from which the action can select
                 the appropriate one to reply to the user.

             Returns:
                 List[Dict[Text, Any]]: Empty list, as there is no follow-up.
             """

        user_message = tracker.latest_message.get('text')

        translator = CustomTranslator()

        translator.detect_language(user_message)

        intent_name = tracker.latest_message['intent']['name']

        response_key = f"utter_{intent_name}"
        if response_key in domain['responses']:
            reply = domain['responses'][response_key][0]['text']

            translated_text = translator.translate_text(reply)
            dispatcher.utter_message(text=translated_text)
        else:
            dispatcher.utter_message(text='No response found for this intent.')

        return []
