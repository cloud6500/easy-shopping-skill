from mycroft import MycroftSkill, intent_file_handler


class EasyShopping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shopping.easy.intent')
    def handle_shopping_easy(self, message):
        self.speak_dialog('shopping.easy')


def create_skill():
    return EasyShopping()

