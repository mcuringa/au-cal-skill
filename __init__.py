from mycroft import MycroftSkill, intent_file_handler


class AdelphiCalendar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calendar.adelphi.intent')
    def handle_calendar_adelphi(self, message):
        self.speak_dialog('calendar.adelphi')


def create_skill():
    return AdelphiCalendar()

