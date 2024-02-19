from dataclasses import dataclass
from accounting.models.entity import Entity

@dataclass
class Account(Entity):
  user_name: str
  address: str
  email: str
  balance: float
