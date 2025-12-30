from telegram import Update
from telegram.ext import ContextTypes
from service import get_news_api, current_price
import config


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')


async def news_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    content = get_news_api(config.NEWS_API_KEY)
    await update.message.reply_text(content, parse_mode='Markdown')


async def price_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please enter a ticker symbol after the command.\n"
                                        "Example: `/price BTC-USD` or `/price TSLA`")
    ticker = context.args[0].upper()
    result = current_price(ticker)
    await update.message.reply_text(result)

.



