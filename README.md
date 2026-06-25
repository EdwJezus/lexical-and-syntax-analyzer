# Lexical and Syntax Analyzer (PLY - Python Lex-Yacc)

This project implements a **lexical and syntactic analyzer** for a custom educational programming language using **Python PLY (Lex-Yacc)**.

The system is capable of tokenizing source code, validating syntax rules, and reporting lexical and syntactic errors based on a defined grammar.

---

## 📁 Project Structure

```text
.
├── lexer.py             # Lexical analyzer (tokenization rules)
├── parser.py            # Syntax analyzer (grammar rules)
├── exemplo.txt          # Example source code in the custom language
├── regras.txt           # Language specification notes
└── README.md            # Project documentation
```

---

## ⚙️ Features

- Lexical analysis using regular expressions (PLY Lexer)
- Custom token definitions for a simplified programming language
- Reserved keywords and operators handling
- Syntax analysis using grammar rules (PLY Yacc)
- Error detection for:
  - Invalid tokens (lexical errors)
  - Invalid syntax (parser errors)
- Support for:
  - Variable declarations
  - Assignments
  - Conditional statements (`se`, `senao`)
  - Loops (`enquanto`, `para`)
  - Function declarations and calls
  - Arithmetic and logical expressions

---

## 🧠 Language Overview

The language is an **educational pseudolanguage** defined for learning compiler construction concepts.

### Example syntax:

```bash
numero x.
x = 10.
se x maior 5. entao.
inicio.
elgio = x.
fim.
```

### Supported constructs:
- Declarations: `numero`, `inteiro`
- Control flow: `se`, `enquanto`, `para`
- Functions: custom function declarations and calls
- Operators: `+ - x / % EXP`
- Comparisons: `igual`, `maior`, `menor`, etc.

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install ply
```

### 2. Run lexical analysis
```bash
python lexer.py exemplo.txt
```

### 3. Run syntax analysis
```bash
python parser.py exemplo.txt
```

---

## 📊 Output Example
Lexical analysis:
```bash
Tipo: IDENTIFICADOR   Valor: x        Linha: 1
Tipo: ATRIBUICAO      Valor: =        Linha: 2
```

Syntax analysis:
```bash
Declaração válida
Atribuição válida
Programa sintaticamente válido!
```

---

## ⚠️ Error Handling

The system reports:

- ❌ Invalid characters (lexer errors)
- ❌ Invalid identifiers
- ❌ Syntax errors with line and token information

Example:
```bash
[ERRO SINTATICO] Linha 3 Token ENTAO Valor 'entao'
```

---

## 🎯 Educational Purpose

This project was developed for studying:

- Compiler construction fundamentals
- Lexical analysis (tokenization)
- Syntax analysis (grammar parsing)
- Formal language definition
- Use of PLY (Python Lex-Yacc)

---

## 🧪 Technologies Used
- Python
- PLY (Lex-Yacc)
- Regular Expressions

---

## 📜 License

MIT License © Eduardo Jesus
