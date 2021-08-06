---
title: "Python 3 notes"
draft: true
---

# [Unicode](https://docs.python.org/3/howto/unicode.html#unicode-howto)

- The [Unicode](https://www.unicode.org/) standard describes how characters are represented by **code points**.  A code point value is an integer in the range 0 to 0x10FFFF. A code point is written using the notation `U+265E` to mean the character with value `0x265e` (9,822 in decimal).
- A unicode code point is not a character but represents a character
- A character is represented on a screen or on paper by a set of graphical elements that’s called a **glyph** (not important to python)

## Encodings

> a Unicode string is a sequence of code points, which are numbers from 0 through `0x10FFFF` (1,114,111 decimal). This sequence of code points needs to be represented in memory as a set of **code units**, and **code units** are then mapped to 8-bit bytes. The rules for translating a Unicode string into a sequence of bytes are called a **character encoding**, or just an **encoding**

### UTF-8 encoding

> UTF stands for “Unicode Transformation Format”, and the ‘8’ means that 8-bit values are used in the encoding. 

- Plays well with C functions.
- A string of ASCII text is also valid UTF-8 text. UTF-8 is a byte oriented encoding. 
- The encoding specifies that each character is represented by a specific sequence of one or more bytes

## [The string type](https://docs.python.org/3/howto/unicode.html#the-string-type)

> the language’s [`str`](https://docs.python.org/3/library/stdtypes.html#str) type contains Unicode characters, meaning any string created using `"unicode rocks!"`, `'unicode rocks!'`, or the triple-quoted string syntax is stored as Unicode

- `"\N{GREEK CAPITAL LETTER DELTA}" == "\u0394"  == "\U00000394"`	
- **bytes** can be decoded to string : `b'\x41'.decode("utf-8")` outputs 'A'
- `bytes.decode` as options for dealing with bytes unknown to the encoding.
- The opposite method of [bytes.decode()](https://docs.python.org/3/library/stdtypes.html#bytes.decode) is [str.encode()](https://docs.python.org/3/library/stdtypes.html#str.encode), which returns a [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) representation of the Unicode string, encoded in the requested *encoding*

