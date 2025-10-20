import time
import os

def beep(frequency=1000, duration=500):
    """Suona un beep (Windows/Linux/Mac compatibile)"""
    try:
        if os.name == 'nt':  # Windows
            import winsound
            winsound.Beep(frequency, duration)
        else:  # Mac/Linux
            os.system(f'play -nq -t alsa synth {duration/1000} sine {frequency} 2>/dev/null || say "beep"')
    except:
        print("[BEEP]")

def tabata_timer():
    rounds = 8
    work_sec = 20
    rest_sec = 10

    print("🏁 CRONOMETRO TABATA — 20\" LAVORO / 10\" RECUPERO")
    print("="*50)

    for round_num in range(1, rounds + 1):
        print(f"\n🔹 ROUND {round_num}/{rounds}")

        # LAVORO
        print(f"⏳ LAVORO — {work_sec} secondi...")
        for i in range(work_sec, 0, -1):
            print(f"  {i}...", end="\r")
            time.sleep(1)
        beep(1500, 300)  # Beep acuto
        print("\n✅ LAVORO TERMINATO!")

        # RECUPERO
        print(f"🛌 RECUPERO — {rest_sec} secondi...")
        for i in range(rest_sec, 0, -1):
            print(f"  {i}...", end="\r")
            time.sleep(1)
        beep(800, 300)  # Beep basso
        print("\n➡️ Pronto per il prossimo round!")

    # FINE
    print("\n" + "="*50)
    print("🎉 SESSIONE TABATA COMPLETATA!")
    beep(2000, 800)  # Beep finale lungo

if __name__ == "__main__":
    tabata_timer()