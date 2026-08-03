from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class Command:


    # Original input
    raw: str



    # Normalized input
    normalized: str = ""



    # Intent
    intent: str | None = None



    # Entities
    entities: dict = field(
        default_factory=dict
    )



    # Confidence
    confidence: float = 0.0



    # Source
    source: str = "voice"



    # Context
    context: dict = field(
        default_factory=dict
    )



    # Time
    timestamp: datetime = field(
        default_factory=datetime.now
    )



    def __post_init__(self):


        if not self.normalized:


            self.normalized = (
                self.raw
                .lower()
                .strip()
            )