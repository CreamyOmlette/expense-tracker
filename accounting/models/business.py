from enum import Enum
from dataclasses import dataclass

@dataclass
class BusinessType(Enum):
  TRAVEL = 1
  RESTAURANT = 2
  SHOP = 3
  SERVICE = 4
  UTILITY = 5