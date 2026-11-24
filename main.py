"""Weirdest Job Title: Blind Judge Showdown — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a single job title, the weirdest one possible, 60 characters or fewer and nothing else.
"""
import os

LINE = "Senior Vice President of Waiting for the Wi-Fi to Come Back"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
