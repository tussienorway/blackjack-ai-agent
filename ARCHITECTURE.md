# TussiesJack - Arkitektur & Implementasjonsveiledning

## 🎯 Oversikt

TussiesJack er en AI-drevet blackjack-agent som kjører lokalt på mobilen med følgende komponenter:

1. **Backend (Genkit + Node.js)**: AI-orkestrering, coaching, og Firestore-integrasjon
2. **Mobile (Flutter)**: Native UI, on-device ML (TFLite)
3. **ML Training (Python)**: Reinforcement learning for optimal strategi

## 📂 Filstruktur som skal opprettes

```
TussiesJack/
├── backend/
│   ├── src/
│   │   ├── index.ts                 # Genkit app starter
│   │   ├── genkit.config.ts          # Genkit konfigurering
│   │   ├── flows/
│   │   │   ├── blackjackAdvisor.ts   # AI strategianbefaling
│   │   │   ├── coachFlow.ts          # Coaching forklaringer
│   │   │   └── analysisFlow.ts       # Hånd-analyse
│   │   ├── blackjack/
│   │   │   ├── engine.ts             # Spillmotor
│   │   │   ├── strategy.ts           # Basic strategy
│   │   │   └── types.ts              # Typer
│   │   └── firebase/
│   │       ├── firestore.ts          # Firestore CRUD
│   │       └── auth.ts               # Firebase Auth
│   ├── package.json
│   ├── tsconfig.json
│   └── .env.example
├── mobile/
│   ├── lib/
│   │   ├── main.dart                 # App entry
│   │   ├── screens/
│   │   │   ├── game_screen.dart      # Spill-UI
│   │   │   ├── stats_screen.dart     # Statistikk
│   │   │   └── settings_screen.dart  # Innstillinger
│   │   ├── models/
│   │   │   ├── game_state.dart       # Spilltilstand
│   │   │   └── player_stats.dart     # Spiller-stats
│   │   ├── ml/
│   │   │   ├── tflite_interpreter.dart # TFLite integration
│   │   │   └── model_loader.dart     # Modellasting
│   │   ├── firebase/
│   │   │   ├── firestore_service.dart
│   │   │   └── auth_service.dart
│   │   ├── services/
│   │   │   ├── genkit_api.dart       # Genkit HTTP-kall
│   │   │   └── game_engine.dart      # Lokal spillmotor
│   │   └── widgets/
│   │       ├── card_display.dart
│   │       └── action_buttons.dart
│   ├── pubspec.yaml
│   ├── pubspec.lock
│   └── assets/
│       ├── models/tussiesjack.tflite # ML-modell
│       └── fonts/
├── training/
│   ├── train_strategy.py            # RL training script
│   ├── requirements.txt
│   ├── data/
│   │   └── simulation_data.csv       # Treningsdata
│   └── models/
│       ├── strategy_model.h5         # Keras modell
│       └── tussiesjack.tflite        # Konvertert modell
├── docs/
│   ├── SETUP.md                      # Installasjonsveiledning
│   ├── API.md                        # API-dokumentasjon
│   └── ML_TRAINING.md                # ML-treningsveiledning
├── README.md
├── ARCHITECTURE.md                   # Denne filen
├── package.json
└── tsconfig.json
```

## 🔧 Teknisk Stack

### Backend
- **Genkit 1.0+**: AI agent framework
- **Node.js 20+**: Runtime
- **Firebase Admin SDK**: Cloud integration
- **Express.js**: REST API
- **TypeScript**: Type safety

### Mobile
- **Flutter 3.x**: Cross-platform UI
- **Firebase Flutter SDK**: Backend integration
- **TensorFlow Lite**: On-device ML
- **Provider**: State management

### ML/Training
- **TensorFlow 2.x**: Deep learning
- **Python 3.10+**: Training
- **DQN**: Reinforcement learning
- **TensorFlow Lite Converter**: Model optimization

## 📊 Data Flow

