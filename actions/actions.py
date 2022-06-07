# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import mysql.connector as msql
import pandas as pd
from mysql.connector import Error
import numpy as np
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_first_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities=tracker.latest_message['entities']
        print(entities)
        for e in entities:
            if e['entity'] == 'internal_num':
                internal= e['value']
        result="None"
        try:
           conn = msql.connect(host='localhost', database='chatbot', user='root', password='harshita')
           if conn.is_connected():
              cursor = conn.cursor()
              cursor.execute("SELECT Date FROM chatbot.calender WHERE event like '%Mathan%'")
              records =  cursor.fetchall()
              print(records)
        except Error as e:
            print("Error while connecting to MySQL", e)      

        dispatcher.utter_message(text="heeeloo")

        return []
