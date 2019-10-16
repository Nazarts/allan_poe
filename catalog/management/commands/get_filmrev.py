from django.core.management.base import BaseCommand
from datetime import datetime
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor
from catalog.models import FilmReview
from slugify import slugify
from requests import get
from lxml import etree


def crawler(url):
    with HTMLSession() as session:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
        response = session.get(url, headers=headers)
    premiere = response.html.xpath('//div[@class="timestamp published-date padding-12-left"]')[0].text.replace(",", " ")
    premiere = " ".join([i for i in premiere.split()[:3]])
    premiere = datetime.strptime(premiere, "%B %d %Y")
    review = response.html.xpath('//div[@class="article-content-container two-col-content-container"]/p')
    review = "<p>".join([i.text + "</p>" for i in review[:-1]])
    description = response.html.xpath('//h1[@class="headline heading-content"]')[0].text
    film_rev = dict(premiere=premiere, review=review, description=description, performers=[])
    film_tags = ["genre", "performers", "director", "complete coverage"]
    tags = [i.text.lower() for i in response.html.xpath('//tbody/tr/td[1]')]
    count = 0
    for tag in tags:
        if tag in film_tags:
            if film_tags.index(tag) < 2:
                film_rev[tag] = [i.text.replace(",", "") for i in response.html.xpath(
                    f'//tbody[{tags.index(tag) + 1}]/tr/td/ul/li')]
            else:
                film_rev[tag] = response.html.xpath(f'//tbody[{tags.index(tag) + 1}]/tr/td/ul/li')[0].text
    film_rev['name'] = film_rev.pop('complete coverage')
    film_rev['slug'] = slugify(film_rev['name'])
    try:
        image_source = response.html.xpath('//div[@class="partial lead-image"]//img/@src')[0]
        film_rev['image_source'] = image_source
        with HTMLSession() as session2:
            image_file = session2.get(image_source)
        image_name = "film_images/" + film_rev['slug'] + image_source[-4:]
        film_rev['image'] = image_name
        with open(f"media/{image_name}", "wb") as image:
            image.write(image_file.content)
        del image_file
    except Exception as ex:
        print(type(ex), ex)
        film_rev['images'] = "film_images/default.jpg"
    try:
        FilmReview.create(**film_rev)
        print("Success: ", url)
    except Exception as ex:
        print(type(ex), ex)
        return


def link_generator():
    for b in range(2, 9):
        for i in range(1, 24):
            temp = get(f'https://ew.com/sitemap.xml?yyyy=2018&mm=0{b}&dd={i}')
            chabo = 'https://ew.com/movies/'
            tree = etree.fromstring(temp.content)
            for i in tree:
                reference = i.getchildren()[0].text
                if chabo in reference:
                    yield reference


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = link_generator()
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(crawler, url)
