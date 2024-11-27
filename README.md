# trace-logger

Populate same trace id across all logs related to each request.

* Added color log level wise.

This package patching the standard `logging` library.

Thus, after import, all improvements will be available inside the `logging` module.

### Requirements

Python 3.7 and above. with fastapi and starlette dependencies.

### Installation

`pip install api-x-trace-logger`

### Usage

#### Simple usage

```python
import api_logger

```

#### More advanced usage

```python
import api_logger
# Or, if you want to configure color formatter:
handler = logging.colorfullogs(True)

```
