# New Banking System - Object-Oriented Programming
This project is a fully object-oriented banking system developed in Python. The goal is to simulate real-world banking operations using OOP principles such as abstraction, encapsulation, inheritance (superclasses and subclasses), and polymorphism. The system is capable of managing clients, accounts (including savings and checking), performing transactions, tracking operations, and enforcing business rules like withdrawal limits and account history.

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Images](#images)  
- [Project Structure Diagram](#project-structure-diagram)  
- [Developer Guide](#developer-guide)  
- [About the Author](#about-the-author)

---

## Project Overview
This Python-based bank system was designed to explore and apply advanced object-oriented programming (OOP) concepts in practice. The system uses:

- **Superclasses and Concrete Subclasses:** A `Client` superclass with concrete subclasses such as `Individual` (`PessoaFisica`) and account types like `CurrentAccount` (`ContaCorrente`) and `SavingsAccount` (`ContaPoupanca`).
- **Abstract Base Classes:** Use of the `abc` module to define contracts for interfaces and abstract behaviors (e.g., `AbstractAccount`, `AbstractTransaction`).
- **Polymorphism:** Methods like `withdraw` are implemented differently depending on the account type.
- **Encapsulation:** Attributes are managed with proper access control.
- **Composition:** A `Client` can have one or more accounts; `Account` maintains a list of `Transaction` objects.
- **Business Logic Enforcement:** Includes rules like daily withdrawal limits, minimum balance checks, and proper validation of CPF and account existence.

---

### Key Features

- Creating individual clients (CPF-based).
- Managing accounts: current and savings.
- Performing deposits and withdrawals.
- Transaction history per account.
- Polymorphic behavior for withdrawal rules per account type.
- Command-line interaction and print outputs.
- CPF validation.
- Account and transaction classes with detailed behavior.
- Demonstrates deep understanding of class inheritance, method overriding, and type checking.

---

## Technologies Used
- **Python 3.11.2**: Core language.
- **abc**: Abstract Base Classes for enforcing OOP design.
- **Built-in terminal print/logic**: For testing and visualization during development.
- **POO principles**: Applied extensively throughout the project.

---

## Usage
This project is terminal-based and meant to simulate the flow of banking operations through Python classes. To explore the system:

- Create client objects and assign accounts.
- Perform deposit and withdrawal operations using polymorphic methods.
- Observe the output history of transactions per account.
- Customize and extend logic for more features like transfers or fees.
- The current structure supports modular extension.

---

## Images
This section provides visual examples of the program in action. Is reserved for system diagrams and execution screenshots.

### UML Diagram
![Diagram-UML](https://github.com/ecopque/new_banking_system/blob/main/prints/Code_-_Python_-_New_Nanking_System.png)

---

## Developer Guide
If you have any questions about the code, I have documented the most important lines with explanations on their functionality in the **log.txt** file. This file provides a **step-by-step** guide to help understand the code and how the system works.
