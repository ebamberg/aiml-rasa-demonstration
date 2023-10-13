# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGreetPlayer(Action):
     def name(self) -> Text:
         return "action_greet_player"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         playername = tracker.get_slot("playername")
         if not playername:
             dispatcher.utter_message(text="Sorry mighty player. I didn't get your name. How shall I call you ?")
         else: 
            dispatcher.utter_message(text=f"Hello, I will call you {playername} from now on")
         return []        

class ActionPrintLocationDecription(Action):
     def name(self) -> Text:
         return "action_print_location_decription"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        with open(f'gamedata/locations/{location}/description.txt') as f:
            description = f.read()
        dispatcher.utter_message(text=description)
        return []       


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
