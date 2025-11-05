import subprocess
import threading
import time
import sys
import death_detector
import spawn_reset

time.sleep(2)

# Inställningar



WAIT_AFTER_CYCLE = 10   # sekunder att vänta mellan loopsfcccf

DEATH_CHECK_INTERVAL = 2  # hur ofta kolla för dödcccfrl



MONITOR_ACTIVE = True     # slå av/ccclpå dödsövervakningccc


# Global flagga för att signalera död34567890123
death_detected = False

def monitor_death():
    global death_detected
    while True:

        if death_detector.is_dead_screen():
            print("💀 Dödsdetekterad! Initierar återställning...")

            death_detected = True

        time.sleep(DEATH_CHECK_INTERVAL)
        
def run_cycle():
    global death_detected

    death_detected = False
    # Starta dödsövervakning i bakgrunden
    if MONITOR_ACTIVE:
        monitor_thread = threading.Thread(target=monitor_death, daemon=True)
        monitor_thread.start()

    start = time.time()

    # Kör main.py som egen subprocess men med övervakning
    main_proc = subprocess.Popen(["python", "main.py"])

    # Vänta på att main.py ska bli klar, ELLER att vi dör
    while main_proc.poll() is None:
        if death_detected:
            print("💀 Dödsdetekterad under cykel – avbryter main.py")
            main_proc.terminate()
            time.sleep(2)
            spawn_reset.respawn_at_bed()
            print("✅ Återställning klar. Startar om direkt.")
            return
        time.sleep(1)

    end = time.time()
    print(f"✅ Cykel avslutad. Tidsåtgång: {end - start:.1f} sekunder")

    print(f"⏳ Väntar {WAIT_AFTER_CYCLE} sekunder innan nästa cykel...")
    time.sleep(WAIT_AFTER_CYCLE)


if __name__ == "__main__":
    try:
        while True:
            run_cycle()
    except KeyboardInterrupt:
        print("❌ Avbruten manuellt")
        sys.exit(0)

         



""" The old one and this one works
#  Test a cycle

while True:
    start = time.time()ccc
    rl
    print("🔁 Startar ny cykel...")
    subprocess.run(["python", "main.py"])
    end = time.time()

    print("Full round took: ", (end - start))
    print("⏳ Väntar 60 sec innan nästa cykel...")
    time.sleep(10)

### Test geting in and out of the pod 10 time too find the error
"""

