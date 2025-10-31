import random

def main():
    print(" Willkommen zum Zahlenratespiel!")
    print("Ich denke an eine Zahl zwischen 1 und 100.")
    
    geheimzahl = random.randint(1, 100)
    versuche = 0
    
    while True:
        tipp = input("Gib deine Zahl ein (oder 'q' zum Beenden): ")
        
        if tipp.lower() == 'q':
            print("Spiel beendet. Die Zahl war:", geheimzahl)
            break
        
        if not tipp.isdigit():
            print("Bitte gib eine gültige Zahl ein!")
            continue
        
        tipp = int(tipp)
        versuche += 1
        
        if tipp < geheimzahl:
            print("Zu niedrig! 🔽")
        elif tipp > geheimzahl:
            print("Zu hoch! 🔼")
        else:
            print(f"🎉 Richtig! Die Zahl war {geheimzahl}. Du hast {versuche} Versuche gebraucht.")
            break

if __name__ == "__main__":
    main()
