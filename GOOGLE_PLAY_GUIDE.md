# 📱 Google Play Publishing Guide - BlackJack Pro

Denne guiden viser hvordan du publiserer BlackJack Pro på Google Play Store.

## 📋 Forutsetninger

- ✅ Google-konto
- ✅ Google Play Developer account ($25 one-time fee)
- ✅ APK eller AAB-fil (vi generer fra PWA)
- ✅ App-ikon (512x512 PNG)
- ✅ Screenshots (minst 2)
- ✅ Beskrivelse, kategori, osv.

---

## 🚀 Steg-for-steg

### 1. Registrer som Developer

1. Gå til **play.google.com/apps/publish**
2. Klikk **Create app**
3. Fyll inn app-navn: "BlackJack Pro"
4. Velg kategori: **Games > Card**
5. Klikk **Create**

### 2. Lag App-ikon

Du trenger **512x512 PNG** med åpent felt rundt:

```
BlackJack Pro Icon:
- Format: PNG (transparent background)
- Size: 512x512 pixels
- Content: 🎰 emoji eller ditt eget design
```

Bruk f.eks. **Photoshop**, **Canva**, eller **GIMP** (gratis).

**Tips**: Åpne `index.html` i en browser, åpne DevTools (F12), ta screenshot av headeren, og gjør det til et ikon.

### 3. Ta Screenshots

Du trenger minst 2 skjermbilder (for hver device type):

**Phone (1080x1920):**
- Screenshot 1: App-hjem med tips-knapp
- Screenshot 2: Resultat-skjerm med råd
- Screenshot 3: Cache statistikk

**Tablet (1440x2560) - optional:**
- Samme som phone, men større

**Hvordan ta screenshots:**

```bash
# Chrome DevTools (F12)
# 1. Trykk Ctrl+Shift+M (mobile mode)
# 2. Åpne appen
# 3. Trykk ... → Capture screenshot
```

### 4. Lag beskrivelser

#### App Title:
```
BlackJack Pro - AI Strategy Advisor
```

#### Short Description (80 chars):
```
AI-powered BlackJack tips with smart cache learning system.
```

#### Full Description (4000 chars):
```
BlackJack Pro - Your AI-powered strategy advisor!

Get instant, mathematically-optimized BlackJack strategy tips based on your hand and the dealer's card. Our smart AI cache system learns from your playing patterns and adapts its advice.

FEATURES:
✅ Instant Strategy Tips - Based on optimal BlackJack basic strategy
✅ Smart Cache Memory - AI learns from your last 4 rounds
✅ Pattern Recognition - Warns about risky sequences
✅ Mobile Optimized - Smooth gameplay on all devices
✅ Offline Ready - Works without internet connection
✅ Camera Integration - Analyze cards visually

HOW TO PLAY:
1. Open the game
2. Place your bet
3. Click "Deal"
4. Follow AI strategy tips for optimal play
5. Hit, Stand, Double Down, or Split based on tips
6. Watch the cache learn your patterns

DISCLAIMER:
This is a strategy guide tool, not a gambling app. No real money is involved. This tool is for educational purposes to learn proper BlackJack strategy.

STRATEGY BASIS:
Our AI uses the Basic BlackJack strategy, a mathematically proven approach that reduces the house edge to its lowest possible level.
```

### 5. Fyll ut Play Store-skjemaer

Når appen er opprettet i Play Console, må du gjennom noen obligatoriske skjemaer.

#### App Access
Velg om hele appen er tilgjengelig, eller om noe er låst bak innlogging. For BlackJack Pro er det som regel **Full access**.

#### Ads (annonser)
Hvis appen ikke har reklame, velger du **No, my app does not contain ads**.

#### Content Rating
Fyll ut spørsmål om gambling, vold, osv.
- For BlackJack Pro: marker at det er **kortspill / gambling-relatert**, men **UTEN ekte penger**.

#### Target Audience
Velg målgruppe. Siden dette er blackjack-strategi:
- Velg **13+ eller 18+** (ikke barn under 13)
- Ikke markedsfør mot barn

#### Data Safety
Svar på om du samler inn data:
- Hvis appen bare kjører logikk lokalt og ikke sender personinfo ut = **"Does not collect data"**
- Les nøye gjennom spørsmålene

### 6. Last opp ikon og screenshots

I Play Console under **Store listing**:

**High-res icon:**
- 512x512 px
- 32-bit PNG
- Maks 1024 KB
- Hel firkant, ingen runde hjørner (Google runder selv)

**Screenshots:**
- Minst 2 for telefon (f.eks. 1080x1920)
- Du kan bruke de du tok via Chrome DevTools (mobilvisning)
- Bruk "Preview" for å se hvordan det ser ut

