from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp

TOKEN = '7202083219:AAEE3cNH1gMoM3vnGRq5fClyrE9DwjA3HBg'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Send me a social media link to download.')

async def download_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    await update.message.reply_text(f'Processing the link: {url}')
    await download_media(url, update)

async def download_media(url: str, update: Update) -> None:
    ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict)
        await update.message.reply_document(document=open(file_name, 'rb'))

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_link))

    application.run_polling()

if __name__ == '__main__':
    main()



'''    
      Interact with the breakpoint
send social media links to the bot vexdownloladerbot to test the download functionality


       Enhance the Bot
1.Add  support for other social media platforms:

2. Handle Errors and Edge cases:
Errors to manage invalid or unsupported links, handle differrent media types

3. Deploy bot

Servers like Heroku, AWS, Digital Ocean can host your bot

     Compliance and legal Considerations
1. Impliment rate limiting 
2. Comply with the terms and services and legal requirements of the social media platforms
'''