```
┌─────────────┐
│   Mobile    │
│  (Flutter)  │
└──────┬──────┘
       │
       ├─ TFLite Model ──────────────┐
       │  (on-device decisions)       │
       │                              │
       └─ HTTP ─────────────────────┐ │
                                    │ │
                         ┌──────────▼─┴──────┐
                         │  Backend (Genkit) │
                         │   ┌──────────┐    │
                         │   │ Advisor  │    │
                         │   │ Flow     │    │
                         │   └──────────┘    │
                         │   ┌──────────┐    │
                         │   │ Coach    │    │
                         │   │ Flow     │    │
                         │   └──────────┘    │
                         └────────┬──────────┘
                                  │
                         ┌────────▼──────────┐
                         │    Firebase       │
                         │  ┌────────────┐   │
                         │  │ Firestore  │   │
                         │  │ (logging)  │   │
                         │  └────────────┘   │
                         └───────────────────┘
```

## 🎯 Implementeringssteg

### Phase 1: Foundation
- ✅ GitHub repo setup
- ✅ package.json + tsconfig.json
- [ ] Blackjack engine (engine.ts)
- [ ] Basic strategy tabell (strategy.ts)

### Phase 2: Backend (Genkit)
- [ ] Genkit config (genkit.config.ts)
- [ ] Blackjack advisor flow
- [ ] Coach explanation flow
- [ ] Firestore integration
- [ ] REST API (Express)

### Phase 3: ML Model
- [ ] Training script setup
- [ ] DQN model training
- [ ] TFLite conversion
- [ ] Model optimization

### Phase 4: Mobile (Flutter)
- [ ] Project setup
- [ ] Game UI (game_screen.dart)
- [ ] TFLite integration
- [ ] Firebase auth + Firestore
- [ ] State management

### Phase 5: Integration & Deployment
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] App Store/Play Store submission
- [ ] Monitoring setup

## 🔑 Nøkkelfiler og deres Formål

### Backend Core

**src/blackjack/engine.ts**
```typescript
export interface GameState {
  playerCards: Card[];
  dealerCards: Card[];
  playerTotal: number;
  dealerTotal: number;
  hasAce: boolean;
}

export class BlackjackEngine {
  dealHand(): GameState;
  hit(state: GameState): GameState;
  stand(state: GameState): GameState;
  doubleDown(state: GameState): GameState;
  calculateWinner(state: GameState): Result;
}
```

**src/flows/blackjackAdvisor.ts**
```typescript
export const blackjackAdvisorFlow = defineFlow(
  {
    name: 'blackjackAdvisor',
    inputSchema: z.object({
      gameState: GameStateSchema,
      dealerCard: z.number(),
    }),
  },
  async (input) => {
    // Use LLM to explain best move
    // Return: { move: 'hit' | 'stand' | 'double' | 'split', explanation: string }
  }
);
```

### Mobile Core

**lib/screens/game_screen.dart**
- Game UI rendering
- Action buttons (Hit, Stand, Double, Split)
- Score display
- History tracking

**lib/ml/tflite_interpreter.dart**
- TFLite model loading
- Inference execution
- Post-processing results

## 🚀 Deployment

### Backend Deployment
```bash
# Build
npm run build

# Deploy to Cloud Run
firebase deploy --only functions

# Or run locally
npm run genkit:start
```

### Mobile Deployment
```bash
# Build APK (Android)
flutter build apk --release

# Build IPA (iOS)
flutter build ios --release
```

## 📊 Firestore Collections

### Structure
```
users/{userId}/
  ├── profile/
  │   ├── displayName
  │   ├── email
  │   └── createdAt
  ├── stats/
  │   ├── totalHands
  │   ├── wins
  │   ├── losses
  │   └── winRate
  └── hands/{handId}/
      ├── dealerCards
      ├── playerCards
      ├── playerAction
      ├── aiRecommendation
      ├── result
      └── timestamp
```

## 🔐 Environment Variables

```bash
# .env
FIREBASE_PROJECT_ID=ai-kursing
FIREBASE_API_KEY=xxx
GEMINI_API_KEY=xxx
GENKIT_PORT=3400
```

## 📚 Ressurser

- [Genkit Documentation](https://ai.google.dev/genkit)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Flutter Documentation](https://flutter.dev/docs)
- [TensorFlow Lite Guide](https://www.tensorflow.org/lite)
- [DQN Paper](https://www.nature.com/articles/nature14236)

## 🎓 Learning Resources

1. **Blackjack Basic Strategy**: https://www.blackjackinfo.com/basic-strategy/
2. **Reinforcement Learning**: Deep Q-Learning (Mnih et al., 2015)
3. **Mobile ML**: TensorFlow Lite for mobile deployment
4. **Genkit**: Agent-oriented AI development

---

**Status**: Foundation phase - Ready for implementation ✅
