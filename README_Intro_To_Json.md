# JSON (JavaScript Object Notation): Research Notes
---

## Table of Contents

1. [Overview](#1-overview)
2. [Definition and Etymology](#2-definition-and-etymology)
3. [Purpose and Use Cases](#3-purpose-and-use-cases)
4. [Implementation and Language Independence](#4-implementation-and-language-independence)
5. [Advantages](#5-advantages)
6. [Supported Data Types](#6-supported-data-types)
7. [JSON Syntax](#7-json-syntax)
8. [Working with JSON in Python](#8-working-with-json-in-python)
9. [Best Practices](#9-best-practices)
10. [References](#10-references)

---

## 1. Overview

This document summarises the JSON data format, covering its definition, purpose, structure, supported data types and syntax rules. Definitions are aligned with the Python standard library documentation for the `json` module.
---

## 2. Definition and Etymology

**JSON** stands for **JavaScript Object Notation**.

The Python documentation describes JSON as a lightweight data interchange format inspired by JavaScript object literal syntax, formally specified in RFC 7159 (since superseded by RFC 8259) and ECMA-404. The documentation also clarifies that JSON is **not a strict subset of JavaScript**, which highlights that it is a distinct data format rather than a part of the JavaScript language (Python Software Foundation, 2026).

---

## 3. Purpose and Use Cases

JSON is used to **store and exchange structured data** in a text-based form that both humans and machines can process. Typical applications include:

| Use case | Example |
|---|---|
| Client-server communication | Responses from REST APIs to web and mobile applications |
| Configuration | `package.json` (Node.js), editor and tool settings |
| Data storage | Document databases (e.g. MongoDB) and JSON columns in relational databases |
| Data serialisation | Saving application state or settings to disk |

---

## 4. Implementation and Language Independence

JSON is **not a programming language**. It is a **plain-text data format**, conventionally encoded in UTF-8 and saved with the `.json` extension.

Although its syntax derives from JavaScript object literals, JSON is **language-independent**. Most modern languages provide a library for converting between native data structures and JSON text. In Python, this is the built-in `json` module; in JavaScript, the `JSON.parse()` and `JSON.stringify()` methods.

---

## 5. Advantages

- **Human-readable:** the structure is easy to read, write and debug.
- **Lightweight:** it is less verbose than alternatives such as XML, reducing payload size and transfer time.
- **Language-independent:** supported across virtually all platforms and programming languages.
- **Easy to parse and generate:** mature libraries exist in most languages, including Python's standard library.
- **Supports nested structures:** objects and arrays can be combined to model complex, hierarchical data.
- **Widely adopted:** it is the dominant format for web APIs and is supported by most databases and tools.

---

## 6. Supported Data Types

JSON defines six data types: four primitive types and two structured types.

| JSON type | Category | Example |
|---|---|---|
| String | Primitive | `"Hello"` |
| Number | Primitive | `42`, `3.14`, `-7`, `1.5e3` |
| Boolean | Primitive | `true`, `false` |
| Null | Primitive | `null` |
| Object | Structured | `{"a": 1}` |
| Array | Structured | `[1, 2, 3]` |

**Limitations.** JSON has no native type for dates, `undefined`, functions or comments. Dates are conventionally stored as strings, ideally in ISO 8601 format (e.g. `"2026-10-14"`).

### 6.1 Mapping between JSON and Python types

The Python `json` module converts between JSON and Python types as follows (Python Software Foundation, 2026):

| JSON | Python |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number (integer) | `int` |
| number (real) | `float` |
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

When Python **encodes** data, `tuple` values are also converted to JSON arrays. When decoded, they return as `list`.

---

## 7. JSON Syntax

### 7.1 Name/value pairs

The fundamental unit of JSON is the **name/value pair**. The name (key) must be a **string enclosed in double quotes**, followed by a colon (`:`), then the value.

```json
"name": "Alice"
```

### 7.2 Objects

An **object** is an unordered collection of name/value pairs enclosed in **curly braces** `{ }`.

```json
{
  "name": "Alice",
  "age": 25,
  "isStudent": true
}
```

### 7.3 Separating data

Name/value pairs within an object are separated by **commas**. A comma must **not** follow the final pair, as trailing commas are invalid in JSON.

```json
{
  "firstName": "Alice",
  "lastName": "Smith",
  "age": 25
}
```

### 7.4 Arrays

An **array** is an ordered list of values enclosed in **square brackets** `[ ]`, with values separated by commas. Array elements may be of any JSON type, including objects and other arrays.

```json
{
  "name": "Alice",
  "hobbies": ["reading", "coding", "cycling"],
  "courses": [
    { "title": "Databases", "grade": 85 },
    { "title": "Web Development", "grade": 90 }
  ]
}
```

### 7.5 Syntax summary

| Element | Syntax rule |
|---|---|
| Object | Curly braces `{ }` |
| Array | Square brackets `[ ]` |
| Key | String in **double quotes** |
| Key/value delimiter | Colon `:` |
| Item separator | Comma `,` (none after the last item) |
| Strings | Double quotes only (single quotes are invalid) |
| Comments | Not permitted |

---

## 8. Working with JSON in Python

The `json` module provides four principal functions:

| Function | Purpose |
|---|---|
| `json.dumps(obj)` | Serialise a Python object to a JSON **string** |
| `json.dump(obj, fp)` | Serialise a Python object and write it to a **file** |
| `json.loads(s)` | Deserialise a JSON **string** into a Python object |
| `json.load(fp)` | Deserialise JSON from a **file** into a Python object |

```python
import json

# Python dict -> JSON string
student = {
    "name": "Alice",
    "age": 25,
    "isStudent": True,
    "courses": ["Databases", "Web Development"],
    "address": None,
}
json_text = json.dumps(student, indent=2)
print(json_text)

# JSON string -> Python dict
data = json.loads(json_text)
print(data["name"])        # Alice
print(type(data))          # <class 'dict'>

# Writing to and reading from a file
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, indent=2)

with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

**Note on non-standard values.** By default, Python's encoder will accept `NaN` and `Infinity` and write them out, but these are **not valid JSON**. The `allow_nan=False` parameter can be used to enforce strict compliance (Python Software Foundation, 2026).

---

## 9. Best Practices

1. Use **double quotes** for all keys and string values.
2. Apply a **consistent naming convention** for keys (e.g. `camelCase` or `snake_case`).
3. **Indent** output for readability during development (e.g. `indent=2`).
4. Avoid trailing commas and comments, as both are invalid.
5. Store dates in **ISO 8601** string format.
6. **Validate** JSON with a linter or validator (e.g. JSONLint) and use `try/except` around `json.loads()` to handle `json.JSONDecodeError`.
7. Use UTF-8 encoding when reading and writing files.

---

## 10. References

Bray, T. (Ed.) (2017) *RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format*. Internet Engineering Task Force. Available at: https://www.rfc-editor.org/rfc/rfc8259

Ecma International (2017) *ECMA-404: The JSON Data Interchange Syntax*. 2nd edn. Available at: https://ecma-international.org/publications-and-standards/standards/ecma-404/

Python Software Foundation (2026) *json: JSON encoder and decoder*. Python 3 Documentation. Available at: https://docs.python.org/3/library/json.html
