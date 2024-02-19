from typing import List, TypeVar
from accounting.models.entity import Entity

T = TypeVar("T", Entity)

class Repository:

  def findOne(predicate: callable[[Entity], bool]) -> T:
    pass

  def findAll(predicate: callable[[Entity], bool]) -> List[T]:
    pass

  def create(entity: Entity) -> Entity:
    pass

  def update(entity: Entity) -> Entity:
    pass

  def delete(entity: Entity) -> Entity:
    pass