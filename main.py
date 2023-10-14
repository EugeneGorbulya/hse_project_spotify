import pandas as pd
import argparse
from typing import List, Dict


def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()

def get_year_stats(table: List) -> Dict:
    d = dict()
    for el in table:
        if el[1] in d:
            d[el[1]]+=1
        else:
            d[el[1]] = 1
    return d




if __name__ == "__main__":

    # придумываем аргументы, которые сможет прочитать прога
    parser = argparse.ArgumentParser(description="our little spotify experience")

    parser.add_argument("file_path", type=str, help="input path to our datasheet")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Shows more info during script run"
    )
    # парсим аргументы в переменные
    args = parser.parse_args()

    if args.verbose:
        print(args)
        print("Hello world")
        print(f"File path: {args.file_path}")

    table = open_file(args.file_path)
    s = get_year_stats(table)
    print(s)
    print(len(table))
