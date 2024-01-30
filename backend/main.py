import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api.api_router import router
from core.config import settings, initiate_database
from helpers.exception_handler import CustomException, http_exception_handler

config_log = settings.LOGGING_CONFIG_FILE

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initiate_database()
    yield

def get_application() -> FastAPI:
    application = FastAPI(
        lifespan=lifespan,
        # title=settings.PROJECT_NAME, docs_url="/docs", redoc_url='/re-docs',
        # openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description='''
        Base frame with FastAPI micro framework + Postgresql
            - Login/Register with JWT
            - Permission
            - CRUD User
            - Unit testing with Pytest
            - Dockerize
        '''
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router, prefix=settings.API_PREFIX)
    application.add_exception_handler(CustomException, http_exception_handler)
    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=6543, log_config=config_log)
