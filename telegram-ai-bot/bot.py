
# initialize bot
def main():
    updater = Updater(token=API_KEY, use_context=True)
    up = updater.dispatcher

    # Command handlers
    up.add_handler(CommandHandler('tip', send_ai_generated_tips))
    dp.add_handler(CommandHandler('feedback', collect_feedback))
    dp.add_handler(CommandHandler('update', send_product_updates))


    #start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
