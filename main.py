import telebot
from telebot import types
from faker import Faker
import random

# 1. التوكن الخاص بك
TOKEN = "2145056561:AAGvUbzKQ1pq9gqTQoK4bkPs9h-QoBEqiD8"
bot = telebot.TeleBot(TOKEN)
fake = Faker()

# 2. القائمة البيضاء (المصرح لهم فقط)
ALLOWED_USERS = [2041946334, 6485711685, 8549227762]

# --- بيانات الدول ---
PH_DATA = [
    {"city": "Manila", "zip": "1000", "province": "Metro Manila", "streets": ["Roxas Blvd", "Taft Ave", "Escolta St", "Padre Faura St"]},
    {"city": "Makati City", "zip": "1200", "province": "Metro Manila", "streets": ["Ayala Ave", "Paseo de Roxas", "Makati Ave", "Sen. Gil Puyat Ave"]},
    {"city": "Quezon City", "zip": "1100", "province": "Metro Manila", "streets": ["Tomas Morato Ave", "Katipunan Ave", "Commonwealth Ave", "Timog Ave"]},
    {"city": "Cebu City", "zip": "6000", "province": "Cebu", "streets": ["Colon St", "Osmeña Blvd", "Mango Ave", "Gorordo Ave"]},
]

UKRAINE_DATA = [
    {"city": "Kyiv", "zip": "01001", "streets": ["Khreshchatyk St", "Volodymyrska St", "Velyka Vasylkivska St"]},
    {"city": "Lviv", "zip": "79000", "streets": ["Svobody Ave", "Halytska St", "Kopernyka St"]},
    {"city": "Odesa", "zip": "65000", "streets": ["Deribasivska St", "Rishyelievska St", "Pushkinska St"]},
]

# بيانات سويسرا المضافة (شوارع حقيقية)
CH_DATA = [
    {"city": "Zurich", "zip": "8001", "streets": ["Bahnhofstrasse", "Niederdorfstrasse", "Limmatquai"]},
    {"city": "Geneva", "zip": "1201", "streets": ["Rue du Rhône", "Rue de la Croix-d'Or", "Rue du Mont-Blanc"]},
    {"city": "Bern", "zip": "3011", "streets": ["Kramgasse", "Marktgasse", "Spitalgasse"]},
    {"city": "Basel", "zip": "4051", "streets": ["Freie Strasse", "Gerbergasse", "Steinenvorstadt"]}
]

# --- دوال توليد البيانات ---
def generate_ph_data():
    full_name = f"{fake.first_name()} {fake.first_name()} {fake.last_name()}"
    loc = random.choice(PH_DATA)
    prefixes = ['917', '918', '919', '920', '921', '922', '977', '998']
    # تم حذف 63
    phone = f"{random.choice(prefixes)}{''.join([str(random.randint(0,9)) for _ in range(7)])}"
    clean_name = full_name.lower().replace(" ", "")
    email = f"{clean_name}{random.randint(10, 99)}@gmail.com"
    street = random.choice(loc['streets'])
    house_num = random.randint(1, 300)

    return (f"🇵🇭 *بيانات PayPal (الفلبين)*\n"
            f"━━━━━━━━━━━━━━━\n"
            f"👤 *Full Name:* `{full_name}`\n"
            f"🏠 *Address:* `{house_num} {street}, {loc['city']}, {loc['province']}, {loc['zip']}, Philippines`\n"
            f"🏙️ *City:* `{loc['city']}`\n"
            f"📮 *Zip Code:* `{loc['zip']}`\n"
            f"📞 *Phone:* `{phone}`\n"
            f"📧 *Gmail:* `{email}`\n"
            f"🔑 *Password:* `123@123@`\n"
            f"━━━━━━━━━━━━━━━")

def generate_ua_data():
    full_name = f"{fake.first_name()} {fake.first_name()} {fake.last_name()}"
    loc = random.choice(UKRAINE_DATA)
    operators = ['50', '66', '95', '67', '68', '63', '73', '93']
    # تم حذف 380
    phone = f"{random.choice(operators)}{''.join([str(random.randint(0,9)) for _ in range(7)])}"
    clean_name = full_name.lower().replace(" ", "")
    email = f"{clean_name}{random.randint(10, 99)}@gmail.com"
    street = random.choice(loc['streets'])
    house_num = random.randint(1, 150)

    return (f"💳 *بيانات PayPal (أوكرانيا)*\n"
            f"━━━━━━━━━━━━━━━\n"
            f"👤 *Full Name:* `{full_name}`\n"
            f"🏠 *Address:* `{house_num} {street}, {loc['city']}, {loc['zip']}, Ukraine`\n"
            f"🏙️ *City:* `{loc['city']}`\n"
            f"📮 *Zip Code:* `{loc['zip']}`\n"
            f"📞 *Phone:* `{phone}`\n"
            f"📧 *Gmail:* `{email}`\n"
            f"🔑 *Password:* `123@123@`\n"
            f"━━━━━━━━━━━━━━━")

