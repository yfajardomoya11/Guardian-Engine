import sys
import os
import time

# --- MANIOBRA DE SEGURIDAD: Forzar la ruta del proyecto ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
# ---------------------------------------------------------

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils.alerts import send_alert
from processor.analyzer import analyze_new_lines
from database.db_manager import init_db, save_log 

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("alerts.log"):
            # Ahora recibimos una LISTA de resultados
            results = analyze_new_lines(event.src_path) 
            for result in results:
                level, message = result
                send_alert(message, level)
                save_log(level, message)

def start_engine():
    init_db()
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path=BASE_DIR, recursive=False)
    
    send_alert(">>> Guardian-Engine v1.0: MODO VIGILANCIA + DB ACTIVADO", "info")
    send_alert(f"Vigilando: {BASE_DIR}", "info")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        send_alert("Motor detenido por el usuario.", "warning")
    observer.join()

if __name__ == "__main__":
    start_engine() 