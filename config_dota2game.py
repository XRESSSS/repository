import dataclasses


@dataclasses.dataclass(frozen=True)
class BeastParametrs:
    HEALTH_POINTS = 220
    POWER = 60
    ACCURACY = 30

class TrollParametrs:
    POWER = 25
    ACCURACY = 90