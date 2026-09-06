from datetime import datetime

def logger_run(result):
        logs = open("logs", "a", encoding="utf-8")

        heure = datetime.now().strftime("%H:%M:%S")
        date = datetime.now().strftime("%Y-%m-d")

        url = result["url"]
        logs.write(f"[ heure : {heure} ]")
        logs.write(f"[ date  : {date}  ]")
        logs.write(f"Scan    : {url}")
