from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7375363650:AAG1VYvYg4G4RB-w_0ugesTxnE1JZfgC6Mg"

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
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    choice = query.data

    if choice == 'episodes':
        episodes_text = (
            "📺 *قائمة الحلقات:*\n"
            "1️⃣ [الحلقة 1](https://t.me/c/1927164880/431)\n"
            "2️⃣ [الحلقة 2](https://t.me/c/1927164880/430)\n"
            "3️⃣ [الحلقة 3](https://t.me/c/1927164880/425)\n"
        )
        await query.edit_message_text(episodes_text, parse_mode="Markdown")
    
    elif choice == 'movies':
        await query.edit_message_text("🎬 هذه قائمة الأفلام...")

    elif choice == 'cartoons':
        await query.edit_message_text("👶 هذه قائمة الكرتون...")
