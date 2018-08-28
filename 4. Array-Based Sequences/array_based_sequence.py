# Using Array-Based Sequences
# Python code for a Scoreboard class that maintains an ordered series of scores as GameEntry objects.

class Scoreboard:
    """Fixed-length sequence of the high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self._board = [None] * capacity                 # reserve space for future scores
        self._n = 0                                     # number of actual entries

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry quality as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):                  # no score drops from list
                self._n += 1                                # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]         # shift entry from j-1 to j
                j -= 1                                      # and decrement j
            self._board[j] = entry                          # when done, add new entry
