# coding=UTF-8
import scrapy

class NEWSpider(scrapy.Spider):
    name = "news_spider"

    def start_requests(self):        
        urls = ['https://news.google.com/?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(50):
            title = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/h3/a/text()').extract_first()
            source = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/div[2]/div/a/text()').extract_first()
            
            source_url = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/h3/a/@href').extract_first()
            source_time = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/div[2]/div/time/@datetime').extract_first()

            new_source_url = str(source_url).replace('.','https://news.google.com')

            related_title = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[2]/div/div[1]/article['+str(i)+']/h4/text()').extract()
            related_source = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[2]/div/div[1]/article['+str(i)+']/div[2]/div/a/text()').extract()
            related_source_url = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[2]/div/div[1]/article['+str(i)+']/div[2]/div/a/@href').extract()
            related_time = response.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[2]/div/div[1]/article[2]/div['+str(i)+']/div/time/@datetime').extract_first()
            
            related_new_source_url = str(related_source_url).replace('.','https://news.google.com')
            
            if title:
                # print(title)
                # print(source)
                # print(new_source_url)
                # print(source_time)
                newsdict = {'News_Title':title, 'News_source':source, 'News_source_url':new_source_url, 'News_source_time':source_time}
                yield newsdict

            if related_title:
                # print(related_title)
                # print(related_source)
                # print(related_new_source_url)
                # print(related_time)
                newsdict_1 = {'News_Title':related_title, 'News_source':related_source, 'News_source_url':related_new_source_url, 'News_source_time':related_time}
                yield newsdict

