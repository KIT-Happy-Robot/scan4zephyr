# scan4zephyr

## Introduction

scan.pyってあるけど、正しくは3DF Zephyrでフォトグラメトリを行うための写真を撮影するプログラムである。

## Setup

```bash
python3 -m venv sfz_venv
# pipのアップデート
pip install -U pip
```

## How to use

### Linux

```bash
source rs_venv/bin/activate
pip install -r requirements.txt
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```

### Windows

```bash
.\rs_env\Scripts\activate
pip install -r requirements.txt
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```
