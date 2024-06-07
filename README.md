![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)  ![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


# Телеграмм-бот рекомендаций анимационных фильмов


## Описание проекта

В проекте реализован парсинг анимационных фильмов, а именно асинхронный парсер на базе специализированного фреймворка **Scrapy**. Результаты парсинга сохранятся в формате CSV и в БД SQLite (в планах перенести в PostgreSQL).

В парсере прописан единственный паук ***anime***. В его методах использованы CSS-селекторы.
В качестве домена для парсинга установлен *www.world-art.ru*.

При запуске паука ***anime*** парсер выводит csv-файл - выводится список анимационных фильмов: название, год выпуска, рейтинг, жанры, ссылка на основную страницу фильма, количество комментариев в чате-обсуждении.


## Используемые технологии:

- Scrapy
- SqlAlchemy
- python-telegram-bot
- SQLite
- PostgreSQL


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке: 
```
git clone git@github.com:miscanth/world_art_scrapy.git
```
Cоздать и активировать виртуальное окружение: 
```
python3.9 -m venv venv 
```
* Если у вас Linux/macOS 

    ```
    source env/bin/activate
    ```
* Если у вас windows 
 
    ```
    source env/scripts/activate 
    ```
```
python3.9 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить паука anime
```
scrapy crawl anime
```

Запустить телеграмv-бота
```
python3.9 main.py
```


## Разработчик (исполнитель):
👩🏼‍💻 Юлия: https://github.com/miscanth