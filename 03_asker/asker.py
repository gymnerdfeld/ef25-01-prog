# Ein int bei der:m Benutzer:in abfragen
done = False
while not done:
    answer = input("Wie alt bist du? ")
    if answer.isdigit():
        age = int(answer)
        print(f"Dann wirst du nächstes Jahr {age + 1}")
        done = True
    else:
        print("Ungültige Eingabe" )


# Aufgabe:
# Der obige Code soll in eine Funktion gepackt werden


def input_int(prompt):
    ...


# Folgendermassen soll die Funktion verwendet werden können:
age = input_int("Wie alt bist du? ")
print(f"Dann wirst du nächstes Jahr {age + 1}")


# Zusatzaufgabe:
# Kreiere eine eigene Funktion `isdigit`, welche Pythons Version ersetzt.


def isdigit(text):
    ...


# Folgendermassen soll die Funktion verwendet werden können:
isdigit("1234")  # -> True
isdigit("abc23")  # -> False
isdigit("¼")  # -> False
isdigit("1.6")  # -> False
isdigit("")  # -> ???
isdigit(True)  # -> ??? (Error)
