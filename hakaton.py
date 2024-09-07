
employees = {
    "Тригуб":{
        "посада": "Data Analyst",
        "Коефіцієнт ефективності": 8,
        "проєкти": ["Mail List Clasterisation", "Positions Classification", "Rewiews Schedule"]
   },
    "Тимошенко":{
        "посада": "Geodata Technician",
        "Коефіцієнт ефективності": 7,
        "проєкти": ["Earth Scanning", "Streets Data Scrapping", "Qgis Drawing"]
   }
}


print("1. Список усіх працівників:")
for e in employees:
    print("-", e)


max_koef = 0
for e in employees:
    if employees[e]["Коефіцієнт ефективності"] > max_koef:
        max_koef = employees[e]["Коефіцієнт ефективності"]


print("2. Список найуспішнішик працівників, у яких коефіцієнт ефективності дорівнює", max_koef)
for e in employees:
    if employees[e]["Коефіцієнт ефективності"] == max_koef:
        print("-", e)


positions = []
for e in employees:
    if employees[e]["посада"] not in positions:
        positions.append(employees[e]["посада"])


print("3. Перелік усіх посад працівників")
for position in positions:
    print("-", position)
