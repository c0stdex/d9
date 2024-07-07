# main.py
import subprocess

subprocess.run(['scrapy', 'crawl', 'quotes', '-o', 'quotes.json'])
