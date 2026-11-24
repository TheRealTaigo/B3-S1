# Measuring personal health

Een Android-app die jongeren helpt om thuis zelfstandig te sporten. De app herkent met de telefooncamera hoe je een oefening uitvoert, geeft direct feedback op je houding en houdt je gemotiveerd met punten, een progressiebalk en quests.

> **Let op:** de app is een spel en geeft geen medisch advies, diagnoses of lichaamsoordelen.

## Waarom dit project

Beginnen in een sportschool is voor veel jongeren een grote stap, en sportschoolabonnementen zijn duurder geworden. Wie thuis begint, heeft niemand die ingrijpt als een oefening verkeerd gaat, wat het risico op blessures vergroot. Deze app geeft begeleiding en motivatie, zonder extra apparatuur: alleen een telefoon.

## Functies

- **Houdingsherkenning** met de camera, realtime en op het toestel zelf.
- **Directe feedback** tijdens de oefening, geformuleerd als aanwijzing en niet als oordeel.
- **Gamification:** punten voor correcte herhalingen, een progressiebalk onder het camerabeeld en quests zoals “Doe 10 correcte push-ups”.
- **Offline eerst:** de kern werkt zonder internet.
- **Privacy:** camerabeelden worden niet opgeslagen en alleen op het toestel verwerkt.

## Status

`[invullen: bijvoorbeeld "in ontwikkeling, designfase afgerond"]`

| Onderdeel | Status |
| --- | --- |
| Basisapplicatie (Kivy) | `[invullen]` |
| Pose-detectie (Mediapipe) | `[invullen]` |
| Gamification (punten, balk, quests) | `[invullen]` |
| Synchronisatie met de cloud | `[invullen]` |

## Gebruikte technieken

| Onderdeel | Techniek |
| --- | --- |
| App en UI | [Kivy](https://kivy.org) (Python) |
| Pose-detectie | [Mediapipe Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) |
| Lokale opslag | `[invullen, bijvoorbeeld Kivy JsonStore of SQLite]` |
| Cloud (later) | Microsoft Azure |
| Platform | Android |

## Aan de slag

### Vereisten

- Python `[versie invullen]`
- Een computer met camera om te testen, of een Android-toestel

### Installeren

```bash
git clone [repo-url invullen]
cd [mapnaam invullen]
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Starten op de computer

```bash
python main.py
```

### Bouwen voor Android

Met [Buildozer](https://buildozer.readthedocs.io) (werkt op Linux of in WSL):

```bash
pip install buildozer
buildozer -v android debug
```

De APK staat daarna in de map `bin/`.

> Pas de bestandsnamen en commando’s hierboven aan naar jullie eigen opzet.

## Gamification in het kort

Alle spelelementen draaien om de uitkomst van een herhaling, zodat techniek zwaarder weegt dan het aantal herhalingen.

| Actie | Punten |
| --- | --- |
| Correcte herhaling | 10 |
| Incorrecte herhaling | 0 |
| Niet beoordeeld (tracking onbetrouwbaar) | 0 |
| Voltooide quest | 20 tot 100 |

- Punten gaan nooit af.
- De **progressiebalk** toont goedgekeurde herhalingen, herhalingen met feedback, de techniekscore, de teller (bijvoorbeeld 16/20) en de sessiepunten.
- Een **quest** is een eenvoudige challenge: een aantal correcte herhalingen van één oefening. Alleen correcte herhalingen tellen mee.

Het volledige ontwerp staat in het designdocument.

## Projectstructuur

`[Pas aan naar jullie echte mappen. Voorbeeld:]`

```
.
├── main.py              # startpunt van de app
├── gamification/        # punten, techniekscore en quests
├── screens/             # Kivy-schermen en de progressiebalk
├── docs/                # voorstel, onderzoek, analyse en design
├── requirements.txt
└── buildozer.spec
```

## Documentatie

Alle projectdocumenten staan in de map `docs/` `[of voeg links toe]`:

- Voorstel
- Onderzoek
- Analyse en advies
- Design gamification

## Privacy

- Camerabeelden worden niet opgeslagen en gaan niet naar internet.
- Alleen uitkomsten (aantallen, punten, questvoortgang) worden bewaard.
- Er worden geen gewicht, BMI of lichaamsoordelen opgeslagen.

## Team

- Jason Bakker
- Floris van den Berg
- Tygo Offermans
- Anja Rashidi
- Jessica Smets
- Jasmijn Verhagen

## Bijdragen

1. Maak een eigen branch voor elke taak: `git checkout -b feature/naam-van-de-taak`.
2. Commit met een korte, duidelijke beschrijving.
3. Open een pull request en laat een teamlid meekijken voordat je merget.
4. Werk in aparte bestanden en schermen waar het kan, zodat we elkaar niet in de weg zitten.

## Licentie

`[invullen, bijvoorbeeld MIT, of verwijder deze sectie]`
