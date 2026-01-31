from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# TOKEN נשאב מה-Environment Variable שהכנסת ב-Railway
TOKEN = os.getenv("BOT_TOKEN")

# זה ה-ID שלך בטלגרם – אתה צריך לשים את המספר שלך כאן
OWNER_ID = 587596950 # <- החלף את זה ב-ID שלך (מ-@userinfobot)

# פונקציה שמקבלת הודעות ממשתמשים ושולחת אליך לפלאפון
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"📩 פנייה חדשה:\nמזהה: {user.id}\nשם משתמש: {user.username}\nהודעה:\n{text}"
    )

# פונקציה שתאפשר לך לענות למשתמשים מהפלאפון
async def reply_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = int(context.args[0])
        reply_text = " ".join(context.args[1:])
        await context.bot.send_message(chat_id=user_id, text=reply_text)
    except:
        await update.message.reply_text("שגיאה בפורמט. השתמש: /reply user_id הודעה")

# בניית האפליקציה
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.COMMAND, reply_to_user))

# הרצה
app.run_polling()
