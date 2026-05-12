from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class CrewRank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    # Lista entre 1 y 12 miembros
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    #  Valor por defecto
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_business_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in [CrewRank.COMMANDER, CrewRank.CAPTAIN]
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need at least 50% experienced crew"
                )

        all_active = all(member.is_active for member in self.crew)
        if not all_active:
            raise ValueError(
                "All Crew Members must be active"
            )
        return self


def main() -> None:
    try:
        valid_mission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            launch_date=datetime.now(),
            # Nested porque primero valida CrewMember y luego SpaceMission
            crew=[
                    CrewMember(
                        member_id="C001",
                        name="Sarah Connor",
                        rank=CrewRank.COMMANDER,
                        age=45,
                        specialization="Mission Command",
                        years_experience=15
                    ),
                    CrewMember(
                        member_id="C002",
                        name="John Smith",
                        rank=CrewRank.LIEUTENANT,
                        age=35,
                        specialization="Navigation",
                        years_experience=9
                    ),
                    CrewMember(
                        member_id="C003",
                        name="Alice Johnson",
                        rank=CrewRank.OFFICER,
                        age=40,
                        specialization="Engineering",
                        years_experience=3
                    )
                ]
            )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"- {member.name} "
                f"({member.rank.value}) "
                f"- {member.specialization}"
            )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print()
    print("=" * 40,)

    try:
        SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            launch_date=datetime.now(),
            crew=[
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=CrewRank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=3
                )
            ]
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=" * 40)
    main()
