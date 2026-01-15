from pathlib import Path
import subprocess

puml = r"""
@startuml
skinparam classAttributeIconSize 0

class Factory {
  +name: String
}

abstract class Building {
  +name: String  <<unique>>
}

class OfficeBuilding
class Warehouse
class ProductionHall

Building <|-- OfficeBuilding
Building <|-- Warehouse
Building <|-- ProductionHall

Factory "1" *-- "1..*" Building : consists of

class Employee {
  +name: String
  +dateOfBirth: Date
  +qualification: String
}

Building "1" -- "0..*" Employee : assigned

abstract class InventoryItem {
  +name: String
}

class Furniture {
  +category: String
}

class Machine {
  +powerKW: float
  +status: String
  +start(): void
  +stop(): void
}

class Material {
  +quantity: float
  +unit: String
}

class Robot {
  +model: String
  +payloadKg: float
  +executeTask(task: String): void
}

InventoryItem <|-- Furniture
InventoryItem <|-- Machine
InventoryItem <|-- Material
InventoryItem <|-- Robot

Building "1" o-- "0..*" InventoryItem : stores

note right of Building
- name is unique (constraint)
- inventory optional: 0..*
end note

@enduml
""".strip()

Path("factory_uml.puml").write_text(puml, encoding="utf-8")
print("Wrote factory_uml.puml")

# Optional: render to PNG (requires PlantUML installed + Graphviz)
# If the 'plantuml' command exists on your system, this will produce factory_uml.png
try:
    subprocess.run(["plantuml", "-tpng", "factory_uml.puml"], check=True)
    print("Rendered factory_uml.png")
except FileNotFoundError:
    print("PlantUML not found. Install PlantUML (and Graphviz) or render the .puml in an IDE.")
