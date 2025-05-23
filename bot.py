
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7375363650:AAG1VYvYg4G4RB-w_0ugesTxnE1JZfgC6Mg"

# روابط الحلقات
EPISODES = {
    '1': 'https://t.me/c/1927164880/425',
     '2': 'https://t.me/c/1927164880/430',
    '3': 'https://t.me/c/1927164880/431',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': '',
    '10': ''
}

# إنشاء الأزرار حسب الصفحة
def get_episode_keyboard(page=1):
    ep_per_page = 5
    start = (page - 1) * ep_per_page + 1
    end = start + ep_per_page
    buttons = []

    for i in range(start, min(end, len(EPISODES)+1)):
        buttons.append([InlineKeyboardButton(f"📺 الحلقة {i}", callback_data=f"episode_{i}")])

    navigation = []
    if page > 1:
        navigation.append(InlineKeyboardButton("⬅️ السابق", callback_data=f"page_{page-1}"))
    if end <= len(EPISODES):
        navigation.append(InlineKeyboardButton("التالي ➡️", callback_data=f"page_{page+1}"))

    if navigation:
        buttons.append(navigation)

    return InlineKeyboardMarkup(buttons)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 اختر حلقة من القائمة:", reply_markup=get_episode_keyboard(page=1))

# الرد على الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("page_"):
        page = int(data.split("_")[1])
        await query.edit_message_text("📚 اختر حلقة من القائمة:", reply_markup=get_episode_keyboard(page))

    elif data.startswith("episode_"):
        ep_num = data.split("_")[1]
        link = EPISODES.get(ep_num, None)
        if link:
            await query.message.reply_text(f"🎬 *الحلقة {ep_num}:* {link}", parse_mode="Markdown")
        else:
            await query.message.reply_text("❌ الحلقة غير متوفرة.")

# تشغيل البوت
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
