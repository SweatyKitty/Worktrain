from fastapi import FastAPI
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = FastAPI()

# Telegram bot token
TOKEN = "YOUR_BOT_TOKEN"

# Initialize bot
bot = ApplicationBuilder().token(TOKEN).build()

@app.get("/")
async def root():
    return {"message": "Telegram Mini App is running"}

# Telegram command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to our Telegram Mini App!")

# Add command handler to bot
bot.add_handler(CommandHandler("start", start))

# Run bot polling in the background
@app.on_event("startup")
async def startup_event():
    await bot.initialize()
    await bot.start()

@app.on_event("shutdown")
async def shutdown_event():
    await bot.stop()