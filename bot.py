from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "ضع_توكن_البوت_هنا"

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📺 حلقات", callback_data='episodes')],
        [InlineKeyboardButton("🎬 أفلام", callback_data='movies')],
        [InlineKeyboardButton("📚 وثائقيات", callback_data='documentaries')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("ماذا تود مشاهدة؟ 👇", reply_markup=reply_markup)

# دالة استقبال الرد
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    choice = query.data
    if choice == 'episodes':
        await query.edit_message_text("🟢 هذه قائمة الحلقات...")
    elif choice == 'movies':
        await query.edit_message_text("🟢 هذه قائمة الأفلام...")
    elif choice == 'documentaries':
        await query.edit_message_text("🟢 هذه قائمة الوثائقيات...")

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()
