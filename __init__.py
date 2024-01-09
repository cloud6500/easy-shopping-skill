from mycroft import MycroftSkill, intent_file_handler,intent_handler


class EasyShopping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    #@intent_file_handler('shopping.easy.intent')
    #def handle_shopping_easy(self, message):
       # self.speak_dialog('shopping.easy')

    @intent_handler('view.goods.intent')
    def handle_view_goods(self, message):
        self.speak('Taking a photo now. Please wait a second for me to get the result.')
        self.speak('I find some goods here, you can ask me whatever goods you want.')

    @intent_handler('is.there.any.goods.intent')
    def handle_is_there_any_goods(self, message):
        category_label = message.data.get('category')
        str = 'yes, I find ' + category_label + ' in front of you'
        self.speak(str)

def create_skill():
    return EasyShopping()

