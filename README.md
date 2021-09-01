# scan4zephyr

## Introduction

scan.pyってあるけど、正しくは3DF Zephyrでフォトグラメトリを行うための写真を撮影するプログラムである。

## Setup

```bash
python3 -m venv sfz_venv
```

## How to use

### Linux

```bash
source rfz_venv/bin/activate
# pipのアップデート
pip install -U pip
pip install -r requirements.txt
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```

### Windows

```bash
.\rfz_env\Scripts\activate
# pipのアップデート
pip install -U pip
pip install -r requirements.txt
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```
