continent = {
    'Євразія': 54440000,
    'Африка': 30370000,
    'Північна Америка': 24709000,
    'Південна Америка': 17840000,
    'Австралія': 8600000,
    'Антарктида': 14000000
}

sortcont = dict(sorted(continent.items(), key=lambda item: item[1], reverse=True))

print("Континенти в порядку спадання площі:")
for continent, area in sortcont.items():
    print(f"{continent}: {area} кв. км")

