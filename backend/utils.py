from datetime import datetime
import requests
from bs4 import BeautifulSoup
from random import sample


def datetime_to_str(datetime_object):
    return datetime_object.strftime('%d/%m/%Y, %H:%M:%S')

def str_to_datetime(time_str):
    return datetime.strptime(time_str, '%d/%m/%Y, %H:%M:%S')

def order_projects(projects):
    topped_projects = [project for project in projects if project["isOnTop"]]
    untopped_projects = [project for project in projects if not project["isOnTop"]]
    
    topped_projects.sort(reverse=True, key=lambda project: str_to_datetime(project['isOnTopTime']))
    untopped_projects.sort(reverse=True, key=lambda project: str_to_datetime(project['createdTime']))

    return topped_projects + untopped_projects

def order_comments(comments):
    comments.sort(reverse=True, key=lambda comment: str_to_datetime(comment["createdTime"]))
    comments.sort(key=lambda comment: -comment["likedNum"])
    return comments

def get_top10_users(users):
    users.sort(key=lambda user: user["points"], reverse=True)
    return users[:10]


def get_news(major):
    major_list = ["CSE", "Business", "Medical", "Literature"]

    if major not in major_list:
        major = sample(major_list, 1)[0]
    
    if major == "CSE":
        url = 'https://www.nature.com/search?q=Computer%20Science&order=relevance&article_type=news&journal=nature&date_range=last_30_days'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        news_list = []
        for item in sample(soup.select('h2[role=heading]'), 5):
            news_list.append({
                "heading": item.getText().strip(),
                "href": "https://www.nature.com" + item.a['href']
            })
        return news_list

    elif major == "Business":
        url = "https://www.ft.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        news_list = []
        for item in sample(soup.select('a.js-teaser-heading-link'), 5):
            news_list.append({
                "heading": item.getText().strip(),
                "href": "https://www.ft.com" + item['href']
            })
        return news_list

    elif major == "Medical":
        url = "https://www.nature.com/search?q=Medical&order=relevance&article_type=news&journal=nature&date_range=last_30_days"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        news_list = []
        for item in sample(soup.select('h2[role=heading]'), 5):
            news_list.append({
                "heading": item.getText().strip(),
                "href": "https://www.nature.com" + item.a['href']
            })
        return news_list

    elif major == "Literature":
        url = "https://www.worldliteraturetoday.org/events-news"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        news_list = []
        for item in sample(soup.findAll("h3", {"class": "views-field-title"}), 5):
            news_list.append({
                "heading": item.getText().strip(),
                "href": item.a['href']
            })
        return news_list
