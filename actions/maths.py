from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAddNumbers(Action):

    def name(self) -> Text:
        return "action_add_numbers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        left = entities[0]['value']
        right = entities[1]['value']
        sum_value = left + right
        dispatcher.utter_message(text=f"The sum of {left} and {right} is {sum_value}")

        return []
