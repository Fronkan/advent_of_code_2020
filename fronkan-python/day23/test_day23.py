import importlib
import pytest
from pathlib import Path

DIRECTORY = Path(__file__).parent

solution = importlib.import_module(f"{DIRECTORY.name}.solution")


@pytest.mark.parametrize(
    "puzzle, result", [(1, 67384529), (2, 149245887792)],
)
def test_puzzle_example_input(puzzle, result):
    input_file = Path(__file__).parent / "example_input.txt"
    puzzle_solver = getattr(solution, f"puzzle{puzzle}")
    assert puzzle_solver(input_file) == result


@pytest.mark.parametrize(
    "puzzle, result", [(1, 95648732), (2, 192515314252)],
)
def test_puzzle_real_input(puzzle, result):
    input_file = Path(__file__).parent / "input.txt"
    puzzle_solver = getattr(solution, f"puzzle{puzzle}")
    assert puzzle_solver(input_file) == result