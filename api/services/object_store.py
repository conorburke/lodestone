import os

from fastapi import UploadFile
from minio import Minio

from utils.logger import create_stream_logger

logger = create_stream_logger(__name__)

client = Minio('minio:9000', 
               access_key=os.environ.get('MINIO_ACCESS_KEY'),
               secret_key=os.environ.get('MINIO_SECRET_KEY'),
               secure=False)

def create_bucket(name: str):
    # check if bucket already exists
    found = client.bucket_exists(name)
    # create bucket if it does not exist
    if not found:
        logger.info(f"Creating bucket '{name}'.")
        client.make_bucket(name, )
    else:
        logger.info(f"Bucket '{name}' already exists")

def send_file_to_store(bucket: str, file: UploadFile):
    file_size = os.fstat(file.file.fileno()).st_size
    return client.put_object(bucket, file.filename, file.file, file_size)