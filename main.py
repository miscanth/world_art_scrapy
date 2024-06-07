import os
import telegram
from dotenv import load_dotenv
from world_art.pipelines import Title
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declared_attr, declarative_base



class TelegramErrorException(Exception):
    pass


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def send_message(bot, message: str) -> None:
    """Отправляет сообщение в Телеграм чат."""
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
    except telegram.error.TelegramError as error:
        raise TelegramErrorException(error)


def main():
    """Основная логика работы бота."""
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    engine = create_engine('sqlite:///sqlite.db', echo=False)
    session = Session(engine)

    all_titles = session.query(Title.name).all()[:5:]
    #first_title = str(session.query(Title).first())
    #message = [i.name for i in all_titles]
    # send_message(bot, message)
    for title in all_titles:
        send_message(bot, str(title[0]))
    # send_message(bot, first_title)
    # print(message)


if __name__ == '__main__':
    main()
