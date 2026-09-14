# Adaptive Arena — projectplanning

## Fase 1 — Een speelbare basis - [x]
*Grotendeels afgerond.*

### 1. Venster en game-loop - [x]
Een venster openen, gebeurtenissen verwerken, het scherm verversen en de framesnelheid begrenzen.

**Einddoel:** het spel opent en sluit netjes en heeft één centrale game-loop.

### 2. Spelerbeweging - [x]
Toetsen uitlezen, posities bijhouden met vectoren en beweging berekenen met snelheid en verstreken tijd.

**Einddoel:** de speler beweegt soepel met WASD, gaat diagonaal niet sneller en blijft binnen het scherm.

### 3. Eén achtervolgende vijand - [x]
De richting van een vijand naar de speler berekenen en cirkelbotsingen herkennen.

**Einddoel:** een vijand achtervolgt de speler en aanraking veroorzaakt game over.

### 4. Game over en herstarten - [x]
Verschillende speltoestanden gebruiken en alle gegevens van een poging opnieuw instellen.

**Einddoel:** na game over kun je met R opnieuw beginnen zonder het programma opnieuw te starten.

### 5. Meerdere vijanden - [x]
Vijanden bewaren in een lijst, hun eigenschappen groeperen en nieuwe vijanden aan willekeurige schermranden maken.

**Einddoel:** er verschijnen regelmatig nieuwe vijanden die onafhankelijk bewegen en botsingen veroorzaken.

### 6. Overlevingstijd - [x]
De duur van een poging meten en tonen.

**Einddoel:** iedere poging krijgt een eindtijd die bij game over stopt en bij herstart wordt gereset.

## Fase 2 — Gegevens opslaan en begrijpen - []
*Hier zijn we nu.*

### 7. Resultaten opslaan - [x]
Iedere voltooide poging als één rij toevoegen aan een CSV-bestand, met eenmalig de kolomnamen.

**Einddoel:** resultaten blijven bewaard na het sluiten van het spel, zonder dubbele rijen per poging.

### 8. Resultaten teruglezen - [x]
Een CSV-reader gebruiken, de kopregel overslaan, lijsten indexeren en tekst naar getallen omzetten.

**Einddoel:** een apart analyseprogramma verzamelt alle overlevingstijden als getallen in een lijst.

### 9. Eerste statistieken - [x]
Aantal pogingen, gemiddelde, mediaan, minimum en maximum leren berekenen en interpreteren.

**Einddoel:** je analyseprogramma geeft een begrijpelijk overzicht van je resultaten, ook als er nog geen pogingen zijn.

### 10. Datakwaliteit controleren - [x]
Omgaan met lege regels, ontbrekende waarden en ongeldige getallen. Eenheden en kolomnamen consequent gebruiken.

**Einddoel:** je weet welke gegevens bruikbaar zijn en je analyse loopt niet onverwacht vast op een verkeerde rij.

### 11. Eerste grafieken - [x]
Met Matplotlib resultaten zichtbaar maken: overlevingstijd per poging en de verdeling van overlevingstijden.

**Einddoel:** je maakt twee leesbare grafieken met titels, asnamen en eenheden, en legt uit wat ze laten zien.

### 12. Analyseren met pandas - []
Dezelfde gegevens als een tabel inladen, kolommen selecteren, filteren en samenvatten.

**Einddoel:** je kunt je eerdere analyse met pandas uitvoeren en begrijpt hoe dat aansluit op je eigen Python-berekeningen.

## Fase 3 — De game als experiment - []

### 13. Moeilijkheidsinstellingen - []
Instelbare vijandsnelheid en spawninterval toevoegen. De gebruikte instellingen bij iedere poging opslaan.

**Einddoel:** je kunt meerdere moeilijkheidsniveaus spelen en achteraf zien onder welke instellingen iedere poging plaatsvond.

### 14. Een eerlijke vergelijking - []
Een onderzoeksvraag formuleren, één instelling tegelijk veranderen en meerdere pogingen per instelling spelen.

**Einddoel:** je kunt met resultaten onderbouwen hoe bijvoorbeeld het spawninterval de overlevingstijd beïnvloedt.

### 15. Meer gedrag meten - []
Afgelegde afstand en bijvoorbeeld tijd nabij een schermrand meten. Vastleggen wat iedere meting precies betekent.

**Einddoel:** je dataset bevat naast de eindtijd ook enkele betrouwbare beschrijvingen van speelgedrag.

### 16. Metingen tijdens een poging - []
Iedere seconde een momentopname bewaren met onder andere pogingnummer, verstreken tijd, spelerpositie en aantal vijanden.

**Einddoel:** je kunt reconstrueren hoe een poging zich ontwikkelde, zonder iedere frame gegevens op te slaan.

### 17. Code organiseren - []
Verantwoordelijkheden verdelen over spelbesturing, speler, vijanden, opslag en analyse. Herhaling verminderen en waar nuttig classes introduceren.

**Einddoel:** je kunt uitleggen waar iedere taak thuishoort en een eigenschap aanpassen zonder op veel plekken dezelfde code te veranderen.

## Fase 4 — SQL en databases - []

### 18. Resultaten naar SQLite brengen - []
Tabellen maken voor pogingen en momentopnamen. Ze verbinden met een uniek pogingnummer.

**Einddoel:** het spel slaat gegevens op in een lokale database en iedere momentopname hoort bij de juiste poging.

