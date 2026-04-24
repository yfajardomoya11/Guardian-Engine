import pandas as pd

# Variable global para recordar qué línea fue la última que leímos
last_processed_line = 0

def analyze_new_lines(file_path):
    global last_processed_line
    results = []
    
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            
            # Si el archivo se vació, reseteamos el contador
            if len(lines) < last_processed_line:
                last_processed_line = 0
            
            # Leemos desde la última que procesamos hasta el final
            new_lines = lines[last_processed_line:]
            
            for line in new_lines:
                line = line.strip()
                if not line: continue
                
                if "CRITICAL" in line.upper() or "ATTACK" in line.upper():
                    results.append(("critical", f"ALERTA DETECTADA: {line}"))
                elif "WARNING" in line.upper():
                    results.append(("warning", f"Actividad sospechosa: {line}"))
                else:
                    results.append(("info", f"Evento registrado: {line}"))
            
            # Actualizamos el marcador de posición
            last_processed_line = len(lines)
            return results
    except Exception as e:
        return [("error", f"Error al leer log: {e}")]