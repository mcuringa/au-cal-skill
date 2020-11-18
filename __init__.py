from mycroft import MycroftSkill, intent_file_handler, util

from lingua_franca.format import nice_date, nice_date_time, nice_time
from datetime import date

# load the vents property from data.py
from .data import events

class AdelphiCalendar(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_file_handler('springbreak.intent')
    def handle_springbreak(self, message):
        self.speak_dialog("springbreak")



    @intent_file_handler('semester.start.intent')
    def handle_semester_start(self, message):

        # first figure out if they want to know about the fall or spring semester
        month = date.today().month
        term = "spring"
        if month > 5 and month < 10:
            term = "fall"

        if "term" in message.data:
            term = message.data["term"]

        self.log.info(f"asking about the start of the {term} semester")

        # get the data from out dicts
        key = "first-day-" + term
        event = events[key]
        event["start"] = nice_date(date.fromisoformat(event["start"]))

        # send the data to the dialog

        self.speak_dialog("event", event)



def create_skill():
    return AdelphiCalendar()
