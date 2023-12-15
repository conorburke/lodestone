from fastapi import APIRouter, UploadFile, HTTPException
from services.object_store import create_bucket, send_file_to_store
from utils.logger import create_stream_logger

router = APIRouter(prefix='/v1/files')

logger = create_stream_logger(__name__)

bucket_name = 'raw-data-bucket'

create_bucket(bucket_name)

@router.get('/')
def index():
    return "File Router"


@router.post('/')
async def upload_file(file: UploadFile):
    try:
        store_response = send_file_to_store(bucket_name, file)
        logger.info(f'Created object with key: {store_response.etag}')
        return {
            "filename": file.filename,
            "etag": store_response.etag,
            "bucket": bucket_name,
            "object_name": store_response.object_name
        }
    except:
        return HTTPException(500, 'Error processing file.')