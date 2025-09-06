## Määrittelydokumentti

Tässä harjoitustyössä käytetään pythonia, enkä hallitse muita kieliä sillä tasolla, että pystyisin tekemään vertaisarviointeja.

Tavoitteena on tehdä kaksiulotteinen peli, jossa on ruudukossa huoneita, joiden välille generoidaan automaattisesti käytävät. Huoneiden generoinnin voisi sattunnaistaa myöhemmässä vaiheessa, mutta ensisijaisesti keskityn huoneiden välisten verkon luomiseen Bowyer–Watson algoritmilla ja sen jälkeen etsimään verkosta pienin virittävä puu primmin algoritmilla (prim's algorithm). Lopuksi käytetään A* algoritmia luomaan lyhimmät reitit huoneiden välille.

Käytettäviä lähteitä ovat kurssin suosittelemat aiheeseen liittyvät lähteet sekä Wikipedia. Muihin lähteisiin en ole vielä perehtynyt.

Aiheen ydin on huoneiden välisten verkon luominen, pienimmän virittävän puun löytäminen ja polkujen generointi. Prioriteettina ei ole pelin toiminnallisuus, kuten hahmon liikuttaminen ja muut pelimekaniikat, vaan luolaston generointi.