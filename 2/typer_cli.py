import typer
import json
import os

app = typer.Typer()

FILE_PATH = "payloads.json"

def read():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return [] 
    return []

def write(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def append_payload_to_file(payload: dict):
    data = read()
    data.append(payload)
    write(data)

@app.command("append")
def append_payload(payload: str):
    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError:
        typer.echo("Invalid JSON payload", err=True)
        raise typer.Exit(1)

    append_payload_to_file(parsed)
    typer.echo("Payload appended successfully")


@app.command("last_payloads")
def get_last_payloads():
    data = read()
    last_payloads = data[-10:]  
    
    if last_payloads:
        for payload in last_payloads:
            print(payload)
    else:
        typer.echo("No data found")

if __name__ == "__main__":
    app()