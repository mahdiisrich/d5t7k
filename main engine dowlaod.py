import telebot
from pytube import YouTube
import os

bot = telebot.TeleBot(os.getenv("6069842275:AAEAttFjSqCgjOQrHB0eqCLLTIfLogXRGP8"))
URL = os.getenv("URL")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! Welcome to the YouTube Video Downloader bot. Send me a YouTube video link to get started.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        bot.reply_to(message, "Processing your request...")

        youtube_link = message.text
        yt = YouTube(youtube_link)

        bot.reply_to(message, "Step 1: Video found. Downloading...")
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(filename='video')

        bot.reply_to(message, "Step 2: Uploading to Telegram...")
        with open('video.mp4', 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        bot.reply_to(message, "Step 3: Download complete! The video has been sent to you.")

        os.remove('video.mp4')  # Remove the temporary video file

    except Exception as e:
        bot.reply_to(message, "Sorry, an error occurred while processing your request. Please make sure the YouTube link is valid.")

bot.polling()
