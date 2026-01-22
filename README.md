# 🃏 TussiesJack - AI Blackjack Mester

En kraftig AI-basert blackjack-agent som kjører lokalt på mobilen ved hjelp av Firebase, Genkit og TensorFlow Lite. Inkluderer on-device ML-strategi, Genkit-coachflows og Firestore-analyse.

## 🚀 Funksjoner

- **On-Device AI**: TensorFlow Lite-modell som kjører helt lokalt uten internettforbindelse
- **Genkit-Coaching**: Intelligente flows som forklarer og veileder hver beslutning
- **Firebase Integration**: Lagrer handhistorikk, win-rate og progresjon
- **Optimal Strategi**: Trenet RL-agent som lærer fra millioner av simulerte hender
- **Støttes på**: iOS (Swift/Kotlin) via Flutter eller native implementasjon
- **Offline-First**: Fungerer fullt offline med synkronisering når wifi er tilgjengelig

## 📁 Prosjektstruktur

```
TussiesJack/
├── backend/              # Genkit + Node.js server
│   ├── src/
│   │   ├── index.ts      # Genkit app entry
│   │   ├── flows/        # AI flows (advisor, coach, analyzer)
│   │   ├── blackjack/    # Spillmotor
│   │   └── firebase/     # Firestore integrasjon
│   ├── package.json
│   └── tsconfig.json
├── mobile/               # Flutter app
│   ├── lib/
│   │   ├── main.dart
│   │   ├── screens/      # Game, Stats, Settings
│   │   ├── ml/           # TFLite integration
│   │   └── firebase/     # Auth & Firestore
│   └── pubspec.yaml
├── training/             # ML model training
│   ├── train_strategy.py # RL training script
│   ├── data/             # Training data
│   └── models/           # Saved models
└── docs/                 # Documentation
```

## 🛠️ Oppsettsguide

### Backend (Genkit)

```bash
cd backend
npm install
npm run build
npm run genkit:start  # Starter på port 3400
```

### Mobile (Flutter)

```bash
cd mobile
flutter pub get
flutter run
```

### Treningsskript

```bash
python training/train_strategy.py
```

## 📱 Spilling

1. Start appen
2. Velg "Spill"-modus eller "Coach"-modus
3. AI-agenten analyserer hendene og gir anbefalinger
4. Se statistikk og historikk i "Profil"-seksjonen

## 🧠 AI-Strategi

TussiesJack bruker:
- **Basic Strategy Table**: Hardkodet optimal blackjack-strategi
- **Reinforcement Learning**: Trenet DQN-modell som lærer fra spill
- **Genkit LLM Integration**: Claude/Gemini for forklaringer og coaching

## 🔧 Teknologi Stack

- **Backend**: Genkit, Node.js, Firebase Admin SDK
- **Mobile**: Flutter, TensorFlow Lite, Firebase
- **ML**: TensorFlow, Python, RL (DQN)
- **Cloud**: Firebase Firestore, Cloud Run, Cloud Storage

## 📊 Firestore Schema

```
users/{userId}/
  hands/{handId}/
    - dealerCard
    - playerCards
    - playerAction
    - result
    - timestamp
  stats/
    - totalHands
    - wins
    - losses
    - winRate
```

## 🎯 Neste Steg

- [ ] Implementere TFLite strategi-modell
- [ ] Bygge Flutter UI
- [ ] Konfigurere Firebase
- [ ] Teste Genkit flows
- [ ] Distribuere på App Store/Play Store

## 📜 Lisens

MIT

## 👨‍💻 Forfatter

Thomas Tussien - @tussienorway

---

**TussiesJack** - Bli en blackjack-mester! 🎰
