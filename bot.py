from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

episodes = [
    "الحلقة 1: مقدمة عن التكنولوجيا",
    "الحلقة 2: تطور الهواتف الذكية",
    "الحلقة 3: تأثير الإنترنت على الحياة اليومية",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا! أرسل /episode رقم_الحلقة للحصول على الحلقة المطلوبة.\nمثال: /episode 1"
    )

async def episode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        num = int(context.args[0])
        if 1 <= num <= len(episodes):
            await update.message.reply_text(episodes[num - 1])
        else:
            await update.message.reply_text("عذرًا، رقم الحلقة غير موجود.")
    except (IndexError, ValueError):
        await update.message.reply_text("يرجى إرسال رقم الحلقة بعد الأمر، مثل: /episode 2")

def main():
    TOKEN = "7375363650:AAG1VYvYg4G4RB-w_0ugesTxnE1JZfgC6Mg"  # استبدل هنا بالتوكن الحقيقي

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("episode", episode))

    app.run_polling()

if __name__ == '__main__':
    main()
