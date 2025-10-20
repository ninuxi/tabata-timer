# 🔐 Google Sync Setup Guide

## Panoramica

Questa guida spiega come configurare la sincronizzazione con Google Drive per il Tabata Timer.

## ⚠️ Nota Importante

**La funzione Google Sync è attualmente in fase di sviluppo e richiede configurazione tecnica.**

Per un backup immediato dei tuoi dati, usa:
- **💾 Export JSON** - Scarica tutti i tuoi dati
- **📥 Import JSON** - Carica i dati su un altro dispositivo

## 🔧 Configurazione Google Cloud (Per Developer)

### Step 1: Crea un Progetto Google Cloud

1. Vai su [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuovo progetto o selezionane uno esistente
3. Annota il **Project ID**

### Step 2: Abilita Google Drive API

1. Nel menu laterale, vai su **APIs & Services** → **Library**
2. Cerca "Google Drive API"
3. Clicca **Enable**

### Step 3: Configura OAuth 2.0

1. Vai su **APIs & Services** → **Credentials**
2. Clicca **Create Credentials** → **OAuth client ID**
3. Seleziona **Web application**
4. Aggiungi **Authorized JavaScript origins**:
   ```
   https://ninuxi.github.io
   http://localhost:5500
   ```
5. Aggiungi **Authorized redirect URIs**:
   ```
   https://ninuxi.github.io/tabata-timer
   http://localhost:5500/tabata-timer
   ```
6. Clicca **Create**
7. Copia il **Client ID** e l'**API Key**

### Step 4: Configura il Codice

In `programma.html`, sostituisci:

```javascript
const GOOGLE_CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID'; // ← Inserisci qui
const GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY';     // ← Inserisci qui
```

Con le tue credenziali:

```javascript
const GOOGLE_CLIENT_ID = '123456789-abc.apps.googleusercontent.com';
const GOOGLE_API_KEY = 'AIzaSyAbc123xyz...';
```

### Step 5: Test Locale

1. Avvia un server locale (es. Live Server in VS Code)
2. Apri `http://localhost:5500/programma.html`
3. Clicca su **☁️ Google Sync**
4. Autorizza l'app con il tuo account Google

### Step 6: Deploy su GitHub Pages

1. Commit e push delle modifiche
2. Vai su GitHub → Settings → Pages
3. Abilita GitHub Pages
4. L'app sarà disponibile su `https://ninuxi.github.io/tabata-timer`

## 🔐 Sicurezza

### Dati Salvati su Google Drive

- File JSON criptato (opzionale)
- Cartella dedicata: `TabataTimerBackup`
- Accesso solo alla tua app
- Non condiviso con terze parti

### Permessi Richiesti

- `https://www.googleapis.com/auth/drive.file` - Accesso ai file creati dall'app
- `https://www.googleapis.com/auth/drive.appdata` - Dati app nascosti

## 📱 Uso Pratico

### Export/Import (Funziona ORA)

1. **Export**: Clicca "💾 Export JSON" → Scarica `tabata-backup-YYYY-MM-DD.json`
2. **Import**: Su altro dispositivo → Clicca "📥 Import JSON" → Seleziona il file

### Google Sync (Richiede Setup)

1. Clicca "☁️ Google Sync"
2. Login con Google
3. Conferma permessi
4. Sincronizzazione automatica

## 🆘 Troubleshooting

### "Google Drive API non configurata"
→ Segui gli step di configurazione sopra

### "Login Google non funziona"
→ Verifica che le Redirect URI siano corrette

### "File non trovato su Drive"
→ Prima sincronizzazione? Verrà creato automaticamente

## 🔮 Roadmap

- [ ] Login con GitHub
- [ ] Backup automatico ogni N giorni
- [ ] Sincronizzazione multi-dispositivo in tempo reale
- [ ] Condivisione programmi con altri utenti
- [ ] Community di allenamenti

## 💡 Alternative

Se non vuoi configurare Google OAuth:

1. **Export/Import manuale** - Già funzionante! 💾
2. **PWA Offline** - Installa l'app e i dati restano sul dispositivo
3. **Browser Sync** - Usa Chrome/Edge sync per sincronizzare localStorage

---

**Domande?** Apri una issue su [GitHub](https://github.com/ninuxi/tabata-timer/issues)
