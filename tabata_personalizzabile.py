import time
import os
import sys

def beep(frequency=1000, duration=500):
    """Genera un beep - compatibile Windows/Mac/Linux"""
    try:
        if os.name == 'nt':  # Windows
            import winsound
            winsound.Beep(frequency, duration)
        else:  # Mac/Linux
            # Usa 'say' su Mac, 'spd-say' su Linux
            if sys.platform == "darwin":
                os.system(f'say -r 200 "beep" &')
            else:
                os.system(f'play -nq -t alsa synth {duration/1000} sine {frequency} 2>/dev/null || spd-say "beep" &')
    except Exception as e:
        print(f"[BEEP FALLITO: {e}]")

def speak_countdown(seconds_left):
    """Dice ad alta voce gli ultimi 3 secondi"""
    if seconds_left <= 3 and seconds_left > 0:
        if os.name == 'nt':  # Windows
            try:
                import winsound
                winsound.Beep(1200, 200)  # Beep veloce prima della voce
                # Usa PowerShell per la voce su Windows
                os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; '
                         f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{seconds_left}\')"')
            except:
                print(f"🔊 {seconds_left}")
        else:  # Mac/Linux
            if sys.platform == "darwin":
                os.system(f'say -r 200 "{seconds_left}" &')
            else:
                os.system(f'spd-say "{seconds_left}" &')

def tabata_timer():
    print("🎙️ CRONOMETRO TABATA CON VOCE + BEEP")
    print("===================================")

    # INPUT PERSONALIZZATO
    try:
        work_sec = int(input("⏱️  Secondi di LAVORO (default: 20): ") or 20)
        rest_sec = int(input("🛌 Secondi di RECUPERO (default: 10): ") or 10)
        rounds = int(input("🔁 Quanti round? (default: 8): ") or 8)
    except ValueError:
        print("⚠️  Valori non validi — uso impostazioni predefinite (20/10/8)")
        work_sec, rest_sec, rounds = 20, 10, 8

    print(f"\n🚀 PARTENZA: {work_sec}\" LAVORO / {rest_sec}\" RECUPERO — {rounds} ROUND")
    print("="*60)

    for round_num in range(1, rounds + 1):
        print(f"\n🔹 ROUND {round_num}/{rounds}")

        # --- FASE DI LAVORO ---
        print(f"🔥 LAVORO — {work_sec} secondi...")
        for i in range(work_sec, 0, -1):
            print(f"  🔥 {i:2d}...", end="\r", flush=True)
            speak_countdown(i)  # Voce negli ultimi 3 secondi
            time.sleep(1)
        beep(1500, 300)  # Beep acuto — fine lavoro
        print("\n✅ LAVORO TERMINATO!           ")

        # --- FASE DI RECUPERO ---
        print(f"💤 RECUPERO — {rest_sec} secondi...")
        for i in range(rest_sec, 0, -1):
            print(f"  💤 {i:2d}...", end="\r", flush=True)
            speak_countdown(i)  # Voce negli ultimi 3 secondi
            time.sleep(1)
        beep(800, 300)  # Beep basso — fine recupero
        print("\n➡️  Pronto per il prossimo round! ")

    # --- FINE SESSIONE ---
    print("\n" + "="*60)
    print("🎉🎉🎉 SESSIONE TABATA COMPLETATA! 🎉🎉🎉")
    beep(2000, 800)  # Beep lungo finale

    # Voce di chiusura
    if os.name == 'nt':
        os.system('powershell -Command "Add-Type -AssemblyName System.Speech; '
                 '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Sessione completata. Ottimo lavoro!\')"')
    else:
        if sys.platform == "darwin":
            os.system('say -r 200 "Sessione completata. Ottimo lavoro!" &')
        else:
            os.system('spd-say "Sessione completata. Ottimo lavoro!" &')

if __name__ == "__main__":
    try:
        tabata_timer()
    except KeyboardInterrupt:
        print("\n\n⏹️  Timer interrotto manualmente. A presto!")