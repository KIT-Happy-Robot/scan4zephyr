# scan4zephyr

## Introduction

3dscan.pyってあるけど、正しくは3DF Zephyrでフォトグラメトリを行うための写真を撮影するプログラムである。

## Setup

```bash
python3 -m venv rs_env
pip install -r requirements.txt
```

## How to use

### Linux

```bash
source rs_venv/bin/activate
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```

### Windows

```bash
.\rs_env\Scripts\activate
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```
