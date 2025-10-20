# ⏱️ Cronometro Tabata

Una collezione completa di timer per allenamenti Tabata, disponibile in versione web e Python.

**Lingue**: [English](README.md) | **Italiano**

## 🌐 Versione Web
**[Accedi al Timer Online](https://ninuxi.github.io/tabata-timer/)**

Cronometro Tabata moderno e responsive con:
- ✨ Design moderno ottimizzato per mobile
- 🔊 Sintesi vocale per countdown
- 📱 Layout responsive per tutti i dispositivi
- 🎯 Preset rapidi (Tabata 20/10, 30/15, 40/20)
- 💾 Salvataggio/caricamento preset personalizzati
- 📤 Esportazione/importazione preset tramite file JSON
- 🔔 Segnali audio per cambio fase
- 🇮🇹/🇬🇧 Supporto multilingua (IT/EN) con rilevamento automatico
- 📅 **NUOVO**: Calendario settimanale con tracking progressi
- 💾 **NUOVO**: Export/Import di tutti i tuoi dati come JSON
- ☁️ **NUOVO**: Sincronizzazione Google Drive (beta - richiede setup)
- 📲 **NUOVO**: App PWA installabile per uso offline

## 🐍 Versioni Python

### `tabata_fisso.py` - Timer Base
Timer Tabata classico con impostazioni predefinite:
- **20 secondi** di lavoro
- **10 secondi** di recupero  
- **8 round** totali
- Segnali audio per ogni fase
- Compatibile Windows/Mac/Linux

```bash
python tabata_fisso.py
```

### `tabata_personalizzabile.py` - Timer Avanzato
Timer con parametri personalizzabili e sintesi vocale:
- ⚙️ Personalizzazione completa (lavoro/recupero/round)
- 🎙️ Sintesi vocale per countdown finale
- 🔊 Beep differenziati per ogni fase
- 🌍 Supporto multipiattaforma completo

```bash
python tabata_personalizzabile.py
```

## 🚀 Come Usare

### Web
1. Vai su https://ninuxi.github.io/tabata-timer/
2. Personalizza i tempi di lavoro, recupero e numero di round.
3. Usa i preset rapidi o salva le tue configurazioni.
4. Premi "AVVIA TIMER" per iniziare.

### Python
1. Clona il repository: `git clone https://github.com/ninuxi/tabata-timer.git`
2. Esegui il timer desiderato: `python tabata_fisso.py` o `python tabata_personalizzabile.py`

## 📋 Caratteristiche

- **Timer Preciso**: Countdown accurato al secondo.
- **Segnali Audio**: Beep distintivi per lavoro/recupero/fine.
- **Interfaccia Intuitiva**: Design pulito e facile da usare.
- **Responsive Design**: Ottimizzato per desktop, tablet e smartphone.
- **Preset Manager**: Salvataggio e condivisione configurazioni.
- **Cross-Platform**: Funziona su Windows, Mac, Linux e browser web.
- **Multilingua**: Rilevamento automatico della lingua (Italiano/Inglese).
- **📅 Tracking Progressi**: Calendario settimanale per segnare gli allenamenti completati
- **💾 Backup Dati**: Export/Import di tutti i tuoi dati come JSON
- **☁️ Sync Cloud**: Integrazione Google Drive (vedi [GOOGLE_SYNC_SETUP.md](GOOGLE_SYNC_SETUP.md))
- **📲 PWA Ready**: Installabile come app su mobile e desktop

## 💾 Backup & Sincronizzazione

### Export/Import (Pronto all'Uso)
- Clicca **💾 Export JSON** per scaricare tutti i tuoi dati di allenamento
- Usa **📥 Import JSON** su un altro dispositivo per ripristinare i dati
- Il file include: calendario, storico allenamenti e statistiche

### Google Drive Sync (Beta)
- Richiede configurazione Google Cloud
- Vedi [GOOGLE_SYNC_SETUP.md](GOOGLE_SYNC_SETUP.md) per le istruzioni di setup
- Backup automatico sul tuo account Google Drive

---

*Perfetto per allenamenti HIIT, Tabata e interval training! 💪*
