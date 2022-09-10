import telebot
import base
from auth_data import token
from messages import *
from treatment import *
from requests import get
from films import film_list

bot = telebot.TeleBot(token)
conn, cur = base.open_db()
buttons = create_keyboard(2, 11)
cancel_butt = cancel_vote_butt()

photo = 'https://i.ibb.co/TPnRBjS/IMG-1139.jpg'

@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id, start_message)
        bot.send_photo(message.chat.id, get(photo).content, reply_markup=buttons)
    except Exception as e:
        bot.send_message(message.chat.id, error_mess)
        print(e)


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def vote_hand(call):
    try:
        vote = int(call.data)
        user_id = call.from_user.id
        if is_already_vote(cur, user_id):
            bot.answer_callback_query(call.id, text=already_vote_message, show_alert=True)
        else:
            insert_vote(cur, user_id, vote)
            conn.commit()
            bot.answer_callback_query(call.id, text=vote_counted, show_alert=True)
            vote_mess = bot.send_message(user_id, text=f'Ваш голос - {film_list[vote - 1]}', reply_markup=cancel_butt)
            update_last_mess(cur, vote_mess.message_id, user_id)
            conn.commit()
    except Exception as e:
        bot.send_message(call.from_user.id, error_mess)
        print(e)


@bot.callback_query_handler(func=lambda call: call.data.strip() == 'cancel')
def cancel_vote(call):
    try:
        user_id = call.from_user.id
        vote_mess = last_message(cur, user_id)
        delete_vote(cur, user_id)
        conn.commit()
        bot.answer_callback_query(call.id, text=cancel_mess, show_alert=True)
        bot.delete_message(user_id, vote_mess)
    except Exception as e:
        bot.send_message(call.from_user.id, error_mess)
        print(e)


@bot.message_handler(commands=['cancel'])
def cancel(message):
    delete_vote(cur, message.from_user.id)
    bot.send_message(message.chat.id, cancel_mess)


bot.polling()

bot.send_message('432591267', 'Бот упал')