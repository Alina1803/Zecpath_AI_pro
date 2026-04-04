import boto3

s3 = boto3.client('s3')

def upload_file(file_path, bucket_name, key):
    s3.upload_file(r"E:\Zecpath_AI_pro\data\raw", f"https://drive.google.com/drive/folders/10S7B4NN0sYGeK-pXaqVfkCOr7OXoen4Z?usp=sharing", key)

