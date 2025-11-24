# Problem Statement

Lots of people are creating **easy-to-guess passwords** for their online accounts. These weak passwords make accounts vulnerable to common hacking methods like **brute force** (trying every possible combination), **dictionary attacks** (using common words), and **social engineering** (tricking people). This is a big risk for everyone, from individuals to large companies. We clearly need a simple tool that can check how strong a password is and give **helpful tips** on how to make it safer. 


## Scope of Project

This project aims to build a smart **password checker program using Python**. This tool will look at passwords and grade them based on several key factors:

* **Length:** Checking that the password is long enough (it should meet a minimum and ideal length).
* **Complexity (Mix of Characters):** Checking if the password uses a good combination of different character types (like **BIG letters**, **small letters**, **numbers**, and **special symbols**).
* **Use of Special Characters:** Making sure the password includes and uses various symbols or punctuation marks.
* **Resistance to Common Attack Patterns:** Making sure the password avoids common, easy-to-guess patterns like simple sequences ("123456"), dictionary words, or common names.

In the end, the tool will give a **final strength score** and clear, practical **suggestions on what to fix**.


## Target Users

This tool is designed to be useful for three main groups of people who care about digital security:

* **Everyday users** who just want to quickly check if the passwords they use for their personal accounts are safe.
* **Tech experts and security hobbyists** who need a fast, reliable tool for testing security rules or checking potential weak spots.
* **Companies and organizations** that want to use the tool in training sessions to teach their employees how to create strong and unique passwords.


## High-level Features

The Password Strength Analyzer will have these main capabilities:

* **Analyze password strength based on many factors at once:** The tool won't just look at one thing; it will check the length, character mix, and common patterns all at the same time to decide the overall safety level.
* **Provide a number grade and simple feedback:** It will give a number grade (e.g., from 0 to 100) and immediately translate that into an easy-to-understand rating (like **"Too Weak"**, **"Medium"**, or **"Excellent"**).
* **Suggest improvements for weak passwords:** If a password is weak, the tool will tell the user exactly what's missing (e.g., "You need to add a capital letter," or "Make the password 4 characters longer").
* **Simple, easy-to-use text box interface:** The main way users interact with the tool will be through a basic **command-line window**, making it quick to use without needing complicated menus or setups.
