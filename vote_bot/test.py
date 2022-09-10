import telebot
from auth_data import token
from messages import *



def answer(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def hello(message):
        #bot.send_message(message.chat.id, "Hello! I'm a test, so I can't do anything)")
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Дарий")
        item2 = telebot.types.KeyboardButton("Не Дарий")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id,
                         'Выбери, кто ты',
                         reply_markup=markup)

        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            # Если юзер прислал 1, выдаем ему случайный факт
            if message.text.strip() == 'Дарий':
                answer = 'Привет, самый классный мальчик!'
            # Если юзер прислал 2, выдаем умную мысль
            elif message.text.strip() == 'Не Дарий':
                answer = "Здравствуйте!"
            else:
                answer = "Попробуй еще раз"
            # Отсылаем юзеру сообщение в его чат
            bot.send_message(message.chat.id, answer)


    bot.polling()

def print_id(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_id(message):
        user_id = message.from_user.id
        bot.send_message(message.chat.id, user_id)

    bot.polling()

def print_mess(token, user_id, mess):
    bot = telebot.TeleBot(token)
    bot.send_message(user_id, mess)

def answer2(message, user_id, bot):
    if message.text.strip() == 'Так':
        change_vote(cur, user_id, vote)
        conn.commit()
        bot.send_message(message.chat.id, vote_counted, reply_markup=types.ReplyKeyboardRemove())
    elif message.text.strip() == 'Ні':
        bot.send_message(message.chat.id, old_vote, reply_markup=types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, dont_und)
def chose10(bot):
    @bot.message_handler(commands=['start'])
    def buttons(message):
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
        butt_list = [telebot.types.InlineKeyboardButton(text=f'{i}', callback_data=f'{i}') for i in range(1, 14)]
        keyboard.add(*butt_list,)
        bot.send_message(message.chat.id, "Test 10 button"+lorem_ipsum, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.isdigit())
    def answers(call):
        vote = call.data
        bot.answer_callback_query(call.id, text=f'Ваш голос - {vote}', show_alert=True)

if __name__ == '__main__':
    bot = telebot.TeleBot(token)
    user_id = '432591267'
    chose10(bot)


    bot.polling()

