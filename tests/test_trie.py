import json
from typing import Any

from .helpers import sanitize, remove_hex_prefix
from eth1spec import rlp
from eth1spec.trie import map_keys, root


def test_trie_secure_hex() -> None:
    tests = load_tests("hex_encoded_securetrie_test.json")

    for (name, test) in tests.items():
        normalized = {}
        for (k, v) in test.get("in").items():
            normalized[sanitize(k)] = sanitize(v)

        result = root(map_keys(normalized))
        expected = remove_hex_prefix(test.get("root"))
        assert result.hex() == expected, f"test {name} failed"


def test_trie_secure() -> None:
    tests = load_tests("trietest_secureTrie.json")

    for (name, test) in tests.items():
        normalized = {}
        for t in test.get("in"):
            normalized[sanitize(t[0])] = sanitize(t[1])

        result = root(map_keys(normalized))
        expected = remove_hex_prefix(test.get("root"))
        assert result.hex() == expected, f"test {name} failed"


def test_trie_secure_any_order() -> None:
    tests = load_tests("trieanyorder_secureTrie.json")

    for (name, test) in tests.items():
        normalized = {}
        for (k, v) in test.get("in").items():
            normalized[sanitize(k)] = sanitize(v)

        result = root(map_keys(normalized))
        expected = remove_hex_prefix(test.get("root"))
        assert result.hex() == expected, f"test {name} failed"


def test_trie() -> None:
    tests = load_tests("trietest.json")

    for (name, test) in tests.items():
        normalized = {}
        for t in test.get("in"):
            normalized[sanitize(t[0])] = sanitize(t[1])

        print(name)
        result = root(map_keys(normalized, secured=False))
        expected = remove_hex_prefix(test.get("root"))
        assert result.hex() == expected, f"test {name} failed"


#  def test_trie_any_order() -> None:
#      tests = load_tests("trieanyorder.json")

#      for (name, test) in tests.items():
#          normalized = {}
#          for (k, v) in test.get("in").items():
#              normalized[sanitize(k)] = sanitize(v)

#          result = root(map_keys(normalized, secured=False))
#          expected = remove_hex_prefix(test.get("root"))
#          assert result.hex() == expected, f"test {name} failed"


def load_tests(path: str) -> Any:
    with open("tests/fixtures/TrieTests/" + path) as f:
        tests = json.load(f)

    return tests