from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start, news_handler, price_handler, gabi
import config

if __name__ == '__main__':
    app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news_handler))
    app.add_handler(CommandHandler("price", price_handler))
    app.add_handler(CommandHandler("gabi", gabi))

    print("Bot is activate")
    app.run_polling()
