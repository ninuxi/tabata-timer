# ⏱️ Tabata Timer Pro

Timer professionale per allenamenti Tabata HIIT con funzionalità avanzate

## 🚀 Nuove Funzionalità

### ✨ Quick Features
- ⌨️ **Keyboard Shortcuts**: Space (Start/Pause), R (Reset), M (Mute), F (Fullscreen), ? (Help)
- 📱 **Wake Lock**: Lo schermo rimane sempre acceso durante l'allenamento
- 📳 **Vibrazione**: Feedback tattile su dispositivi mobili
- 🔊 **Controllo Volume**: Slider per regolare volume beep e voce
- ⚙️ **Toggle Separati**: Attiva/disattiva suoni, voce, vibrazione indipendentemente
- 🎨 **Flash Visuale**: Lo schermo lampeggia negli ultimi 3 secondi
- ⛶ **Modalità Fullscreen**: Allenamento immersivo senza distrazioni

### 📱 Progressive Web App (PWA)
- 📲 **Installabile**: Aggiungi alla schermata home come app nativa
- 🔌 **Funziona Offline**: Service Worker per uso senza connessione
- 🚀 **Performance**: Caricamento istantaneo con cache intelligente
- 🎯 **Shortcuts**: Avvio rapido timer o programma dalla home

### 📊 Sistema di Tracciamento
- 📝 **Storico Allenamenti**: Tutti i workout salvati automaticamente
- 📈 **Statistiche**: Total workout, round completati, ultimo allenamento
- 💾 **LocalStorage**: Dati salvati localmente, nessun server richiesto

### 🎙️ Audio Migliorato
- 🗣️ **Voce Italiana Ottimizzata**: Selezione automatica migliore voce (Alice su macOS)
- 🔔 **Beep Distintivi**: Suoni diversi per lavoro/riposo/fine sessione
- ⏱️ **Countdown Vocale 3-2-1**: Prima dell'inizio e durante ogni fase

## 🎯 Come Usare

### Installazione PWA
1. Apri l'app nel browser (Chrome, Safari, Firefox)
2. Clicca sul menu → "Installa App" / "Aggiungi a Home"
3. L'app apparirà come icona nella home del telefono
4. Apri come un'app nativa!

### Shortcuts Tastiera
- `Space` = Avvia/Pausa timer
- `R` = Reset timer
- `M` = Mute/Unmute tutto
- `F` = Fullscreen
- `?` = Mostra aiuto shortcuts

### Impostazioni Consigliate Mobile
1. Attiva "Schermo Sempre Acceso" ✅
2. Attiva "Vibrazione" per feedback tattile ✅
3. Regola volume al 80% per sentire bene senza disturbare
4. Usa modalità Fullscreen per focus massimo

## 🔧 Funzionalità Tecniche

### Compatibilità
- ✅ Chrome/Edge (Android & Desktop)
- ✅ Safari (iOS & macOS)
- ✅ Firefox
- ✅ Responsive: funziona su tutti i dispositivi

### API Utilizzate
- Wake Lock API (schermo sempre acceso)
- Web Speech API (voce countdown)
- Vibration API (feedback tattile)
- Web Audio API (beep personalizzati)
- Service Worker (PWA offline)
- LocalStorage (salvataggio dati)
- Fullscreen API

## 📦 File Struttura

```
tabata-timer/
├── index.html              # Timer principale con tutte le features
├── programma.html          # Programma allenamento con mini-timer
├── programma_testo.html    # Versione testo del programma
├── diario.html             # Diario allenamenti
├── about.html              # Info app
├── manifest.json           # PWA manifest
├── sw.js                   # Service Worker
├── icon-192.svg            # Icona app 192x192
├── icon-512.svg            # Icona app 512x512
├── img/                    # Immagini esercizi
├── robots.txt              # SEO
└── sitemap.xml             # Sitemap

```

## 🎨 Personalizzazione

### Colori Tema
Modifica le variabili CSS in `index.html`:
```css
--bg: #0a0a0a;          /* Sfondo
--accent: #00ff00;       /* Verde neon */
--accent2: #ff6b35;      /* Arancione */
--accent3: #ffd700;      /* Oro */
```

### Preset Timer
Aggiungi nuovi preset in `tabataPresets`:
```javascript
4: { work: 45, rest: 15, rounds: 10 }
```

## 📱 Mobile-First Design

L'app è ottimizzata per mobile:
- ✅ Touch-friendly: pulsanti grandi e ben spaziati
- ✅ Swipe gestures: scorri tra i pannelli
- ✅ Responsive layout: si adatta a ogni schermo
- ✅ Performance: animazioni fluide 60fps
- ✅ Accessibilità: contrasto alto, font leggibili

## 🔒 Privacy

- ✅ Nessun tracking o analytics
- ✅ Tutti i dati salvati solo localmente
- ✅ Nessun server esterno
- ✅ Funziona completamente offline
- ✅ Open source

## 🚀 Roadmap Future

### Coming Soon
- [ ] Grafici allenamenti con Chart.js
- [ ] Badge e achievement
- [ ] Workout builder custom
- [ ] Audio files pre-registrati professionali
- [ ] Dark mode toggle
- [ ] Multi-language completo
- [ ] Integrazione wearable (Apple Watch, Garmin)
- [ ] Social sharing
- [ ] Cloud sync opzionale

## 🙏 Contributi

Contributi benvenuti! Apri una issue o una PR.

## 📄 Licenza

MIT License - Libero di usare, modificare e distribuire

## 🆘 Supporto

Per bug o richieste: apri una issue su GitHub

---

**Made with 💪 for fitness enthusiasts**

Buon allenamento! 🏋️‍♂️
