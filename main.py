from uuid import UUID

from fastapi import Depends, FastAPI

from trace_logger.config import configure_logging, get_logger
from trace_logger.deps import get_trace_id
from trace_logger.middleware import TraceIDMiddleware

# User explicitly configures logging
configure_logging(level="error")

app = FastAPI()
app.add_middleware(TraceIDMiddleware)

# Keep this in a common file from where you can access through out the project
logger = get_logger(__name__)


@app.get("/")
def say_hello(name: str = "Dev", trace_id: UUID = Depends(get_trace_id)):
    logger.debug("This is debug level log.")
    logger.info("This is info level log.")
    logger.error("This is error level log.")
    logger.warning("This is warning level log.")
    return {"Message": f"Hello {name}"}
