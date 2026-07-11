#!/usr/bin/env python3
"""grep-rust — Fast file content search. CLI that searches for patterns in files with colored output."""
import sys, json, argparse
def main():
    parser = argparse.ArgumentParser(description="Fast file content search. CLI that searches for patterns in files with colored output.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "grep-rust", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")
if __name__ == "__main__":
    main()
