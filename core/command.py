from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Command:
    """
    Universal command object used throughout NEXUS pipeline.
    """

    # Original user input
    raw: str

    # Cleaned command after normalization
    normalized: str = ""

    # Detected user intention
    intent: str | None = None

    # Extracted information
    entities: dict = field(default_factory=dict)

    # Confidence score from intent engine
    confidence: float = 0.0

    # Where command came from
    source: str = "voice"

    # Extra temporary information
    context: dict = field(default_factory=dict)

    # Creation time
    timestamp: datetime = field(
        default_factory=datetime.now
    )