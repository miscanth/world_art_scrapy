from itemadapter import ItemAdapter
from sqlalchemy import create_engine, Column, Date, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from scrapy.exceptions import DropItem


Base = declarative_base()

class Title(Base):
    __tablename__ = 'new_anime_review'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    year = Column(String())
    score = Column(Float(10,2)) # Column(FLOAT(precision=10, scale=2))
    genre = Column(String(400))
    link = Column(String())
    chat = Column(Integer())
    image_link = Column(String())

    def __str__(self):
        # При вызове функции print()
        # будут выводиться значение поля name.
        return f'{self.name}'


class AnimePipeline:
    def open_spider(self, spider):
        # Создание "движка" алхимии.
        engine = create_engine('sqlite:///sqlite.db')
        # Создание всех таблиц.
        Base.metadata.create_all(engine)
        # Создание сессии как атрибута объекта.
        self.session = Session(engine) 

    def process_item(self, item, spider):
        title = Title(
            name=item['name'],
            year=item['year'],
            score=item['score'],
            genre=', '.join(item['genre']),
            link=item['link'],
            chat=item['chat'],
            image_link=item['image_link']
        )
        # Добавление объекта в сессию и коммит сессии.
        self.session.add(title)
        self.session.commit()
        # Возвращаем item, чтобы обработка данных не прерывалась.
        return item 


    def close_spider(self, spider):
        self.session.close() 