from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7375363650:AAG1VYvYg4G4RB-w_0ugesTxnE1JZfgC6Mg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """👋 أهلاً!

قناة البوت: https://t.me/alfarabic (انضم)
القناة الثانية: https://t.me/alfaic1 (انضم)
✅ مالك البوت:@Yaaaaafkk / @Beem_0 """

    keyboard = [
        [InlineKeyboardButton("⏯️ كيفية استخدام البوت للمشاهدة", callback_data="how_to_use")],
        [InlineKeyboardButton("🎬 أفلام ميراكلوس", callback_data="movies")],
        [InlineKeyboardButton("🎞️ حلقات خاصة", callback_data="special")],
        [InlineKeyboardButton("📺 مواسم", callback_data="seasons")],
    ]

    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "how_to_use":
        await query.message.reply_text("🎥 فقط اختر القسم المطلوب، وسيظهر لك الفيديو.\n✅ لا تنس الانضمام إلى القنوات.")
    elif query.data == "movies":
        await query.message.reply_text("🎬 قائمة أفلام ميراكلوس (قريباً).")
    elif query.data == "special":
        await query.message.reply_text("🎞️ حلقات خاصة (قريباً).")
    elif query.data == "seasons":
        await query.message.reply_text("📺 المواسم: \n1- الموسم الأول\n2- الموسم الثاني...\n(قريباً)")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("menu", start))
    from telegram.ext import CallbackQueryHandler
...
app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
