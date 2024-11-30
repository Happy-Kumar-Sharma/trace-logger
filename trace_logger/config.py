import inspect
import logging

from .utils import get_trace_id

_LOGGING_CONFIGURED = False


def configure_logging(level: str):
    """
    Configures the logging level for the library.

    Args:
        level (str): The logging level (e.g., DEBUG, INFO, WARNING, ERROR,
        CRITICAL).
    """
    global _LOGGING_CONFIGURED
    if not _LOGGING_CONFIGURED:
        logging.basicConfig(
            level=getattr(logging, level.upper(), logging.INFO),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        _LOGGING_CONFIGURED = True


class TraceIDAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        trace_id = get_trace_id()
        frame = inspect.currentframe()
        calling_frame = frame.f_back.f_back.f_back
        function_name = calling_frame.f_code.co_name
        return (
            f"[trace_id: {trace_id}] [function: {function_name}] {msg}",
            kwargs,
        )  # noqa


def get_logger(name: str = __name__) -> TraceIDAdapter:
    """
    Returns a TraceIDAdapter logger with the given name.

    Args:
        name (str): The name of the logger.

    Returns:
        TraceIDAdapter: The logger instance.
    """
    logger = logging.getLogger(name)
    if not logging.getLogger().hasHandlers():
        configure_logging(level="DEBUG")
        logger.warning(
            "No logging configuration detected. Consider calling "
            "configure_logging()."
        )
    return TraceIDAdapter(logger, {})
