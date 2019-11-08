import pyowm
owm = pyowm.OWM("cfade00ca1f4fd527a497ff66c591dee",language= "ru")
place = input("введите город: ")

observation =  owm.weather_at_place(place)
w =  observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас в районе" + str(temp))
if temp < 10:
	print("Суйчас ппц как холодно,если не хочешь умереть оденься потеплее")
elif temp < 20:
	print("сейчас холодно хорошо оденься иначе твоей маме позвоню")
else:
	print("температу зашибись иди цыплять тяночек")
input()
