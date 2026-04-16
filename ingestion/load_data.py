import pandas as pd
import os

def load_data(path):
    df = pd.read_csv(path)
    print("Data Loaded:", df.shape)
    return df

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    input_path = os.path.join(project_root, "data", "raw", "diabetic_data", "diabetic_data.csv")
    output_path = os.path.join(project_root, "data", "processed", "raw_copy.csv")
    
    df = load_data(input_path)
    df.to_csv(output_path, index=False)
