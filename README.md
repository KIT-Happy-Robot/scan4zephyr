# scan4zephyr

## Introduction

scan.pyってあるけど、正しくは3DF Zephyrでフォトグラメトリを行うための写真を撮影するプログラムである。

## Setup

```bash
python3 -m venv rs_env
pip install -r requirements.txt (仕事してないかも)
```

pipでインストールが必要な奴

```bash
pip install numpy
pip install opencv-python
pip install pyrealsense2
```

## How to use

### Linux

```bash
source rs_venv/bin/activate
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```
# 未完成
### Windows

```bash
.\rs_env\Scripts\activate
python 3dscan.py {folder_name}
# 使い終わったら
deactivate
```
