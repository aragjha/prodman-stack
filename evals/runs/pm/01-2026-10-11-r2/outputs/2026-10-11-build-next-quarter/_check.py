from datetime import date, timedelta
seats = dict(A=4, B=11, C=6, D=2, E=9, F=15)
print("seat total:", sum(seats.values()))
print("max firm:", max(seats, key=seats.get), max(seats.values()))
print("min firm:", min(seats, key=seats.get), min(seats.values()))
direct = ["A", "E", "F"]; adjacent = ["B", "C"]; touch = ["A", "B", "C", "E", "F"]
print("direct reminders:", len(direct), direct)
print("adjacent:", len(adjacent), adjacent)
print("touch chasing problem:", len(touch), touch)
d = date(2026, 10, 11); p = d + timedelta(days=14)
print("today:", d.strftime("%A"), d.isoformat())
print("plus 14 days:", p.strftime("%A"), p.isoformat())
