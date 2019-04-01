import datetime
now = datetime.datetime.now()
if now.minute in (29, 59):
    print(f"The next bus leaves in {60-now.second} seconds.")
elif now.minute in (0, 30) and now.second == 0:
    print("The bus is here and leaves right now.")
elif now.minute < 30:
    print(f"The next bus leaves in {30-now.minute} minutes.")
else:
    print(f"The next bus leaves in {60-now.minute} minutes.")
