from mycroft import MycroftSkill, intent_file_handler


class CallSimon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('simon.call.intent')
    def handle_simon_call(self, message):
        self.speak_dialog('simon.call')


def create_skill():
    return CallSimon()

