import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.interface.errors.http_error import http_error_handler
from app.interface.errors.validation_error import http422_error_handler
from app.interface.api import router as api_router
from app.settings.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.settings.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler())
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
