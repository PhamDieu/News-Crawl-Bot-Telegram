from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

#get news thehackernews:
# def get_news():
#     list_news = []
#     r = requests.get("https://thehackernews.com/")
#     soup = BeautifulSoup(r.text, 'html.parser')
#     mydivs = soup.find_all("div", {"class": "body-post clear"})
#
#     for new in mydivs:
#         newdict = {}
#         newdict["link"] = new.a.get("href")
#         list_news.append(newdict)
#
#     return list_news
#
#Get news Securityonline.info:
def getnews2():
    list_news2 = []
    r = requests.get("https://securityonline.info/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs2 = soup.find_all("h2", {"class": "post-title entry-title"})

    for new in mydivs2:
        newdict2 = {}
        newdict2["link"] = new.a.get("href")
        list_news2.append(newdict2)
    return list_news2
#
#Get time of news2 Securityonline.info:
def get_time_news2():    # thời gian được lấy theo đúng thứ tự của các news trong news2
    list_time2 = []
    r = requests.get("https://securityonline.info/")
    soup = BeautifulSoup(r.text, 'html.parser')
    time2 = soup.find_all("p", {"class": "post-date"})

    for new in time2:
        newtime2 = {}
        newtime2["time"] = new.time.get("datetime")
        list_time2.append(newtime2)
    return list_time2
#
# Các function :
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   #function
    await update.message.reply_text(f'Xin chào {update.effective_user.first_name}')
#
#
async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   # xem command
    strcommand = "/news : lấy news từ thehackernews[.]com" + "\n" + "/news2 : lấy news từ Securityonline[.]info" + "\n" + "/timenews2 : lấy time của news2"
    await update.message.reply_text(f'{strcommand}')
#
#
# async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:   #function news
#     data = get_news()
#     str1 = ""
#
#     for item in data:
#       str1 += "-" + item["link"] + "\n"
#     await update.message.reply_text(f'{str1}')
#
#
async def news2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  #function news2
    data = getnews2()

    for item2 in data:  await update.message.reply_text(f'{item2["link"]}')
#
#
async def timenews2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  #function timenews2
    data = get_time_news2()
    str1time= ""

    for item in data:
        str1time += "-" + item["time"] + "\n"
    await update.message.reply_text(f'{str1time}')
#
#
app = ApplicationBuilder().token("5570847525:AAEsKs_m3aRGMQeJHYBw7iM2QkcCEZkLvMg").build()    #key api bot
app.add_handler(CommandHandler("hello", hello))    #keyword call function
app.add_handler(CommandHandler("command", command))
#app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("news2", news2))
app.add_handler(CommandHandler("timenews2", timenews2))
app.run_polling()

