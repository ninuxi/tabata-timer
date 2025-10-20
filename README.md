# ⏱️ Tabata Timer

A complete collection of timers for Tabata workouts, available in web and Python versions.

**Languages**: **English** | [Italiano](README.it.md)

## 🌐 Web Version
**[Access the Online Timer](https://ninuxi.github.io/tabata-timer/)**

A modern and responsive Tabata timer with:
- ✨ Modern design optimized for mobile
- 🔊 Voice synthesis for countdowns
- 📱 Responsive layout for all devices
- 🎯 Quick presets (Tabata 20/10, 30/15, 40/20)
- 💾 Save/load custom presets
- 📤 Export/import presets via JSON file
- 🔔 Audio cues for phase changes
- 🇮🇹/🇬🇧 Multi-language support (IT/EN) with auto-detection
- 📅 **NEW**: Weekly workout calendar with progress tracking
- 💾 **NEW**: Export/Import all your workout data as JSON
- ☁️ **NEW**: Google Drive sync (beta - requires setup)
- 📲 **NEW**: PWA installable app for offline use

## 🐍 Python Versions

### `tabata_fisso.py` - Basic Timer
A classic Tabata timer with default settings:
- **20 seconds** of work
- **10 seconds** of rest
- **8 total rounds**
- Audio signals for each phase
- Compatible with Windows/Mac/Linux

```bash
python tabata_fisso.py
```

### `tabata_personalizzabile.py` - Advanced Timer
A timer with customizable parameters and voice synthesis:
- ⚙️ Full customization (work/rest/rounds)
- 🎙️ Voice synthesis for the final countdown
- 🔊 Differentiated beeps for each phase
- 🌍 Full cross-platform support

```bash
python tabata_personalizzabile.py
```

## 🚀 How to Use

### Web
1. Go to https://ninuxi.github.io/tabata-timer/
2. Customize the work, rest, and number of rounds.
3. Use the quick presets or save your own configurations.
4. Press "START TIMER" to begin.

### Python
1. Clone the repository: `git clone https://github.com/ninuxi/tabata-timer.git`
2. Run the desired timer: `python tabata_fisso.py` or `python tabata_personalizzabile.py`

## 📋 Features

- **Accurate Timer**: Second-accurate countdown.
- **Audio Cues**: Distinctive beeps for work/rest/end.
- **Intuitive Interface**: Clean and easy-to-use design.
- **Responsive Design**: Optimized for desktop, tablet, and smartphone.
- **Preset Manager**: Save and share configurations.
- **Cross-Platform**: Works on Windows, Mac, Linux, and web browsers.
- **Multi-language**: Automatic language detection (Italian/English).
- **📅 Progress Tracking**: Weekly calendar to mark completed workouts
- **💾 Data Backup**: Export/Import all your data as JSON
- **☁️ Cloud Sync**: Google Drive integration (see [GOOGLE_SYNC_SETUP.md](GOOGLE_SYNC_SETUP.md))
- **📲 PWA Ready**: Install as app on mobile and desktop

## 💾 Backup & Sync

### Export/Import (Ready to Use)
- Click **💾 Export JSON** to download all your workout data
- Use **📥 Import JSON** on another device to restore your data
- File includes: calendar, workout history, and statistics

### Google Drive Sync (Beta)
- Requires Google Cloud configuration
- See [GOOGLE_SYNC_SETUP.md](GOOGLE_SYNC_SETUP.md) for setup instructions
- Automatic backup to your Google Drive account

---

*Perfect for HIIT, Tabata, and interval training workouts! 💪*