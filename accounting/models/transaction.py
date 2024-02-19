from datetime import date
from accounting.models.account import Account
from accounting.models.entity import Entity
from accounting.models.vendor import Vendor
from dataclasses import dataclass

@dataclass
class Transaction(Entity):
  vendor: Vendor
  payee: Account
  timestamp: date
  verified: bool
