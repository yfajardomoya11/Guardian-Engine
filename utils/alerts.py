from rich.console import Console

console = Console()

def send_alert(message, level="info"):
    colors = {"info": "blue", "warning": "yellow", "critical": "red bold"}
    color = colors.get(level, "white")
    console.print(f"[{color}][{level.upper()}][/{color}] {message}")
