from bs4 import BeautifulSoup
'''from lxml import etree
from lxml import html'''



'''with open('/Users/yoon/Downloads/web_scraping/home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)'''


with open('/Users/yoon/Downloads/web_scraping/home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.find_all('div',class_='card')

    for course in courses_cards:
        course_names = course.h5.text
        course_prices = course.a.text.split()[-1]
        print(f'{course_names} costs {course_prices}')