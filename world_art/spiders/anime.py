import scrapy
from world_art.items import AnimeItem


ANIME_NUM_LIMIT = 200

class AnimeSpider(scrapy.Spider):
    name = "anime"
    allowed_domains = ["www.world-art.ru"]
    start_urls = ["http://www.world-art.ru/animation/"]

    def parse(self, response):
        anime_list_link = response.css('a:contains("полный список последних обновлений")::attr(href)').get()
        yield response.follow(anime_list_link, callback=self.parse_anime_list)

    def parse_anime_list(self, response):
        # td = response.css('td[size="14"]:contains("средний балл")')
        # anime_scores = response.css('font[size="14"] b::text')

        a_list = response.css('a.h3')
        for a in a_list:
            anime_name = a.css('a::text').get()
            anime_link = a.css('a::attr(href)').get()
            anime_year = a.css('a + font::text').get().replace(' г.)', '').replace('(', '')
            anime_id = anime_link.replace('animation.php?id=', '')
            yield response.follow(
                anime_link, callback=self.parse_anime_title, meta={
                     'name': anime_name, 'link': anime_link, 'year': anime_year, 'anime_id': anime_id
                })

        next_page = response.css('div.list_button a::attr(href)').get()
        num_limit = next_page.replace('list.php?limit_1=', '').replace('&sort=5', '')
        if int(num_limit) < ANIME_NUM_LIMIT:
            yield response.follow(next_page, callback=self.parse_anime_list)

    def parse_anime_title(self, response):
            name = response.meta.get('name')
            year = response.meta.get('year')
            score_string = response.css('td:contains("Средний балл") + td + td.review::text').get()
            score = int()
            link = response.meta.get('link')
            genre = response.css('td:contains("Жанр") + td + td.review a.review::text').getall()
            chat_string = response.css('a:contains("болталка")::attr(title)').get()
            chat = float()
            anime_id = response.meta.get('anime_id')
            if 12000 < int(anime_id) < 13000:
                image_link = f'http://www.world-art.ru/animation/img/13000/{anime_id}/1.jpg'
            if 11000 < int(anime_id) < 12000:
                image_link = f'http://www.world-art.ru/animation/img/12000/{anime_id}/1.jpg'
            if score_string is not None:
                 score = float(score_string.replace('\xa0из 10', ''))
            if chat_string is not None:
                 chat = int(chat_string.replace('постов в болталке этого аниме: ', ''))
            if score >= 7.0 or chat > 3:
                data = {
                    'name': name,
                    'year': year,
                    'score': score,
                    'genre': genre,
                    'link': self.start_urls[0] + link,
                    'chat': chat,
                    'image_link': image_link
                }
                yield AnimeItem(data)
