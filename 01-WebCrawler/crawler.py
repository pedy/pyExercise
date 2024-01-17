from scrapy.crawler import CrawlerProcess
from wordsSpider import WordsSpider
from filePipeline import FilePipeline

if __name__ == "__main__":
    process = CrawlerProcess({
        # https://docs.scrapy.org/en/latest/topics/settings.html#topics-settings-ref
        'LOG_LEVEL': 'ERROR',
        'ITEM_PIPELINES':{
            FilePipeline: 300,
        }
    })
    process.crawl(WordsSpider)
    process.start()
