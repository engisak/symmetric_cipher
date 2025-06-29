# 🔐 Symmetric Encryption Algorithm with KDF (Key Derivation Function)

## 📖 Overview

This project implements a **custom symmetric encryption algorithm** that enhances traditional techniques by applying a **per-round dynamic key generation** method. The encryption system operates with a static master key and derives a new key for each encryption round, significantly improving resistance to cryptanalysis such as key reuse attacks and pattern detection.

## 🎯 Goal

To improve the **security, confusion, and diffusion** of symmetric encryption through:

* Per-round key derivation (KDF)
* Position-based transformation
* Round-aware computation
* Character-indexing based on a strict 72-character set

## 🔑 Key Features

* Uses a **static master key** of 8 integers
* Generates a new round key each round via XOR:

  ```
  RoundKey[i] = (MasterKey[i] XOR Round) mod 10
  ```
* Encryption formula:

  ```
  NewIndex = (OldIndex XOR Key[i % 8] + Position + Round) mod 72
  ```
* Decryption formula:

  ```
  OldIndex = ((NewIndex - (Position + Round)) mod 72) XOR Key[i % 8]
  ```
* Uses a fixed **72-character charset**:

  ```
  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()
  ```
* Supports multi-round encryption for stronger diffusion
* GUI built with Tkinter for ease of use

## 🧪 Example

Given:

* Plaintext: `you`
* Master Key: `[3, 1, 4, 1, 5, 9, 2, 6]`
* Rounds: `2`

The algorithm:

* Adds salt: `@#you`
* Round 1 key: derived using KDF
* Round 2 key: different from round 1
* Produces encrypted output: `$&%0!`
* Can successfully reverse to original plaintext

## 📦 GUI Application

The application includes a GUI interface built with Tkinter.

### Features:

* User input for plaintext or ciphertext
* Select encryption or decryption
* Specify number of rounds
* Provide master key (8 space-separated integers)
* Displays the result clearly

## 🚀 How to Run

1. Clone or download the repository.
2. Open terminal or command prompt.
3. Run the GUI:

   ```bash
   python symmetric_cipher.py
   ```
4. Follow the prompts in the window to encrypt or decrypt messages.

## 📂 Files

* `symmetric_cipher` – GUI application
* `README.md` – Project documentation

## 📌 Use Case

This encryption tool is educational and ideal for demonstrating key cryptographic concepts:

* Symmetric key encryption
* XOR logic
* Key derivation per round
* Index mapping and modular math

## ⚠️ Disclaimer

This is a custom-designed algorithm built for **educational purposes only**. It is **not recommended for securing sensitive or real-world data**.

---

© 2025 — Designed by **GROUP 3** | Final Year Cryptography Project
