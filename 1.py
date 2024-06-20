from datetime import datetime


def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference_between_days = current_date - date_object
        return difference_between_days.days
    except:
        return 'Invalid format'


print(get_days_from_today('2020-10-09'))
