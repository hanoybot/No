from flask import Flask, render_template
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Flask(__name__)

# معلومات البوت
TOKEN = '8165540566:AAGXlo_1ljb6IkAG8jj7BjZdxwfJQhub96o'
bot = telebot.TeleBot(TOKEN)

# صفحة HTML لعرض الكاميرا
@app.route('/camera')
def camera():
    # نمرر رابط الكاميرا بناءً على المعامل في الرابط
    mode = request.args.get('mode', 'user')  # Default to front camera
    return render_template('camera.html', mode=mode)

# إعدادات البوت
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    
    button_front_camera = InlineKeyboardButton("الكاميرا الأمامية", url="http://localhost:5000/camera?mode=user")
    button_back_camera = InlineKeyboardButton("الكاميرا الخلفية", url="http://localhost:5000/camera?mode=environment")
    button_start = InlineKeyboardButton("ابدأ الآن", url="https://google.com")
    
    markup.row(button_front_camera, button_back_camera)
    markup.add(button_start)
    
    bot.send_message(message.chat.id, "مرحبًا! اختر الكاميرا التي تريد استخدامها أو ابدأ الآن:", reply_markup=markup)

# تشغيل البوت
def run_bot():
    bot.polling()

if __name__ == '__main__':
    from threading import Thread
    # تشغيل البوت في خيط منفصل
    bot_thread = Thread(target=run_bot)
    bot_thread.start()
    
    # تشغيل تطبيق Flask
    app.run(debug=True, host='0.0.0.0', port=5000)