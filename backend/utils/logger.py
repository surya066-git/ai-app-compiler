import logging
import sys
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Avoid duplicate handlers if setup_logger is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)
        
    return logger

app_logger = setup_logger("app_compiler")
