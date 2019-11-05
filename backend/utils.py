from datetime import datetime

def datetime_to_str(datetime_object):
    return datetime_object.strftime('%d/%m/%Y, %H:%M:%S')

def str_to_datetime(time_str):
    return datetime.strptime(time_str, '%d/%m/%Y, %H:%M:%S')

def order_projects(projects):
    topped_projects = [project for project in projects if project["isOnTop"]]
    untopped_projects = [project for project in projects if not project["isOnTop"]]
    
    topped_projects.sort(key=lambda project: str_to_datetime(project['isOnTopTime']))
    untopped_projects.sort(key=lambda project: str_to_datetime(project['createdTime']))

    return topped_projects + untopped_projects


def get_top10_users(users):
    users.sort(key=lambda user: user["points"], reverse=True)
    return users[:10]