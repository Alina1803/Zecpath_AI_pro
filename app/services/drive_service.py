import gdown
import os

output_path = r"E:\Zecpath_AI_pro\data\processed"

def download_file_from_drive(file_id, output_path):
    url = f"https://drive.google.com/drive/folders/10S7B4NN0sYGeK-pXaqVfkCOr7OXoen4Z?usp=sharing"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    gdown.download(url, output_path, quiet=False)
    
    return output_path