def find_next_monday():
    today = datetime.date.today()
    if (today.weekday() == 0):
        return today
    else:
        for d in range(7):
            day = today +datetime.timedelta(days=d)
            if (day.weekday() == 0):
                return day