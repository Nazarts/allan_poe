from django.core.management.base import BaseCommand
from requests_html import HTMLSession
from threading import Thread


def crawler(url):
    with HTMLSession() as session:
        response = session.get(url)
    premiere = response.html.xpath('//div[@class="timestamp published-date padding-12-left"]')[0].text
    elements = response.html.xpath('//div[@class="article-content-container two-col-content-container"]/p')
    review = "".join([i.text for i in elements])
    image_source = response.html.xpath('//div[@class="partial lead-image"]//img/@src')[0]
    description = response.html.xpath('//h1[@class="headline heading-content"]')[0].text
    film_rev = dict(premiere=premiere, review=review, image_source=image_source)
    film_tags = ["genre", "performers", "director", "complete coverage"]
    tags = [i.text.lower() for i in response.html.xpath('//tbody/tr/td[1]')]
    count = 0
    for tag in tags:
        if tag in film_tags:
            if film_tags.index(tag) < 2:
                film_rev[tag] = [i.text for i in response.html.xpath(
                    f'//tbody[{tags.index(tag) + 1}]/tr/td/ul/li')]
            else:
                film_rev[tag] = response.html.xpath(f'//tbody[{tags.index(tag) + 1}]/tr/td/ul/li')[0].text

    print(film_rev)


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://ew.com/movie-reviews/2019/09/18/brad-pitt-ad-astra-review/'
        Thread(target=crawler, args=(url,)).start()
