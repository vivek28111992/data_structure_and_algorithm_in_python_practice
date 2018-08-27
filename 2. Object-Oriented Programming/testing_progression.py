# Testing Our Progressions
# Unit tests for our progression classes.

from progression import Progression
from arithmetic_progression import ArithmeticProgression
from geometeric_progression import GeometricProgression
from fibonacci_progression import FibonacciProgresion

if __name__ == '__main__':
    print('Default Progression:')
    Progression().print_progression(10)

    print('Arthmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arthmetic progression with increment 5 & start 2:')
    ArithmeticProgression(5, 2).print_progression(10)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgresion().print_progression(10)

    print('Fibonacci progression with start values 4 & 6:')
    FibonacciProgresion(4, 6).print_progression(10)
