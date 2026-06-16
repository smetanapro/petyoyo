from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("lol")

app = Application.builder().token("8784246805:AAG_cf1zVqdekmNGCu6WgmojoWpJDJzKRoE").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()