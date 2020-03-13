# encoding=utf-8
import re
import Crawler as crawler

urls = input('Welcome!\nEnter URL to crawl: ')  #input the URL
count = int(input('Max Count [e.g. 100]: '))  #input the maximum number
flag = int(input('Choose an algorithm [1.BFS  2.DFS]:'))  #indicate the preferred algorithm


def main(base_url, max_count, flag):
    craw = crawler.Crawler(base_url)
    craw.crawling(base_url, max_count, flag)


if __name__ == "__main__":
    main(urls , count, flag)
    print ("Mission accomplished! Thanks for using :)")