### 7. Legg inn tekster (tittler og beskrivelser)

I **Main store listing** fyller du inn:

**App name (Title)**
- Maks ca. 30 tegn anbefalt for best synlighet
- Eksempel: `BlackJack Pro - AI Strategy Advisor`

**Short description** (maks 80 tegn)
- F.eks.: `AI-powered BlackJack tips with smart cache learning.`
- Ingen emojis, ingen overdrivelser

**Full description** (opptil 4000 tegn)
- Bruk teksten fra punkt 4 over
- Pass på:
  - Ikke lov å love gevinst eller garantert profitt
  - Fokus på læring, strategi og underholdning
  - Klar disclaimer at det er IKKE penger-spill

### 8. Generer APK/AAB fra PWA

For å konvertere PWA til Android-app, bruk **Bubblewrap**:

```bash
# Installer Bubblewrap
npm install -g @bubblewrap/cli

# Initialiser prosjekt
bubblewrap init --manifest="https://yourdomain.com/manifest.json"

# Build APK
bubblewrap build

# Build AAB (recommended for Play Store)
bubblewrap build --app-bundle
```

Dette genererer en `.aab`-fil som er klar for Play Store.

### 9. Last opp APK/AAB

Når PWA-en er pakket som AAB:

1. Gå til Play Console → **Production → Create release**
2. Klikk **Upload** og velg `.aab`-fila
3. Skriv en kort **release note**, f.eks.:
   ```
   Initial release of BlackJack Pro
   - AI-powered strategy tips
   - Smart cache learning system
   - Mobile-optimized gameplay
   - Offline support
   ```
4. Klikk **Next**

### 10. Sjekkliste før publisering

Gå gjennom denne før du trykker "Submit for review":

- ✅ App-ikon er 512x512 PNG og ser klart og tydelig ut
- ✅ Minst 2 screenshots lastet opp
- ✅ Title, short description og full description er fylt ut
- ✅ Content rating-skjema er ferdig
- ✅ Data Safety-skjema er ferdig
- ✅ Privacy policy lenke (hvis nødvendig)
- ✅ AAB er lastet opp i en Production-release
- ✅ App-kategori satt til "Games > Card"
- ✅ Target audience satt (13+ eller 18+)

---

## 🎲 Tips før Å få Godkjent Raskere

1. **Disclaimer**: Vær VELDIG klar at det ikke er ekte penger
2. **No Ads**: Unngå aggressive annonser (de fleste nekter app-er med for mange ads)
3. **Professional Icon**: Lag et pønt ikon, ikke bare tekst
4. **Clear Descriptions**: Skriv kort og klart hva appen gjør
5. **Real Screenshots**: Bruk faktiske screenshots, ikke mock-ups
6. **Privacy**: Ikke krev data du ikke trenger

---

## ✍️ Eksempel: Release Notes

```
v1.0 - Initial Release
- AI-powered BlackJack strategy advisor
- Smart cache system learns from your gameplay
- Pattern recognition warns about risky sequences
- Mobile-optimized for smooth gameplay
- Offline support for uninterrupted play
- Camera integration for card analysis
- No ads or in-app purchases
- Educational tool for learning optimal strategy
```

---

## 🔗 Nyttige Lenker

- **Google Play Console**: https://play.google.com/console
- **Google Play Policy**: https://play.google.com/about/developer-content-policy/
- **Bubblewrap**: https://github.com/GoogleChromeLabs/bubblewrap
- **PWA Guidelines**: https://web.dev/progressive-web-apps/
- **BlackJack Basic Strategy**: https://www.blackjackapprenticeship.com/basic-strategy-charts/

---

## 🙋 Hva hvis Review blir Nektet?

### Vanlige Avslag:

**"App requires gambling disclosure"**
- Løsning: Legg til en KLAR disclaimer at det IKKE er ekte penger

**"Content rating unclear"**
- Løsning: Fyll ut content rating-skjemaet riktig, marker som "games with gambling"

**"Misleading description"**
- Løsning: Fjern ord som "win", "earn", "profit" - bruk "learn", "practice", "strategy"

**"Ad policy violation"**
- Løsning: Fjern aggressive ads, eller bruk AdMob med riktig setup

### Hvis du blir Avvist:

1. Les review-feedback nøye
2. Fiks problemet
3. Resubmit - du kan få en ny review i 1-2 timer
4. Repeter til godkjent

---

## 👏 Gratulerer! 🎉

Nnår appen er publisert:
- Del den på sosiale medier
- Bed venner om reviews
- Oppdater appen med forbedringer
- Lytt til user feedback

**Lykke til!** 🚀
