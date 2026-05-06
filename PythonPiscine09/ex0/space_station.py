
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


# min y max es para str. ge greater o equal >=
# le less or equal <=, datetime fecha y hora
# Optional puede ser None
class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length = 3, max_length = 10)
    name: str = Field(..., min_length = 1, max_length = 50)
    crew_size: int = Field(..., ge = 1, le = 20)
    power_level: float = Field(..., ge = 0.0, le = 100.0)
    oxygen_level: float = Field(..., ge = 0.0, le = 100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default = None, max_length = 200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-01-01T12:00:00",
        is_operational=True
        )
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last maintenance: {station.last_maintenance}")
    print(f"Status: {'Operational' if station.is_operational else 'Not Operational'}")
    print("=" * 40)

    try:
        bad_station = SpaceStation(
        station_id="BAD001",
        name="Bad Station",
        crew_size=30, # Here the Error
        power_level=50.0,
        oxygen_level=50.0,
        last_maintenance="2026-01-01T12:00:00",
        is_operational=False
        )
    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

if __name__ == "__main__":
    main()