### 19. Vragen beantwoorden met SQL - []
Selecteren, filteren, sorteren, groeperen en tabellen combineren.

**Einddoel:** je kunt vragen beantwoorden zoals: “Wat is de gemiddelde overlevingstijd per moeilijkheid?” en “Hoe ontwikkelde het aantal vijanden zich tijdens deze poging?”

### 20. Database en analyse verbinden - []
Gegevens uit SQLite in pandas laden en gebruiken voor statistieken en grafieken.

**Einddoel:** je hebt een complete keten van spelen naar opslaan naar analyseren.

## Fase 5 — Eerste machine learning - []

### 21. Een voorspelvraag definiëren - []
Kiezen wat het model moet voorspellen, bijvoorbeeld: “Overleeft de speler vanaf dit meetmoment nog vijftien seconden?”

**Einddoel:** je kunt precies uitleggen wat één trainingsvoorbeeld is, welke informatie het model krijgt en wat het juiste antwoord is.

### 22. Trainingsgegevens voorbereiden - []
Momentopnamen van labels voorzien en volledige pogingen verdelen over trainings- en testgegevens. Informatie uit de toekomst buiten de invoer houden.

**Einddoel:** je hebt een dataset waarmee je eerlijk kunt testen op pogingen die het model niet heeft gezien.

### 23. Een eenvoudige vergelijking maken - []
Een basisvoorspelling opstellen, bijvoorbeeld altijd de meest voorkomende uitkomst voorspellen.

**Einddoel:** je hebt een meetbaar startpunt waarmee je kunt beoordelen of machine learning werkelijk iets toevoegt.

### 24. Een eerste model trainen - []
Met scikit-learn een eenvoudig model trainen, zoals logistische regressie of een beslisboom.

**Einddoel:** het model doet voorspellingen voor ongeziene pogingen en je vergelijkt de resultaten met je basisvoorspelling.

### 25. Fouten en beperkingen onderzoeken - []
Bekijken wanneer het model verkeerd voorspelt, of het overfit en welke informatie mogelijk ontbreekt.

**Einddoel:** je kunt uitleggen hoe goed het model werkt, waar het faalt en wat je nodig hebt om het te verbeteren.

## Fase 6 — Adaptieve moeilijkheid - []

### 26. Moeilijkheid met regels aanpassen - []
Eerst een begrijpelijk systeem maken dat op basis van de speltoestand de moeilijkheid voorzichtig verhoogt of verlaagt.

**Einddoel:** moeilijkheid verandert geleidelijk, blijft binnen grenzen en kan worden vergeleken met vaste instellingen.

### 27. Modelvoorspellingen in het spel gebruiken - []
Op vaste momenten een voorspelling opvragen en die gebruiken om de moeilijkheid bij te sturen.

**Einddoel:** het spel past zich met behulp van je model aan en bewaart welke aanpassingen het uitvoert.

### 28. Het resultaat evalueren - []
Vaste moeilijkheid, regelgestuurde moeilijkheid en modelgestuurde moeilijkheid vergelijken. Ook je speelervaring vastleggen.

**Einddoel:** je kunt onderbouwen of het adaptieve systeem het spel beter maakt. Langer overleven alleen is niet automatisch hetzelfde als meer plezier.

## Fase 7 — Het project afronden - []

### 29. Betrouwbaarheid en gebruik - []
Belangrijke berekeningen en resetgedrag controleren. Installatie, starten en analyseren beschrijven. Afhankelijkheden vastleggen.

**Einddoel:** iemand anders kan het project installeren, spelen en de analyse uitvoeren met behulp van je README.

### 30. Resultaten presenteren - []
Het spel demonstreren en je onderzoeksvraag, grafieken, modelresultaten en lessen beschrijven.

**Einddoel:** je hebt een portfolio-project waarvan je zelf de code en gemaakte keuzes kunt uitleggen.

## Optionele vervolgroutes — andere talen - []

Kies na het kernproject één route tegelijk. Deze zijn uitbreidingen, geen voorwaarden om het project af te ronden.

### C# - []
Bouw een kleine versie van dezelfde game in een engine die C# ondersteunt.

**Einddoel:** je begrijpt hoe spelobjecten, types en de updatecyclus verschillen van jouw Python-versie.

### C++ - []
Bouw een kleine vijandsimulatie en leer over compileren, geheugen en het meten van prestaties.

**Einddoel:** je kunt dezelfde bewegingsberekening in C++ uitvoeren en verschillen verklaren.

### Rust - []
Maak een programma dat je opgeslagen resultaten leest en samenvat.

**Einddoel:** je maakt kennis met ownership, borrowing en foutafhandeling aan de hand van gegevens die je al begrijpt.

### Assembly - []
Inspecteer de assembly van een kleine gecompileerde functie en onderzoek instructies, registers en sprongen.

**Einddoel:** je kunt bij een eenvoudig voorbeeld uitleggen hoe broncode wordt vertaald naar instructies voor de processor.

## Werkwijze bij iedere stap

1. Beschrijf in eigen woorden wat het onderdeel moet doen.
2. Zoek de benodigde functies op in de documentatie.
3. Maak de kleinst mogelijke werkende versie.
4. Test normale situaties en minstens één randgeval.
5. Leg uit waarom de oplossing werkt.
6. Bewaar de afgeronde stap met een duidelijke Git-commit.

De volgende stap begint wanneer je het huidige onderdeel kunt demonstreren én uitleggen.