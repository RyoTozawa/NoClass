#!/usr/bin/env python3
# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = os.environ.get("FUN_LOGIN_URL") # 環境変数の値をAPに代入
ID = os.environ.get("FUN_ID") # 環境変数の値をAPに代入
PASSWORD = os.environ.get("FUN_PASSWORD") # 環境変数の値をAPに代入


