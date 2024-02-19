from accounting.models.business import BusinessType
from accounting.models.entity import Entity
from dataclasses import dataclass

@dataclass
class Vendor(Entity):
  name: str
  address: str
  postcode: str
  type: BusinessType