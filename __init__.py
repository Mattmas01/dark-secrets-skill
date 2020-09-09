from mycroft import MycroftSkill, intent_file_handler


class DarkSecrets(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('secrets.dark.intent')
    def handle_secrets_dark(self, message):
        self.speak_dialog('secrets.dark')


def create_skill():
    return DarkSecrets()

