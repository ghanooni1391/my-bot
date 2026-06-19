from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
import json
import os

TOKEN = "8508058245:AAHhAx8Ec5b8weLFpEfbbewQHMCECacbNzQ"
ADMIN_ID = 8964812956

def save_user(user_id):
    users = load_users()
    users.add(user_id)
    with open("users.json", "w") as f:
        json.dump(list(users), f)

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return set(json.load(f))
    return set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    save_user(user_id)
    keyboard = [
        [InlineKeyboardButton("🔋خرید اشتراک Open", callback_data="req1")],
        [InlineKeyboardButton("🔒خرید کدAvast", callback_data="req2")],
        [InlineKeyboardButton("🚀 خرید اشتراک v2ray", callback_data="req3")],
        [InlineKeyboardButton("🎁تست رایگان", callback_data="req4")],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")],
    ]
    await update.message.reply_text(
        "👋 سلام! به ربات فروش VPN خوش اومدی\nیه گزینه انتخاب کن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    back = [[InlineKeyboardButton("🔙 برگشت", callback_data="back")]]
    keyboard = [
        [InlineKeyboardButton("خرید اشتراک Open VPN", callback_data="req1")],
        [InlineKeyboardButton("🔒خرید کد Avast", callback_data="req2")],
        [InlineKeyboardButton("🚀کانفیگ ویتوری", callback_data="req3")],
        [InlineKeyboardButton("🎁است رایگان", callback_data="req4")],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")],
    ]

    if query.data == "req1":
        await query.edit_message_text(
            "🔋خرید اشتراک Open \nخرید اشتراک Open VPN،/nحجم: ۱۰ گیگ n\ [شماره کارت: ‌ ‌ ‌ ‌ ‌ ‌  6277601315605517 به نام محمدامین قانونی] \n رسید پرداخت را همین جا ارسال کنید🤝✅️ ‌\n\n هر امری بود همین جا در خدمتیم👇🫡",
            reply_markup=InlineKeyboardMarkup(back)
        )
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 اعلان!\n\n"
                 f"👤 نام: {user.first_name}\n"
                 f"🆔 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
                 f"🔢 آیدی: {user.id}\n\n"
                 f"خرید اشتراک Openرا انتخاب کرد!\n\n"
                 f"✏️ برای جواب:\n/reply {user.id} پیامت را بنویس"
        )

    elif query.data == "req2":
        await query.edit_message_text(
            "🔒خرید کد Avast\\nخرید کد فیلترشکن Avast \nیک ماهه \nنامحدود \n [شماره کارت:6277601315605517 به نام محمدامین قانونی] \n رسید پرداخت را همینجا ارسال کنید🤝✅️ \n\n هر امری بود همین جا👇در خدمتیم 🫡",
            reply_markup=InlineKeyboardMarkup(back)
        )
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 اعلان!\n\n"
                 f"👤 نام: {user.first_name}\n"
                 f"🆔 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
                 f"🔢 آیدی: {user.id}\n\n"
                 f"🔒خرید کد Avastرا انتخاب کرد!\n\n"
                 f"✏️ برای جواب:\n/reply {user.id} پیامت را بنویس"
        )

    elif query.data == "req3":
        await query.edit_message_text(
            "🚀کانفیگ ویتوری\n\nخرید اشتراک Vip ویتوری\n حجم ۱۰ گیگ \n100 هزار تومان\n [شماره کارت : ‌ ‌ ‌ 6277601315605517 به نام محمدامین قانونی]\n رسید پرداخت را همین جا ارسال کنید🤝✅️\n\n هر امری بود همین جا👇در خدمتیم🫡 ",
            reply_markup=InlineKeyboardMarkup(back)
        )
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 اعلان!\n\n"
                 f"👤 نام: {user.first_name}\n"
                 f"🆔 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
                 f"🔢 آیدی: {user.id}\n\n"
                 f"🚀کانفیگ ویتوری را انتخاب کرد!\n\n"
                 f"✏️ برای جواب:\n/reply {user.id} پیامت را بنویس"
        )

    elif query.data == "req4":
        await query.edit_message_text(
            "🎁تست رایگان\n\n📦جزئیات بسته \nحجم ۲گیگ\n به حضور ارسال می گردد\n\n هر امری بود همین جا👇در خدمتیم🫡",
            reply_markup=InlineKeyboardMarkup(back)
        )
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 اعلان!\n\n"
                 f"👤 نام: {user.first_name}\n"
                 f"🆔 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
                 f"🔢 آیدی: {user.id}\n\n"
                 f"تست رایگان را انتخاب کرد!\n\n"
                 f"✏️ برای جواب:\n/reply {user.id} پیامت را بنویس"
        )

    elif query.data == "support":
        await query.edit_message_text(
            "📞 پشتیبانی\n\nیوزرنیم: @Aminghanooni\n\n برید پی وی یا پیامتون رو همینجا بفرستید 👇'پشتیبانی ۲۴ ساعته🫡",
            reply_markup=InlineKeyboardMarkup(back)
        )

    elif query.data == "back":
        await query.edit_message_text(
            "👋 سلام! به ربات فروش vpn بروز خوش اومدی\nیه گزینه انتخاب کن:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def reply_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ فقط ادمین میتونه این دستور رو بزنه!")
        return
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ فرمت اشتباه!\n\n"
            "درست بنویس:\n"
            "/reply آیدی پیام\n\n"
            "مثال:\n"
            "/reply 123456789 سلام!"
        )
        return
    try:
        target_id = int(context.args[0])
        msg = " ".join(context.args[1:])
        await context.bot.send_message(
            chat_id=target_id,
            text=f"💬 پیام از پشتیبانی:\n\n{msg}"
        )
        await update.message.reply_text(f"✅ پیام به {target_id} ارسال شد!")
    except ValueError:
        await update.message.reply_text("❌ آیدی اشتباهه! باید عدد باشه")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا: {e}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    if user_id == ADMIN_ID:
        mode = context.user_data.get("broadcast")
        if mode:
            user_ids = list(load_users())
            count = 0
            for uid in user_ids:
                if uid == ADMIN_ID:
                    continue
                try:
                    if mode == "text" and update.message.text:
                        await context.bot.send_message(chat_id=uid, text=update.message.text)
                    elif mode == "photo" and update.message.photo:
                        await context.bot.send_photo(chat_id=uid,
                            photo=update.message.photo[-1].file_id,
                            caption=update.message.caption)
                    elif mode == "video" and update.message.video:
                        await context.bot.send_video(chat_id=uid,
                            video=update.message.video.file_id,
                            caption=update.message.caption)
                    elif mode == "file" and update.message.document:
                        await context.bot.send_document(chat_id=uid,
                            document=update.message.document.file_id,
                            caption=update.message.caption)
                    count += 1
                except:
                    pass
            context.user_data["broadcast"] = None
            await update.message.reply_text(f"✅ پیام به {count} نفر ارسال شد!")
            return

        await update.message.reply_text(
            "راهنما:\n\n"
            "💬 پیام به مشتری:\n"
            "/reply آیدی پیام\n\n"
            "مثال:\n"
            "/reply 123456789 سلام!\n\n"
            "📢 ارسال به همه:\n/send"
        )
        return

    save_user(user_id)
    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"📩 پیام جدید!\n\n"
                 f"👤 نام: {user.first_name}\n"
                 f"🆔 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
                 f"🔢 آیدی عددی: {user_id}\n\n"
                 f"──────────────\n"
                 f"✏️ برای جواب:\n/reply {user_id} پیامت را بنویس"
        )
        await update.message.forward(chat_id=ADMIN_ID)
        await update.message.reply_text("✅ پیامت دریافت شد! بزودی جواب میدیم 🙏")
    except Exception as e:
        print(f"خطا: {e}")

async def broadcast_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    keyboard = [
        [InlineKeyboardButton("📝 متن", callback_data="b_text")],
        [InlineKeyboardButton("🖼 عکس", callback_data="b_photo")],
        [InlineKeyboardButton("🎥 ویدئو", callback_data="b_video")],
        [InlineKeyboardButton("📁 فایل", callback_data="b_file")],
    ]
    await update.message.reply_text(
        "📢 چی میخوای برای همه بفرستی؟",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def broadcast_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    modes = {
        "b_text": ("text", "✏️ متنت را بنویس:"),
        "b_photo": ("photo", "🖼 عکس را بفرست:"),
        "b_video": ("video", "🎥 ویدئو را بفرست:"),
        "b_file": ("file", "📁 فایل را بفرست:"),
    }
    if query.data in modes:
        mode, msg = modes[query.data]
        context.user_data["broadcast"] = mode
        await query.edit_message_text(msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("send", broadcast_menu))
app.add_handler(CommandHandler("reply", reply_to_user))
app.add_handler(CallbackQueryHandler(broadcast_button, pattern="^b_"))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

print("✅ ربات روشن شد!")
app.run_polling()
