from mycroft import MycroftSkill, intent_file_handler, util

from lingua_franca.format import nice_date, nice_date_time, nice_time
from datetime import date
import os, sys
import json
# import data

class AdelphiCalendar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.ay = ""
        self.current_term = ""
        self.spring_dates = {}
        self.fall_dates = {}




    def load_data(self, filename):
        # dir = os.getcwd()
        # pathname = os.path.dirname(sys.argv[0])
        # dir = os.path.abspath(pathname)
        dir = util.resolve_resource_file("skills/adelphi-calendar-skill/" + filename)
        # self.log.info(f"{dir}")
        with open(dir) as jf:
            data = json.load(jf)
        return data

    def initialize(self):


        def clean(jso):
            o = jso.copy()
            o["no-scool"] = bool(o["no-school"])
            o["start"] = date.fromiso(o["start"])
            if o["end"]:
                o["end"] = date.fromiso(o["end"])
            return o

        self.fall_dates = self.load_data("fall.json")
        self.log.info(self.fall_dates["summer-graduation"]["start"])

        month = date.today().month
        if month < 6:
            self.current_term = "spring"
        else:
            self.current_term = "fall"







    @intent_file_handler('semester.adelphi.intent')
    def handle_calendar_adelphi(self, message):
        # self.log.info("handling semester intent")
        term = message.data.get("term", self.current_term)
        self.log.info(f"asking about the {term} semester")
        self.speak("hold on")
        # if term == "spring":
        #     self.speak_dialog("spring.term.adelphi")
        # else:
        #     self.speak_dialog("fall.term.adelphi")


    # @intent_file_handler('calendar.adelphi.intent')
    # def handle_calendar_adelphi(self, message):
    #     # self.speak_dialog('calendar.adelphi')
    #     event = message.data["event"]
    #     print("calendar event", event)
    #     self.speak("you want to know about " + str(event))




def create_skill():
    return AdelphiCalendar()
