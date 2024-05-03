response = ...
quotes = response.css('div.quote')
quotes[0].css('small')

# В первом элементе списка quote есть два тега span.
# Метод get() возьмёт только первый из них и напечатает его в виде строки:
quotes[0].css('span').get()
# А чтобы извлечь из тега текст - надо дописать к селектору ::text
quotes[0].css('span::text').get()
# Из первого элемента списка quotes получаем все теги <span>
# и выводим их код в виде списка строк.
quotes[0].css('span').getall()
# Точно так же из всех элементов <span> в quotes[0] 
# получаем текст.
quotes[0].css('span::text').getall()

# Чтобы собрать со страницы все теги с атрибутом class="author", указывают имя класса после точки
response.css('.author')
# XPath-селектор для тех же элементов.
# В качестве обозначения любого тега ставится звёздочка.
response.xpath('//*[@class="author"]')
# Найти все ссылки, вложенные в элемент с классом quote
response.css('.quote a')

# конструкция [@key="value"] позволяет найти элемент с атрибутом key, значение которого равно value. 
# селектор найдёт на странице все теги ссылок, ведущих на страницу https://ya.ru/
response.xpath('//a[@href="https://ya.ru/"]')

# Пример поиска авторов, 
# в имени которых есть заглавная буква "E".
# . — «в тексте, который содержится в теге»
response.xpath('//small[contains(., "E")]/text()').getall()
# Подобный поиск можно провести и с помощью CSS-селектора:
response.css('small:contains("E")::text').getall()

response.css('div.quote').xpath('//small').get()
# Перевод: во всех элементах <div class="quote"> на странице найти элементы <small> 
# и получить в виде строки первый <small> из найденных.
'<small class="author" itemprop="author">Albert Einstein</small>'

# для аргумента for
response.css('label[for=id_username]')
response.css('.card-body form div.form-group:nth-of-type(1) label::text').get()

 # По CSS-селектору ищем ссылку на следующую страницу.
next_page = response.css('li.next a::attr(href)').get()
if next_page is not None:
    # Если ссылка нашлась, загружаем страницу по ссылке
    # и вызываем метод parse() ещё раз.
    yield response.follow(next_page, callback=self.parse)
"""<li class="next">
  <a href="/page/2/">Next <span aria-hidden="true">→</span></a>
</li>"""
#Для поиска ссылки на следующую страницу подойдёт такой селектор:
response.xpath("//a[contains(., 'Следующая')]/@href").get()