def generate_ch_data():
    full_name = f"{fake.first_name()} {fake.first_name()} {fake.last_name()}"
    loc = random.choice(CH_DATA)
    # مفاتيح الهواتف السويسرية المحمولة
    operators = ['75', '76', '77', '78', '79']
    # تم حذف 41
    phone = f"{random.choice(operators)}{''.join([str(random.randint(0,9)) for _ in range(7)])}"
    clean_name = full_name.lower().replace(" ", "")
    # تم تغيير النطاق إلى جيميل
    email = f"{clean_name}{random.randint(10, 99)}@gmail.com"
    street = random.choice(loc['streets'])
    house_num = random.randint(1, 150)

    # تنسيق العنوان السويسري المعتاد (الشارع الرقم، الرمز البريدي المدينة)
    return (f"🇨🇭 *بيانات PayPal (سويسرا)*\n"
            f"━━━━━━━━━━━━━━━\n"
            f"👤 *Full Name:* `{full_name}`\n"
            f"🏠 *Address:* `{street} {house_num}, {loc['zip']} {loc['city']}, Switzerland`\n"
            f"🏙️ *City:* `{loc['city']}`\n"
            f"📮 *Zip Code:* `{loc['zip']}`\n"
            f"📞 *Phone:* `{phone}`\n"
            f"📧 *Gmail:* `{email}`\n"
            f"🔑 *Password:* `123@123@`\n"
            f"━━━━━━━━━━━━━━━")

# --- لوحة الأزرار ---
def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🇵🇭 الفلبين", callback_data="gen_ph")
    btn2 = types.InlineKeyboardButton("🇺🇦 أوكرانيا", callback_data="gen_ua")
    btn3 = types.InlineKeyboardButton("🇨🇭 سويسرا", callback_data="gen_ch")
    # تم ترتيب الأزرار ليكون شكلها متناسقاً
    markup.row(btn1, btn2)
    markup.row(btn3)
    return markup

# --- معالجة الأوامر ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id not in ALLOWED_USERS:
        bot.reply_to(message, "❌ نعتذر، البوت خاص ولا يمكنك استخدامه.")
        return
    bot.send_message(message.chat.id, "👋 أهلاً بك! إختر الدولة من الأسفل:", reply_markup=main_menu_keyboard())

@bot.message_handler(commands=['id'])
def send_id(message):
    bot.reply_to(message, f"المعرف الخاص بك (User ID) هو:\n`{message.from_user.id}`", parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "📖 *دليل الاستخدام:*\n"
        "1. استخدم /start لفتح قائمة الدول.\n"
        "2. اضغط على الدولة لتوليد بيانات PayPal وهمية.\n"
        "3. يمكنك الضغط على 'توليد جديد' للحصول على بيانات أخرى فوراً.\n\n"
        "⚠️ البوت يعمل فقط للأشخاص المضافين للقائمة البيضاء."
    )
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# --- معالجة الضغط على الأزرار ---
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.from_user.id not in ALLOWED_USERS:
        bot.answer_callback_query(call.id, "❌ ليس لديك صلاحية!", show_alert=True)
        return

    if call.data == "main_menu":
        bot.edit_message_text("👋 أهلاً بك! إختر الدولة:", call.message.chat.id, call.message.message_id, reply_markup=main_menu_keyboard())
    
    elif call.data == "gen_ph":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔄 توليد جديد (🇵🇭)", callback_data="gen_ph"))
        markup.add(types.InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text(generate_ph_data(), call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "gen_ua":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔄 توليد جديد (🇺🇦)", callback_data="gen_ua"))
        markup.add(types.InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text(generate_ua_data(), call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

    elif call.data == "gen_ch":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔄 توليد جديد (🇨🇭)", callback_data="gen_ch"))
        markup.add(types.InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu"))
        bot.edit_message_text(generate_ch_data(), call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

# تشغيل البوت
print("✅ البوت يعمل الآن وتمت إضافة دولة سويسرا ببريد جيميل")
bot.infinity_polling()
