from typing import TypeVar, Generic

K = TypeVar("K")
V = TypeVar("V")


class Dict(Generic[K, V]):

    def __init__(self, number_of_buckets: int = 19):
        self._buckets: list[list[tuple[K, V]]] = [[] for i in range(number_of_buckets)]
        self._size: int = 0

    def __getitem__(self, search_key: K) -> V:
        bucket_number: int = hash(search_key) % len(self._buckets)
        for key, value in self._buckets[bucket_number]:
            if search_key == key:
                return value
        raise KeyError

    def __setitem__(self, search_key, value):
        bucket_number: int = hash(search_key) % len(self._buckets)
        i: int = 0
        for key, value in self._buckets[bucket_number]:
            if search_key == key:
                self._buckets[bucket_number][i] = (search_key, value)
            i += 1
        self._buckets[bucket_number].append((search_key, value))

    def bucket_sizes(self) -> list[int]:
        return list(map(len, self._buckets))

