from django.core.management.base import BaseCommand
from requests_html import HTMLSession
from threading import  Thread

def crawler(url):
    with HTMLSession() as session:
        response = session.get(url)
    name = response.html.xpath('//tbody[6]/tr/td/ul/li/a[1]')[0].text
    elements = response.html.xpath('//tbody[2]/tr/td/ul/li/a[1]')
    category = [i.text for i in elements]
    premiere = response.html.xpath('//div[@class="timestamp published-date padding-12-left"]')[0].text
    elements = response.html.xpath('//div[@class="article-content-container two-col-content-container"]/p')
    review = "".join([i.text for i in elements])
    image_source = response.html.xpath('//div[@class="partial lead-image"]//img/@src')[0]
    description = response.html.xpath('//h1[@class="headline heading-content"]')[0].text
    director = response.html.xpath('//tbody[3]/tr/td/ul/li/a[1]')[0].text
    elements = response.html.xpath('//tbody[4]/tr/td/ul/li/a[1]')
    characters = [i.text for i in elements]
    film_rev = dict(name=name, category=category, premiere=premiere, review=review, image_source=image_source,
                    description=description, director = director, characters = characters)
    print(film_rev)


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://ew.com/movie-reviews/2019/09/28/martin-scorsese-irishman-movie-review/'
        Thread(target=crawler, args=(url,)).start()
