# Password Detection Neural Network

This repository contains a simple neural network implemented in Python for detecting password-like strings. The goal of this project is to identify whether a given string is similar to a password based on certain characteristics and patterns commonly found in passwords.

## Results

Model file: `models/rnn_model.h5`

#### Model Performances

```
Precision: 0.9682656053623796
Recall: 0.9356340451371319
```

#### Example
Passwords were selected from: https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt

| OriginalWord             | IsPassword | Prediction |
|--------------------------|------------|------------|
| Hello                    | False      | False      |
| at least 8 character long| False      | False      |
| SELECT * FROM table_name;| False      | False      |
| </html>                  | False      | False      |
| col_name                 | False      | False      |
| field=                   | False      | False      |
| 147258                   | True       | False      |
| 123456789a               | True       | True       |
| blink182                 | True       | True       |
| michael1                 | True       | True       |
| 1qaz2wsx                 | True       | True       |
| sunshine                 | True       | False      |

## Usage

```python
from detect_password import *

detector = PasswordDetector(model_path='models/rnn_model.h5')

strings = ['Hello', 'at least 8 character long', '123456789a', 'blink182']

predictions = detector.detect_passwords(strings)
for string, pred in zip(strings, predictions):
    print(f"{string}, Is Password: {pred}")
```

#### Output

```
Hello, Is Password: False
at least 8 character long, Is Password: False
123456789a, Is Password: True
blink182, Is Password: True
```

For more examples, refer to `example.ipynb`.

## Training

To get details about model training, refer to the `train_model.ipynb`.
The training data used for traning is extracted from the following projects, You need to download the project source code and use the `get_words_from_files(dir_name)` function to extract strings for training:

- Wordpress: https://github.com/WordPress/WordPress
- CCXT: https://github.com/ccxt/ccxt

The passwords used during training can be found at: https://github.com/danielmiessler/SecLists/tree/master/Passwords
