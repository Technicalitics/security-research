# Security Research Portfolio

**One security domain per week.** A systematic approach to building practical cybersecurity skills through hands-on challenges across reverse engineering, web application security, cryptography, network analysis, and binary exploitation.

**Portfolio Metrics:** 2/6 domains | 10+ techniques | Updated weekly through Spring 2026

---

## Featured Projects

### Reverse Engineering: Crackme Username/Serial Validation
*November 2025 | crackmes.one*

Reverse engineered ASMboy's "segfault" validation algorithm through static analysis. Reconstructed serial generation logic by analyzing username transformation and integer conversion operations, identifying input validation weaknesses.

**Impact**: Demonstrates binary analysis for vulnerability discovery  
**Skills**: Ghidra, x86-64 assembly, algorithm reconstruction  
**[View Writeup →](reverse-engineering/crackme-segfault/)**

---

### Web Security: SQL Injection - Authentication Bypass & WAF Evasion
*November 2025 | PortSwigger Web Security Academy*

Defeated authentication controls through SQL comment injection, then bypassed XML parsing filters using entity encoding to circumvent WAF protections. Analyzed filter processing order to identify logic gaps exploitable through encoding variations.

**Impact**: Shows capability to identify and exploit defense-in-depth failures
**Skills**: SQL injection, XML encoding, filter bypass analysis, CyberChef
**[View Writeup →](web-security/sql-injection-fundamentals/)**

---

### Cryptography
*Coming December 2025*

---

### Network Security
*Coming December 2025*

---

### Binary Exploitation
*Coming January 2026*

---

### Integration Challenge
*Coming January 2026*

---

## Approach

Each project follows structured methodology:

1. **Reconnaissance**: Systematic attack surface enumeration and constraint identification
2. **Analysis**: Tool-assisted investigation (static/dynamic analysis, traffic inspection)
3. **Exploitation**: Iterative technique development and validation
4. **Documentation**: Professional writeups with defensive mitigation recommendations

Projects balance breadth across security domains with progressive depth within each area.

---

## Tools & Technologies

**Analysis**: Ghidra, GDB, Burp Suite, Wireshark, CyberChef  
**Languages**: Python, SQL, x86-64 assembly, Bash  
**Platforms**: PortSwigger Academy, crackmes.one, HackTheBox, CTFtime  

---

## About This Portfolio

Building practical cybersecurity capabilities through systematic hands-on research. This repository documents technical projects across six security domains, demonstrating vulnerability analysis, exploitation techniques, and defensive thinking.

**Learning Strategy**: One focused domain per week, progressing from foundational to advanced techniques.

**Why Public Documentation**: Security work requires clear technical communication. These writeups practice explaining complex vulnerabilities and methodologies to diverse audiences.

---

## Repository Standards

- All writeups include defensive mitigation analysis
- Professional documentation with reproducible methodology
- Weekly updates through Spring 2026
- Projects selected from recognized security platforms

---

*This portfolio represents ongoing skill development through hands-on security research demonstrating practical capabilities across the cybersecurity domain spectrum.*
