# Turkish Letter Frequency Analysis (Python)

This project performs letter frequency analysis for Turkish text.
It correctly handles Turkish-specific characters such as ç, ğ, ı, ö, ş, ü.

The script counts how many times each letter appears in a given text.

---

## What does this project do?

- Converts Turkish uppercase letters to lowercase correctly
- Ignores non-letter characters
- Counts letter occurrences
- Returns the result as a dictionary

---

## Requirements

- Python 3.x  
(No external libraries required)

---

## Usage Example

## Input
İstanbul çok güzel bir şehir

## Output
{
  'i': 3,
  's': 1,
  't': 1,
  'a': 1,
  'n': 1,
  'b': 1,
  'u': 1,
  'l': 1,
  'ç': 1,
  'o': 1,
  'k': 1,
  'g': 1,
  'ü': 1,
  'z': 1,
  'e': 2,
  'r': 1,
  'b': 1,
  'ş': 1,
  'h': 1
}

---

## How to run

```bash
python freqAnalysis.py
