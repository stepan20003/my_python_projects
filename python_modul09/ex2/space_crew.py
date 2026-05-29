from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_lenght=3, max_lenght=10)
    name: str = Field(min_lenght=2, max_lenght=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_lenght=3, max_lenght=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> "SpaceMission":
        first = False
        count = 0
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for i in self.crew:
            if i.rank == Rank.CAPTAIN or i.rank == Rank.COMMANDER:
                first = True
        if not first:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            for i in self.crew:
                count += i.years_experience
            if count / len(self.crew) <= 5:
                raise ValueError("Long missions (> 365 days)"
                                 " need 50% experienced crew (5+ years)")
        for i in self.crew:
            if not i.is_active:
                raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("="*40)
    print("Valid mission created:")
    valid_data = {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 900,
        'budget_millions': 2500.0,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Connor',
                'rank': 'commander',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'John Smith',
                'rank': 'lieutenant',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Alice Johnson',
                'rank': 'officer',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },

        ]
    }
    try:
        mission = SpaceMission(**valid_data)

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")

        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} "
                f"({member.rank.value}) - "
                f"{member.specialization}"
            )

    except (ValueError, ValidationError) as e:
        print(e)
    print("=" * 41)
    invalid_data = {
        "mission_id": "M2024_FAIL",
        "mission_name": "Failed Mission",
        "destination": "Moon",
        "launch_date": "2024-06-01T00:00:00",
        "duration_days": 100,
        "budget_millions": 500.0,
        "crew": [
            {
                "member_id": "CM010",
                "name": "Bob Wilson",
                "rank": "officer",
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 3,
                "is_active": True
            }
        ]
    }

    try:
        SpaceMission(**invalid_data)

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"][13:])
