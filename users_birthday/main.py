from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)
       
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday_name = workday_name_for_date(birthday_this_year)
            birthdays[weekday_name].append(name)
    
    display_birthdays(birthdays)

def display_birthdays(birthdays):
    for birthday, users in birthdays.items():
        row = "{0:9}: {1}".format(birthday, ", ".join(users))
        print(row)


def workday_name_for_date(date):
     is_saturday = date.weekday() == 5
     is_sunday = date.weekday() == 6
     is_weekend = is_saturday or is_sunday
     weekday_name = date.strftime('%A')
     return weekday_name if not is_weekend else 'Monday'

if __name__ == "__main__":
    users = [{"name": "User 1", "birthday": datetime(1955, 2, 24)},
             {"name": "User 2", "birthday": datetime(1955, 2, 25)},
             {"name": "User 3", "birthday": datetime(1955, 2, 26)},
             {"name": "User 4", "birthday": datetime(1955, 2, 27)},
             {"name": "User 5", "birthday": datetime(1955, 2, 28)},
             {"name": "User 6", "birthday": datetime(1955, 3, 1)},
             {"name": "User 7", "birthday": datetime(1955, 3, 2)}]
    get_birthdays_per_week(users)