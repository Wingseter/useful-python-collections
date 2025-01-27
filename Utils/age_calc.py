import datetime

birth_day = datetime.date(1997, 1, 16)
now_time = datetime.date.today()

final_answer = 0

year_compare = now_time.year - birth_day.year
month_compare = now_time.month - birth_day.month
day_compare = now_time.day - birth_day.day

if month_compare < 0 or (month_compare == 0 and day_compare < 0): # birthday not pass
    final_answer = year_compare
else:
    final_answer = year_compare - 1

korean_age = year_compare + 1

print("당신의 현재 만 나이는 ", final_answer)
print("당신의 현재 한국 나이는 ", korean_age)