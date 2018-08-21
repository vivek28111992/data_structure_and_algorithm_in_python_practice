# Fibonacci Progression
# A class that produces a Fibonacci progression

from progression import Progression

class FibonacciProgresion(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first = 0, second = 1):
        """Create a new fibonacci progression.

        first                   the first term of the progression (default 0)
        second                  the second term of the progression (default 1)
        """

        super.__init__(first)           # start progression at first
        self._prev = second - first     # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current
