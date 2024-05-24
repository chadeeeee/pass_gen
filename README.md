# PassGenerate

PassGenerate is a simple Python library for generating random passwords. It allows you to create secure passwords of a specified length with a mix of characters.

## Installation

To install PassGenerate, you can use pip:

```bash
pip install passgenerate
```

## Usage

Here is an example of how to use the PassGenerate library to generate a password of a specified length:

```python
from PasswordGenerator import generate

password = generate(10) # 10 is the number of characters in the password
print("Your password is", password)
```

## Requirements
Python 3.x