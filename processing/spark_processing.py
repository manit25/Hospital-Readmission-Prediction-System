import pandas as pd
import os

def process_data(input_path, output_path):
    df = pd.read_csv(input_path)

    df = df.drop(columns=["weight", "payer_code", "medical_specialty"], errors='ignore')
    df = df.fillna("Unknown")

    df["readmitted_flag"] = (df["readmitted"] == "<30").astype(int)

    df = df[["age","time_in_hospital","num_lab_procedures",
             "num_medications","number_outpatient",
             "number_emergency","number_inpatient",
             "readmitted_flag"]]

    os.makedirs(output_path, exist_ok=True)
    df.to_csv(os.path.join(output_path, "processed_data.csv"), index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    input_path = os.path.join(project_root, "data", "raw", "diabetic_data", "diabetic_data.csv")
    output_path = os.path.join(project_root, "data", "processed")
    
    process_data(input_path, output_path)
