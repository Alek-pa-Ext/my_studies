import telebot
from films import f_w_dir_list

def insert_vote(cur, tg_id, tg_vote):
    cur.execute("INSERT INTO votes (user_id, vote) VALUES (%s, %s);", (tg_id, tg_vote))

def delete_vote(cur, tg_id):
    cur.execute("DELETE FROM votes WHERE user_id = %s;", (str(tg_id),))

def is_already_vote(cur, tg_id):
    cur.execute("SELECT user_id FROM votes;")
    id_list = [id[0] for id in cur.fetchall()]
    if str(tg_id) in id_list:
        return True
    else:
        return False

def create_keyboard(wigth, amount):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=wigth)
    butt_list = [telebot.types.InlineKeyboardButton(text=f'{i}', callback_data=f'{i}')
                 for i in range(1, amount + 1)]
    keyboard.add(*butt_list)
    return keyboard

def cancel_vote_butt():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text='Відмінити', callback_data='cancel'))
    return keyboard

def update_last_mess(cur, last_mess, tg_id):
    cur.execute("UPDATE votes SET last_mess = %s WHERE user_id = %s;", (str(last_mess), str(tg_id)))

def last_message(cur, tg_id):
    cur.execute("SELECT last_mess FROM votes WHERE user_id = %s;", (str(tg_id),))
    return str(cur.fetchone()[0])


if __name__ == '__main__':
    id = '432591269'
    vote = 3
    conn, cur = open_db()
    change_vote(cur, id, vote)
    conn.commit()
    cur.execute("SELECT * FROM votes;")
    print(cur.fetchall())