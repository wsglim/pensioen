# vraag naar de leeftijd en maak van het antwoord een int-type (integer)
print("Wat is je leeftijd?")
leeftijd=int(input("Voer het aantal jaren in: "))

# vraag naar de werkstatuut
print("Wat is je werkstatuut?")
werkstatuut=input("Voer in: medewerker, zelfstandige of ambtenaar: ")

# maak een list met werkstatuten
werkstatuten=['medewerker','zelfstandige','ambtenaar']

# maak een functie met een parameter voor de berekening van resterende jaren
def resterende_jaren(lt):
    resterend=65-lt
    # geef de uitkomst van de berekening als teruggeefwaarde 
    return resterend

# maak van de leeftijd-variabele het argument voor de berekening van de resterende jaren
# maak een variabele van de teruggeefwaarde van de functie resterende_jaren
wachttijd=resterende_jaren(leeftijd)

# maak een keuzelijst met het pensioenbedrag per leeftijdscategorie en werkstatuut uit de list.
if leeftijd<65:
    # geef de teruggeefwaarde van de functie "resterende_jaren" als je moet wachten op je pensioen.
    print(f"Van werken word je gelukkig, je mag nog {wachttijd} jaar genieten van je baan.")
elif leeftijd<70:
    if werkstatuut==werkstatuten[0]:
        print("Je krijgt €350 per week.")
    elif werkstatuut==werkstatuten[1]:
        print("Je krijgt €300 per week.")
    elif werkstatuut==werkstatuten[2]:
        print("Je krijgt €370 per week.")
elif leeftijd>=70:
    if werkstatuut==werkstatuten[0]:
        print("Je krijgt €370 per week.")
    elif werkstatuut==werkstatuten[1]:
        print("Je krijgt €315 per week.")
    elif werkstatuut==werkstatuten[2]:
        print("Je krijgt €395 per week.")