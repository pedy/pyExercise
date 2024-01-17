import json

class FilePipeline(): # The better approach for files is https://docs.scrapy.org/en/latest/topics/feed-exports.html
    output_file_name = 'fpl.json'

    def __init__(self):
        print(f'Initialized pipeline for file {self.output_file_name}')

    def process_item(self, item, spider):
        print('.', end='')
        for key in item: #Only one pair
            val = key
        #line = json.dumps(dict(item)) + "\n"
        self.file.write(val + '\n')
        return item
    
    def open_spider(self, spider):
        print('Openning spider')
        self.file = open(self.output_file_name, 'w')

    def close_spider(self, spider):
        print('\nClosing spider')
        self.file.close()
