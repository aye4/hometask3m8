from datetime import datetime, timedelta


def get_birthdays_per_week(users: list):
    cur_date = datetime.now()
    d = cur_date
    x = timedelta(days=1)
    # shift the starting date if weekend should be included
    if not d.weekday():
        d -= x
    if d.weekday() == 6:
        d -= x
    # list of dates for a week
    cur_week = {}
    for i in range(7):
        z = d.weekday()
        cur_week[str(d.date())[4:]] = (
            i if z < 5 else i + 7 - z,
            "Monday" if z >= 5 else d.strftime("%A"),
        )
        d += x
    # check the birthdays
    bd_list = {}
    for u in users:
        x = str(u["birthday"].date())[4:]
        if x in cur_week:
            bd_list.setdefault(cur_week[x][1], []).append(u["name"])
    # output
    if bd_list:
        for x, y in sorted(set(cur_week.values())):
            if y in bd_list:
                print(f"{y}: {', '.join(sorted(bd_list[y]))}")
    else:
        print("No birthdays this week")


test_users = [
    {'name':'April4', 'birthday':datetime(year=1999, month=4, day=4)},
    {'name':'April5', 'birthday':datetime(year=1999, month=4, day=5)},
    {'name':'April6', 'birthday':datetime(year=1999, month=4, day=6)},
    {'name':'April7', 'birthday':datetime(year=1999, month=4, day=7)},
    {'name':'April8', 'birthday':datetime(year=1999, month=4, day=8)},
    {'name':'April9', 'birthday':datetime(year=1999, month=4, day=9)},
    {'name':'April10', 'birthday':datetime(year=1999, month=4, day=10)},
    {'name':'April11', 'birthday':datetime(year=1999, month=4, day=11)},
    {'name':'April12', 'birthday':datetime(year=1999, month=4, day=12)},
    {'name':'April13', 'birthday':datetime(year=1999, month=4, day=13)},
    {'name':'April14', 'birthday':datetime(year=1999, month=4, day=14)},
    {'name':'April15', 'birthday':datetime(year=1999, month=4, day=15)},
    {'name':'April16', 'birthday':datetime(year=1999, month=4, day=16)},
]
get_birthdays_per_week(test_users)