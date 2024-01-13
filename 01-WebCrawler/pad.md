# URLs

URL prefix: `https://www.merriam-webster.com/wordfinder/classic/`

| Description | URL suffix |
|-|-|
| All 5 letter words starting with `a` - Page 1 | `begins/all/5/a/1`|
| All words starting with `a` - Page 1 | `begins/all/-1/a/1`|
| All 5 letter words starting with `a` - Page 2 | `begins/all/5/a/2`|
| Common 5 letter words starting with `a` - Page 1 | `begins/common/5/a/1`|

# Interactive?
`scarpy shell URL`

## Steps to my target case

```
$ scrapy shell 'https://www.merriam-webster.com/wordfinder/classic/begins/all/5/a/1'
...
>>> response.css('li.pb-4 > a::text').getall()
...
>>> response.css('label.btn:nth-child(2) > span:nth-child(1)::text').get()
'924'
>>> response.css('.d-block')
```

*Note: `all` has two pages for five letter words starting with 'a', while `common` does not. So I go with the extensive case. It's response would be an emtpy list:*
```
>>> response.css('.d-block')
[]
```


# DB
> You can also write an [item pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#topics-item-pipeline) to store the items in a database.


# PastePad
```python
>>> totalCount = response.css('label.btn:nth-child(2) > span:nth-child(1)::text').get()
>>> totalCount
'924'
# For those which are estimated, e.g. 21k in text,
>>> response.css('label.btn:nth-child(2) > span:nth-child(1)').attrib['title']
'924'
>>> words = []
>>> len(words)
0
>>> words += response.css('li.pb-4 > a::text').getall()
>>> len(words)
468
response.css('.next')
>>> response.css('.next > a').attrib['href']
'/wordfinder/classic/begins/all/5/a/2'
>>> siteURL = 'https://www.merriam-webster.com'
>>> fetch(siteURL + next)
>>> words += response.css('li.pb-4 > a::text').getall()
>>> len(words)
924
>>> len(words) == int(totalCount)
True
```