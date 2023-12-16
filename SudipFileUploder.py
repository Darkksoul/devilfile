import telebot
import json
from telebot import types
bot_id = 'Adarsh_Developer'
def get_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        return None
def save_data(file_name, data):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file)
        return True
    except Exception as e:
        return False
bot = telebot.TeleBot("6455327757:AAGfRYLofYF0xS109IAf7Fy_68dh9Ix2yjY")
bot.delete_webhook()
bot_username = bot.get_me().username
channel_username = '@Aizamods'
@bot.message_handler(commands=['start'])
def start(message):
    broadcast = get_data(f"{bot_id}-user_id.json")
    if broadcast == None:
        push = []
    else:
        push = broadcast

    check_user = push.count(message.from_user.id)
    if check_user > 0:
         """user_exist"""
    else:
        push.append(message.from_user.id)
        save_data(f"{bot_id}-user_id.json", push)
    u = message.from_user.id
    chat = message.chat
    msg = message.text
    if msg == '/start':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("✘ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url='http://t.me/Aizamods')
        item2 = types.InlineKeyboardButton("✅ Jᴏɪɴᴇᴅ",callback_data='join')
        markup.add(item1, item2)
        user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
        bot.send_photo(message.chat.id,photo='https://t.me/Bots_Pay_Alert/941',caption=f"""<b>👋 Hey!   {user_link}

👉 You Need To Join Our Channel To Use This Bot. </b>️""", reply_markup=markup,parse_mode='HTML')
        return
    params = message.text.replace('/start', '')
    try:
        params = int(params)
    except:
        return
    try:
        bot.copy_message(chat_id=chat.id, from_chat_id='-1002007843813', message_id=params)
    except:
        pass

        
@bot.message_handler(content_types=['text', 'photo', 'audio', 'document', 'video', 'animation', 'voice', 'sticker','poll'])
def handle_content_types(message):
    if message.text == '/broadcast':
        handle_broadcast_command(message)
        return
    user_id = message.from_user.id
    member_status = bot.get_chat_member(channel_username, user_id).status
    if member_status not in ["member", "administrator", "creator"]:
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("✘ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url='http://t.me/Aizamods')
        item2 = types.InlineKeyboardButton("✅ Jᴏɪɴᴇᴅ",callback_data='join')
        markup.add(item1, item2)
        user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
        bot.send_photo(message.chat.id,photo='https://t.me/Bots_Pay_Alert/941',caption=f"""<b>👋 Hey!   {user_link}

👉 You Need To Join Our Channel To Use This Bot. </b>""", reply_markup=markup,parse_mode='HTML')
        return            
    copied_message =  bot.copy_message(chat_id='-1002007843813', from_chat_id=message.chat.id, message_id=message.message_id)
    bot.reply_to(message, f"https://t.me/{bot_username}?start={copied_message.message_id}") 
@bot.callback_query_handler(func=lambda call: call.data == 'join')
def join(call):
    user_id = call.from_user.id
    member_status = bot.get_chat_member(channel_username, user_id).status
    if member_status in ["member", "administrator", "creator"]:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markupJ = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("✘ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url='http://t.me/Aizamods')
        item2 = types.InlineKeyboardButton("✘ Dᴇᴠᴇʟᴏᴘᴇʀ",url='https://t.me/MrrrAdarsh')
        markupJ.add(item1, item2)
        bot.send_photo(user_id,photo='https://t.me/Bots_Pay_Alert/941',caption=f"""✘ Hey 👋 !!!

✘ What I Do?

✘ This Bot Design To Store Media/Files/Texts/Etc.

✘ Due To Much Load Sometimes Bot Can Be Response Slowly (Depends On Server Load).

✘ This Specially For Who Want To Store FIles.

✘ Just Send Me Your File/Text/Media And Get Your Shareable Link.""",reply_markup=markupJ,parse_mode='HTML')
    else:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("✘ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url='http://t.me/Aizamods')
        item2 = types.InlineKeyboardButton("✅ Jᴏɪɴᴇᴅ",callback_data='join')
        markup.add(item1, item2)
        bot.send_photo(user_id,photo='https://t.me/Bots_Pay_Alert/941',caption=f"""<b>👋 Hey !!!

👉 You Need To Join Our Channel To Use This Bot. </b>️""", reply_markup=markup,parse_mode='HTML')
        return 
@bot.message_handler(commands=['broadcast'])
def handle_broadcast_command(message):
    if message.chat.id != 5417870023:
        return
    else:
        msg = bot.send_message(message.chat.id, f"""<b>Pʟᴇᴀsᴇ Eɴᴛᴇʀ Tʜᴇ Mᴇssᴀɢᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ:- 👇👇👇</b>""",parse_mode='HTML')
        bot.register_next_step_handler(msg, handle_broadcast_message)

def handle_broadcast_message(message):
    chat_id = message.chat.id
    broadcast_message = message.text

    # Get the list of users from user_list.json (assuming get_data is implemented correctly)
    user_list = get_data(f"{bot_id}-user_id.json")
    if user_list is None:
        bot.send_message(chat_id, "Error: User list not found.")
        return

    total_users = len(user_list)
    total_success = 0
    total_fail = 0

# Broadcast the message to all users in the user list using copy_message
    for user_id in user_list:
        try:
            bot.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=message.message_id)
            total_success += 1
        except Exception as e:
            total_fail += 1

    # Emoji Unicode for visual appeal
    success_emoji = u'\U0001F60E'  # Smiling Face Emoji
    fail_emoji = u'\U0001F622'  # Crying Face Emoji

    # Compose the message with total counts and emojis
    response_message = f"Bʀᴏᴀᴅᴄᴀsᴛ Sᴜᴍᴍᴀʀʏ 👇👇👇\n\n"
    response_message += f"Tᴏᴛᴀʟ Usᴇʀs: {total_users}\n"
    response_message += f"Tᴏᴛᴀʟ Sᴜᴄᴄᴇss: {total_success} {success_emoji}\n"
    response_message += f"Tᴏᴛᴀʟ Fᴀɪʟᴇᴅ: {total_fail} {fail_emoji}\n"

    bot.send_message(chat_id, response_message)              
bot.infinity_polling()