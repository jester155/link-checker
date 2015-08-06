# link-checker

Used to find broken links on a website. This will report any link that is not a 404 or 302.

### Dependencies

* pip install scrapy
* If you still have trouble with getting scrapy to work you must install pywin32 for windows.
  * https://pypi.python.org/simple/pywin32/
* Be sure to add the proper paths to your environment variables
  * C:\Python27\Scripts - or the location you installed python to 

### Configuration

##### Open crawler_config.py and modify the settings accordingly.
- name -> the name of the spider
- allowed_domains -> the allowed domain names to be crawled. Anything that does not contain the domain name will not be crawled
- start_urls -> the urls to begin the crawl from

### Execution

`scrapy crawl 'my_crawler' -o output.json`

replace 'my_crawler'with the name specified in crawler_config.py
The output.json file will be placed in the spider folder.

