import base
import telebot
from films import film_list
from auth_data import token


def get_id(cur):
    cur.execute("SELECT user_id FROM votes;")
    return [id[0] for id in cur.fetchall()]


bot = telebot.TeleBot(token)
conn, cur = base.open_db()

cur.execute("SELECT vote FROM votes;")
vote_list = [v[0] for v in cur.fetchall()]

results = [0 for _ in range(len(film_list))]

for film in range(len(film_list)):
    for vote in vote_list:
        if vote == film+1:
            results[film] += 1


out_res = dict(zip(results, film_list))
text_mess = 'Результати голосувань:\n\n'
for i in range(len(film_list)):
    text_mess += f'{results[i]} - {film_list[i]}\n'

text_mess += f'\nПереможець - {out_res[max(out_res.keys())]}'

print(text_mess)

user_id = '432591267'
id_list = get_id(cur)


#bot.send_message(user_id, text_mess)

#for id in id_list:
#    bot.send_message(id, text_mess)
