from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional


class ContactType(str, Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self) -> "AlienContact":
        if not (self.contact_id[0] == 'A' and self.contact_id[1] == 'C'):
            raise ValueError("Contact ID must start with 'AC'.")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic \
           and self.witness_count < 3:
            raise ValueError("Telepathic contact requires"
                             " at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include"
                             " received messages")
        return self


def printer(obj: AlienContact) -> None:
    print(f"ID: {obj.contact_id}")
    print(f"Type: {obj.contact_type}")
    print(f"Location: {obj.location}")
    print(f"Signal: {obj.signal_strength}/10")
    print(f"Duration: {obj.duration_minutes} minutes")
    print(f"Witness: {obj.witness_count}")
    print(f"Message: '{obj.message_received}'")


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("="*40)
    print("Valid contact report:")
    try:
        data = {
            "contact_id": "AC_2024_001",
            "timestamp": "2026-05-26T19:15:00",
            "location": "Area 51, Nevada",
            "contact_type": "radio",
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 5,
            "message_received": "Greetings from Zeta Reticuli",
            "is_verified": True
        }
        report = AlienContact.model_validate(data)
        printer(report)
        print("\n")

    except (ValueError, ValidationError) as e:
        print(e)
    print("="*40)
    print("Expected validation error:")
    try:
        invalid_report = {
            "contact_id": "AC_2024_003",
            "timestamp": "2024-11-15T00:00:00",
            "location": "Very Large Array, New Mexico",
            "contact_type": "telepathic",
            "signal_strength": 4.5,
            "duration_minutes": 10,
            "witness_count": 2,
            "message_received": "Null",
            "is_verified": False
        }
        invalid_reportreport = AlienContact.model_validate(invalid_report)
        printer(invalid_reportreport)

    except ValidationError as e:
        print(e.errors()[0]["msg"])
