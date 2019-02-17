import os
from bilibili.testv import fetchLatestTestVideos
import sys

RUN_TASKS = os.environ["RUN_TASKS"]

tasks = RUN_TASKS.split(',')

if 'testv' in tasks:
  fetchLatestTestVideos()

if 'sspai' in tasks:
  print('TODO')
