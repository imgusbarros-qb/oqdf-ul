import json
import pandas as pd
import math
from pathlib import Path
from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "OQDF-UL.schema.json"

def infer_qubits(num_rows):
    """Small utility to calculate minimum number of qubits for N states."""
    return math.ceil(math.log2(num_rows))

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_oQDF(data):
    schema = load_schema()
    try:
        validate(instance=data, schema=schema)
        print("✔ Schema validation: OK")
    except ValidationError as e:
        print("❌ Schema validation failed:")
        print(e)
        exit(1)

def build_blueprint(oqdf, df):
    rows = len(df)
    qubits = infer_qubits(rows)

    print("\n🔷 Quantum Blueprint Summary")
    print("----------------------------")
    print(f"Rows in dataset      : {rows}")
    print(f"Inferred qubits      : {qubits}")
    print(f"Declared qubits      : {oqdf['quantum_space']['num_qubits']}")
    print(f"Layers               : {oqdf['quantum_space']['layers']}")
    print("\nFeature Encodings:")
    for f in oqdf["feature_map"]:
        print(f"  - {f['name']} → {f['encoding']}")

    print("\n🔷 State vector size:", 2 ** qubits)
    print("\nBlueprint generation completed.\n")

def main():
    oqdf_path = ROOT / "examples" / "OQDF-UL-example.json"

    with open(oqdf_path, "r", encoding="utf-8") as f:
        oqdf = json.load(f)

    validate_oQDF(oqdf)

    csv_path = ROOT / "examples" / oqdf["classical_source"]
    df = pd.read_csv(csv_path)

    build_blueprint(oqdf, df)

if __name__ == "__main__":
    main()
