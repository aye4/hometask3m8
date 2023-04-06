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
