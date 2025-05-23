

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7375363650:AAG1VYvYg4G4RB-w_0ugesTxnE1JZfgC6Mg"

# ✅ file_id للفيديوهات (لن تُعرض للمستخدم)
VIDEO_IDS = {
    "miraculous_clip1": "https://t.me/c/1994244688/5972/6006",
    "miraculous_clip2": "https://t.me/c/1994244688/5972/6005",
    "adventure_clip1": "https://t.me/c/1994244688/5972/6008",
    "adventure_clip2": "https://t.me/c/1994244688/5972/6007",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🐞 مقتطف 1 من ميراكلوس", callback_data="miraculous_clip1")],
        [InlineKeyboardButton("🐞 مقتطف 2 من ميراكلوس", callback_data="miraculous_clip2")],
        [InlineKeyboardButton("⏰ مقتطف 1 من وقت المغامرة", callback_data="adventure_clip1")],
        [InlineKeyboardButton("⏰ مقتطف 2 من وقت المغامرة", callback_data="adventure_clip2")],
    ]
    await update.message.reply_text("🎬 اختر مقتطفاً للمشاهدة:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    video_id = VIDEO_IDS.get(query.data)
    if video_id:
        await query.message.reply_video(video_id)
    else:
        await query.message.reply_text("❌ المقطع غير متوفر حالياً.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
