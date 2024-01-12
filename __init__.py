from mycroft import MycroftSkill, intent_file_handler,intent_handler
from adapt.intent import IntentBuilder

class EasyShopping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    #@intent_file_handler('shopping.easy.intent')
    #def handle_shopping_easy(self, message):
       # self.speak_dialog('shopping.easy')

   # @intent_handler('view.goods.intent')
   # def handle_view_goods(self, message):
       # self.speak('Taking a photo now. Please wait a second for me to get the result.')
       # self.speak('I find some goods here, you can ask me whatever goods you want.')

    @intent_handler(IntentBuilder('ViewItemInHand').require('ViewItemInHandKeyWord'))
    def handle_view_item_in_hand(self, message):
        self.speak('Taking a photo now. Please wait a second for me to get the result.')
        self.speak('The item is possible to be something. You can ask me any details about the item now, such as brand, color or complete information.')


    @intent_handler(IntentBuilder('AskItemCategory').require('Category').build())
    def handle_ask_item_category(self, message):
         self.speak('I am talking about the category of the item')

    @intent_handler(IntentBuilder('AskItemColor').require('Color').build())
    def handle_ask_item_color(self, message):
         self.speak('I am talking about the color of the item')

    @intent_handler(IntentBuilder('AskItemBrand').require('Brand').build())
    def handle_ask_item_brand(self, message):
        self.speak('I am talking about the brand of the item')

    @intent_handler(IntentBuilder('AskItemKw').require('Kw').build())
    def handle_ask_item_keywords(self, message):
        self.speak('I am talking about the keywords of the item')

    @intent_handler(IntentBuilder('AskItemInfo').require('Info').build())
    def handle_ask_item_complete_info(self, message):
        self.speak('I am speaking the complete information of the item')

    @intent_handler(IntentBuilder('FinishOneItem').require('Finish').build())
    def handle_finish_current_item(self, message):
        self.speak('Got you request. Let\'s continue shopping!')

   # @intent_handler(IntentBuilder('ViewItemInHand').require('Hand').build())
    #def handle_hand_current_item(self, message):
       # self.speak('Taking the photo now.Please wait me to get the result!')

    #@intent_handler('is.there.any.goods.intent')
    #def handle_is_there_any_goods(self, message):
        #category_label = message.data.get('category')
        #str = 'yes, I find ' + category_label + ' in front of you'
        #self.speak(str)

    @intent_handler('is.there.any.goods.intent')
    def handle_is_there_any_goods(self, message):
        # in real application, label_str and loc_list will return from CV API
        label_list = [['milk', 'drink', 'bottle'], ['milk', 'drink', 'bottle']]
        loc_list = ['left top', 'right top']

        category_label = message.data.get('category')
        detected = 0
        for i in range(len(label_list)):
            label_str = label_list[i]
            label_str_subs=''
            for j in range(len(label_str)):
                label_str_sub = label_str[j].lower()
                label_str_subs+=label_str_sub+' '

            if category_label is not None:
                if category_label in label_str_subs:
                    self.speak_dialog('yes.goods',
                                {'category': category_label,
                                'location': loc_list[i]})
                    detected = 1
                    break
            else:
                continue

        if detected == 0:
            self.speak_dialog('no.goods',
            {'category': category_label})

    @intent_handler('view.goods.intent')
    def handle_view_goods(self, message):
        self.speak_dialog('take.photo')


def create_skill():
    return EasyShopping()

