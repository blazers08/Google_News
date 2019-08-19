FROM python:3
WORKDIR /home
COPY requirements.txt /home
COPY scrapy.cfg /home
RUN pip3 install -r requirements.txt
COPY googlenews ./googlenews
CMD scrapy crawl news_spider -o new.json
