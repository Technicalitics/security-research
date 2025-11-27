# ASMboy's "segfault" Crackme

A reverse engineering challenge from [crackmes.one](https://crackmes.one/crackme/6919feb12d267f28f69b7e5c) involving username/serial validation.

**Binary:** x86-64 ELF, not stripped
**Difficulty:** Easy
**Solution:** See [writeup.pdf](writeup.pdf) for complete analysis

---

## Challenge

The binary prompts for a username (8-12 characters) and validates a corresponding serial number. The goal is to understand the algorithm and generate valid serials for any username.

---

## Approach

### Initial Investigation
The challenge name suggested a memory corruption vulnerability. I wrote `segfault.py` using pwntools to fuzz the binary with various malicious inputs (buffer overflows, format strings, etc.).

**Result:** The binary was resilient to these attacks. The name was misleading - the actual challenge required algorithm analysis, not exploitation.

### Actual Solution
Used Ghidra to reverse engineer the username transformation and serial generation algorithm. The writeup details the complete methodology and solution.

---

## Key Findings

- Username undergoes character case alternation (even indices → lowercase, odd → uppercase)
- Serial is derived from first 8 characters using `atoi()`
- Numeric usernames (e.g., `12345678`) have trivial serials due to `atoi()` behavior
- Binary is well-protected against typical memory corruption attacks

---

## Tools Used

- **Ghidra** - Static analysis and decompilation
- **pwntools** - Fuzzing and hypothesis testing
- **Basic Unix tools** - `file`, `strings`

---

## Files

- `a.out` - Challenge binary
- `writeup.pdf` - Detailed technical writeup with screenshots and analysis
- `segfault.py` - Initial fuzzing attempt (unsuccessful but demonstrates methodology)

---

## Skills Demonstrated

- Binary reverse engineering
- Algorithm reconstruction from assembly
- Hypothesis-driven research (including pivoting from incorrect assumptions)
- Static and dynamic analysis
- Technical documentation

---

## Author

**Liam Nicoll**
Aspiring security engineer and reverse engineering enthusiast

*November 2025*
