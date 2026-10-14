import csv
import os
import time
import pytest
from tests.test import generate_sample
from algorithms.two_pointers import two_pointers
from algorithms.binary_search import binary_search
from algorithms.exponential_search import exponential_search
from algorithms.double_binary_search import double_binary_search

CSV_FILE = "data/results.csv"

@pytest.fixture(scope="session", autouse=True)
def setup_csv():
    os.makedirs("data", exist_ok=True)
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["scenario", "m", "n", "ratio", "algorithm", "time_sec"])

ALGORITHMS = {
    "two_pointers": two_pointers,
    "binary_search": binary_search,
    "exponential_search": exponential_search,
    "double_binary_search": double_binary_search,
}

@pytest.mark.parametrize("scenario, m, n", [
    # 1. M = N (симметричный рост от 100 до 300 000)
    ("equal_sizes", 100, 100),
    ("equal_sizes", 1000, 1000),
    ("equal_sizes", 5000, 5000),
    ("equal_sizes", 10000, 10000),
    ("equal_sizes", 50000, 50000),
    ("equal_sizes", 100000, 100000),
    ("equal_sizes", 300000, 300000),

    # 2. M << N (фиксированный маленький M = 50, растущий N до 1 000 000)
    ("fixed_m", 50, 500),
    ("fixed_m", 50, 2000),
    ("fixed_m", 50, 10000),
    ("fixed_m", 50, 50000),
    ("fixed_m", 50, 200000),
    ("fixed_m", 50, 1000000),

    # 3. Переменное отношение N / M (M = 100, N растет)
    ("varying_ratio", 100, 100),
    ("varying_ratio", 100, 500),
    ("varying_ratio", 100, 2000),
    ("varying_ratio", 100, 10000),
    ("varying_ratio", 100, 50000),
    ("varying_ratio", 100, 200000),
])
def test_benchmark(scenario, m, n):
    a, b, _ = generate_sample(m, n, has_common=0)

    rows = []

    for name, algo in ALGORITHMS.items():
        start = time.perf_counter()
        res = algo(a, b)
        elapsed = time.perf_counter() - start

        assert res is False
        rows.append([scenario, m, n, round(n / m, 4), name, elapsed])
        print(f"\n{scenario} (M={m}, N={n}) -> {name}: {elapsed:.6f}s")


    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)