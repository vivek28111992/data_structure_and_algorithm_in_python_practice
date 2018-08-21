# A Geometric Progression Class
# A class that produces a geometric progression.

from progression import Progression

class GeometricProgression(Progression):                    # inherit from Progression
    """Iterator producing a geometric progression."""

    def __init__(self, base = 2, start = 1):
        """Create a new geometric progression.

        base                    the fixed constant multiplied to each term (default 2)
        start                   the first term of the progression (default 1)
        """

        super().__init__(start)
        self._base = base
    
    def _advance(self):                 # override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *= self._base
