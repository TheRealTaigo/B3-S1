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

`in ontwikkeling`

## Gebruikte technieken

| Onderdeel | Techniek |
| --- | --- |
| App en UI | [Kivy](https://kivy.org) (Python) |
| Pose-detectie | [Mediapipe Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) |
| Lokale opslag | `SQLite` |
| Cloud (later) | Microsoft Azure |
| Platform | Android |

## Aan de slag

### Vereisten

- Python `3.12`
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

## Team
- Floris van den Berg
- Tygo Offermans
- Anja Rashidi
- Jessica Smets
- Jasmijn Verhagen
