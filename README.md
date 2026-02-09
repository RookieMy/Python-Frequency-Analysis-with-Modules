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
  "a number of used" : 1 - using percentage: 3.571428571428571%,
  "b number of used" : 2 - using percentage: 7.142857142857142%,
  "c number of used" : 0 - using percentage: 0.0%,
  "ç number of used" : 1 - using percentage: 3.571428571428571%,
  "d number of used" : 0 - using percentage: 0.0%,
  "e number of used" : 2 - using percentage: 7.142857142857142%,
  "f number of used" : 0 - using percentage: 0.0%,
  "g number of used" : 1 - using percentage: 3.571428571428571%,
  "ğ number of used" : 0 - using percentage: 0.0%,
  "h number of used" : 1 - using percentage: 3.571428571428571%,
  "ı number of used" : 0 - using percentage: 0.0%,
  "i number of used" : 2 - using percentage: 7.142857142857142%,
  "j number of used" : 0 - using percentage: 0.0%,
  "k number of used" : 1 - using percentage: 3.571428571428571%,
  "l number of used" : 2 - using percentage: 7.142857142857142%,
  "m number of used" : 0 - using percentage: 0.0%,
  "n number of used" : 1 - using percentage: 3.571428571428571%,
  "o number of used" : 1 - using percentage: 3.571428571428571%,
  "ö number of used" : 0 - using percentage: 0.0%,
  "p number of used" : 0 - using percentage: 0.0%,
  "r number of used" : 2 - using percentage: 7.142857142857142%,
  "s number of used" : 1 - using percentage: 3.571428571428571%,
  "ş number of used" : 1 - using percentage: 3.571428571428571%,
  "t number of used" : 1 - using percentage: 3.571428571428571%,
  "u number of used" : 1 - using percentage: 3.571428571428571%,
  "ü number of used" : 1 - using percentage: 3.571428571428571%,
  "v number of used" : 0 - using percentage: 0.0%,
  "y number of used" : 0 - using percentage: 0.0%,
  "z number of used" : 1 - using percentage: 3.571428571428571%
}

---

## How to run

```bash
python freqAnalysis.py
