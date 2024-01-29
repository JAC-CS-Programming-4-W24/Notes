# Exercise 2.2 - 🔍 Sort & Search

## 🎯 Objectives

- **Sort** a collection of `Comparable` objects.
- **Trace** the binary search algorithm.
- **Find** a particular object in collection of `Comparable` objects using binary search.

## 🔍 Context

By implementing a `Comparable` class in the previous exercise, we got sorting for free! 
> Any container of objects can be sorted, if the objects can be compared to each other.

Once the data is sorted, we can use binary search to search for a particular element 
in the collection.

## 🚦 Let's Go

1. Our task is to refactor the integer binary search from the notes to use our `Pokemon` comparable class instead.
   - The end goal is to `Pokemon.binary_search()` for any Pokemon that may exist in our collection.
2. Now that we can (efficiently) search for a `Pokemon` in our collection, we want to be able to add a Pokemon from our `collection` to our `team` using the `Pokemon.add_to_team()` method.
   - The "collection" is the set of all Pokemon we might have in storage.
   - The "team" is the set of (max) 6 Pokemon that we can carry at any one point.
   - `Pokemon.add_to_team()` should:
     1. Search (using binary search, of course) for the Pokemon we want and get the index of where the Pokemon is in the collection.
     2. If the Pokemon does not exist in the collection, then raise a `PokemonNotFoundError`.
     3. Otherwise, add the Pokemon from the collection to the team.
        - You don't have to worry about removing the Pokemon from the collection.

---

## Code
* use the file from the previous exercise.


```python
from __future__ import annotations
from typing import Optional, Protocol

class PokemonNotFoundError(Exception):
    """Raised if trying to put a pokemon card into your 'team' if you don't actually have that card"""

class PokemonTeamDeckOverflowError(Exception):
    """"Raised if there is an attempt to add more than six cards to your team deck"""

class Comparable(Protocol):
    """ If we want to be able to do a search, then the object collection must be comparable"""
    def __lt__(self, other) -> bool: 
        pass
    def __eq__(self, other) -> bool: 
        pass


def binary_search(collection: list[Comparable], obj: Comparable) -> Optional[int]:
    """
     * An implementation of binary search with comparable objects.
     * @param collection The list of objects to be searched
     * @param find an object in the collection that is equal to obj
     * @return The index of where the Pokémon resides in the collection.
    """

class Pokemon:
    
    # add the following method to your previous Pokemon class

    @staticmethod
    def add_to_team(collection: list[Pokemon], team: list[Pokemon], 
                    card: Pokemon):
        """
        * Specifies a Pokémon to be taken from the collection and added to the team.
        * @param collection All the Pokémon you own.
        * @param team The (max) 6 Pokémon directly on you at any given time.
        * @param card - a pokemon card to add to the team deck
        * @raises PokemonNotFoundError If the Pokémon cannot be found in the collection.
        * @raises PokemonTeamDeckOverflowError is you try to add more than 6 cards to your team
        """
```
