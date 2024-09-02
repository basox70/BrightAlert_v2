import os, yaml, sys, logging
from logging.handlers import RotatingFileHandler
try:
    from cysystemd.journal import JournaldLogHandler
except ImportError:
    JournaldLogHandler = None

# region Logging configuration
class LoggingFormatter(logging.Formatter):
    # Colors
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)

def get_log_data():
    conf = type('Config', (), {})
    if not os.path.isfile("config.yml"):
        sys.exit(f"\"config.yml\" not found! Please add it and try again.")
    else:
        with open("config.yml") as file:
            config = yaml.safe_load(file)
            for k in config:
                if isinstance(config[k], dict):
                    setattr(conf, k, type('dict', (), config[k]))
                else:
                    setattr(conf, k, config[k])
    return conf



def configure_logger():
    cfg = get_log_data()
    logger = logging.getLogger("discord_bot")
    discord_logger = logging.getLogger('discord')
    logger.setLevel(cfg.log.debug_level)
    discord_logger.setLevel(cfg.log.debug_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(LoggingFormatter())
    logger.addHandler(console_handler)
    discord_logger.addHandler(console_handler)

    # Rotating file handler
    rotating_file_handler = RotatingFileHandler(filename=f'logs/{cfg.bot_name}.log', mode="w", maxBytes=cfg.log.max_bytes, backupCount=cfg.log.backup_count, encoding="utf-8")
    rotating_file_formatter = logging.Formatter("%(asctime)s - %(process)d - %(name)s - [%(levelname)s] - %(message)s", datefmt='%y%m%d_%H%M%S')
    rotating_file_handler.setFormatter(rotating_file_formatter)
    logger.addHandler(rotating_file_handler)
    discord_logger.addHandler(rotating_file_handler)

    # systemd handler
    if JournaldLogHandler:
        journal_handler = JournaldLogHandler()
        syslog_formatter = logging.Formatter("%(asctime)s - %(process)d - %(name)s - [%(levelname)s] - %(message)s", datefmt='%y%m%d_%H%M%S')
        journal_handler.setFormatter(syslog_formatter)
        logger.addHandler(journal_handler)
        discord_logger.addHandler(journal_handler)

    return logger


logger = configure_logger()