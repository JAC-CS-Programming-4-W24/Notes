## 🎯 Objectives

- Practice making class objects that are comparable

## 🔨 Setup

Make sure you are using `python3.10` or later.

Create two new files, `pokemon.py` and copy the code (shown below)
into the appropriate files.


## 🚦 Let's Go

1. Implement the `Pokemon` class to track the Pokemon's `name`, `type`, and `level`.
   - Use an [`enum`](https://docs.python.org/3.11/howto/enum.html#enum-basic-tutorial) for the `type`.
2. Override the "__lt__" and "__eq__" functions so that Pokemon can be compared
3. For comparisons
   - The order priority is: 
     - first by `name` (alphabetical) 
     - and then by `level` (increasing).
   - Ex. A Bulbasaur is "less than" a Charmander because B comes before C alphabetically.
   - Ex. A level 1 Bulbasaur is "less than" a level 2 Bulbasaur because while their names are the same, their levels are not.
   - Ex. A level 1 Bulbasaur is "equal to" another level 1 Bulbasaur because both their names and levels are the same.


Starting code: (`pokeman.py`)
```python
from typing import Protocol
from enum import Enum


class PokemonType(Enum):
    FIRE = 1
    WATER = 2
    GRASS = 3


def main():
    """
        To Do:
            * Instantiate two Pokémon here with different names and levels.
            * Verify that your code works by doing simple comparisons
            * Run the first test in PokemonTest to verify that creation is working.
            * Run the second test in PokemonTest to verify that the comparisons are working.
    """


class Pokemon:
    """ Implement the Pokémon class using the Compare Protocol """


if __name__ == "__main__":
    main()
```

