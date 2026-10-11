import datetime
d_eng = datetime.date(2026,10,20)
d_launch = datetime.date(2026,11,15)
print("20 Oct 2026 weekday:", d_eng.strftime("%A"))
print("15 Nov 2026 weekday:", d_launch.strftime("%A"))
print("calendar days 20 Oct to 15 Nov:", (d_launch-d_eng).days)
print("calendar weeks:", round((d_launch-d_eng).days/7,2))
wd=0; dd=d_eng
while dd<=d_launch:
    if dd.weekday()<5: wd+=1
    dd+=datetime.timedelta(days=1)
print("working days incl:", wd, "=", round(wd/5,2),"eng-weeks per engineer")
print("Fri 13 Nov weekday:", datetime.date(2026,11,13).strftime("%A"))
print("sum all est:", 3+2+1+2)
print("PRD must-haves SSO+audit+admin:", 3+2+1)
print("audit+admin only:", 2+1)
print("audit+admin+dashboard:", 2+1+2)
