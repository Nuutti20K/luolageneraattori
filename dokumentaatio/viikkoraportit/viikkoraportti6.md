## Viikkoraportti 6

Tällä viikolla toteutin path_creator moduulin, joka generoi polkuja huoneiden välille. Alunperin aikomuksena oli käyttää a* algoritmia, mutta todellisuudessa tähän oli yksinkertaisempi toteutus. Koska luodussa kartassa ei ole ikinä esteitä, lyhimmän reitin löytäminen kahden huoneen välillä on helppoa ja nopeampaa kuin a* algoritmilla. Lisäksi muutin sovelluksen rakennetta ja lisäsin game_loop moduulin hoitamaan syötteidenn käsittelyn.

Projektin ydintoiminta on nyt valmis. Ohjelma pystyy trianguloimaan huoneiden välille kaikki reitit Bowyer-Watson algoritmilla ja etsimään tästä lyhimmän virittävän puun. Nyt myös ohjelma pystyy luomaan polut näistä yhteyksistä.

Opin tällä viikolla a* algoritmin toiminnasta, vaikka en päätynyt toteuttamaan sitä projektiin.

Seuraavaksi lisäilen testejä ja teen sekalaista hienosäätöä ohjelmassa.