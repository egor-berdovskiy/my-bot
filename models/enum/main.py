from enum import Enum
from models.language import Language


class AvaiableLanguages(Enum):
    RU = Language('RU', '🇷🇺')
    EN = Language('EN', '🇬🇧')
