""" Originally copied from the simpler https://www.geeksforgeeks.org/observer-method-python-design-patterns/"""
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Any, Callable


class EventTypeEnum(Enum):
	UPDATE_DATA = "UPDATE_DATA"
