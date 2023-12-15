from fastapi import FastAPI
from routers.file_router import router
from utils.logger import create_stream_logger
from models.db import create_engine

create_engine()

app = FastAPI(debug=True)
app.include_router(router)

logger = create_stream_logger(__name__)

logger.info('App starting...')

@app.get('/')
def index():
    return "Indexxx"