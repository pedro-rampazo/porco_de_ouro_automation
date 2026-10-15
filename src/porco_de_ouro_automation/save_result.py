import sys
import os
from pathlib import Path

def save_result(script_name, result):
    if not result:
        sys.exit(f"{script_name}: resultado vazio, nada para gravar")
    
    if len(result.encode("utf-8")) > 48_000:
        sys.exit(f"{script_name}: resultado maior que o limite de 48 KB da variável")
    
    Path(os.environ["OUTPUT_FILE"]).write_text(result, encoding="utf-8")

if __name__ == "__main__":
    save_result()