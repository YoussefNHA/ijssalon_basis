print("Wat is je leeftijd?")
#hier kan je de leeftijd invullen
leeftijd = int(input("Voer het aantal jaren: "))
print("Wat is je werkstatuut?")
#hier vul je de werkstatuut in
werkstatuut = input(f"Voer in: medewerker, zelfstandige of ambtenaar: ")

#hieronder wordt gecontroleerd wat er ingevuld is en wat er dan geprint wordt
def oplossing():
    statuut = ["medewerker", "zelfstandige", "ambtenaar"]
    if werkstatuut == statuut[0] and leeftijd >= 65 and leeftijd < 70:
        print(f"Je krijgt $ 350 per week.")
    elif werkstatuut == statuut [0] and leeftijd >= 70:
        print(f"Je krijgt $ 370 per week.")
    elif werkstatuut == statuut [1] and leeftijd >= 65 and leeftijd < 70:
        print(f"Je krijgt $ 300 per week.")
    elif werkstatuut == statuut [1] and leeftijd >= 70:
        print(f"Je krijgt $ 315 per week.")
    elif werkstatuut == statuut [2] and leeftijd >= 65 and leeftijd < 70:
        print(f"Je krijgt $ 370 per week.")
    elif werkstatuut == statuut [2] and leeftijd >= 70:
        print(f"Je krijgt $ 395 per week.")
    else:
        print(f"Van werken word je gelukkig, je mag nog {65 - leeftijd} jaar genieten van je baan.")
    return

oplossing()