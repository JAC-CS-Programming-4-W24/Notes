from __future__ import annotations

from typing import Iterator
from our_dict import Dict
from report import print_table


class our_str:
    """A wrapper class around str to allow us to re-write __hash__"""

    def __init__(self, value: str):
        self._value = value

    def __iter__(self) -> Iterator[str]:
        return iter(self._value)

    def __eq__(self, other: our_str) -> bool:
        return self._value == other._value

    def __getitem__(self, index: int) -> str:
        return self._value[index]

    def __setitem__(self, key, value):
        raise NotImplementedError  # string are immutable!

    def __hash__(self) -> int:
        # Version 0
        # return 0

        # Version 1
        return len(self._value)


def main():
    names: list[our_str] = []
    with open("names.txt", "r") as names_file:
        for name in names_file:
            names.append(our_str(name))

    for number_of_buckets in [7, 19, 53, 101]:
        sample: Dict[our_str, int] = Dict(number_of_buckets)
        for name in names:
            sample[name] = 1
        print_table(f"Buckets = {number_of_buckets}", sample.bucket_sizes())


if __name__ == "__main__":
    main()
