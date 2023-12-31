from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: final = '6759192612:AAEVFQBDcN0Uy8ztxawVVdUfZTShkyW5NTY'
BOT_USERNAME: final = '@Doodlee_122bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('HELLO! THANKS for chatting with me! I am Doodle! your dude')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('HELLO! I am Doodle! your dude. How can I help you')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'HEY there!'
    
    if 'how are you' in processed:
        return 'I am fine!'
    
    if 'what are you doing' in processed:
        return 'I am waiting for your question'
    
    if 'Git & Github' in processed:
        return 'Le bhai LINK : https://youtu.be/Ez8F0nW6S-w?si=xwO1qdI3PTWEOoM-'
    
    if 'java' in processed:
        return 'le bhai LINK : https://youtube.com/playlist?list=PLxgZQoSe9cg00xyG5gzb5BMkOClkch7Gr&si=O1_eCRGO2ZZ9XX7F'
    
    if 'WEB Development' in processed:
        return 'Le bhai LINK : https://youtube.com/playlist?list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w&si=PtGCiggURdqdb74n'
    
    if 'Python' in processed:
        return 'Le bhai LINK : https://youtube.com/playlist?list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT&si=XGPs3KlHDBNU5j4F'
    
    if 'C language' in processed:
        return 'Le bhai LINK : https://youtube.com/playlist?list=PL7ersPsTyYt3J6qL6DT_NOMv2sRsoK6Qd&si=FD5_L7yfzUFNfpTN'
    
    return 'Ye mere samajh ke bahar hai filhal'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('polling...')
    app.run_polling(poll_interval=3)
