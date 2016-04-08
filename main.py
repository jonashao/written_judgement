# coding: utf-8
from jio import JIO
import log

try:
    jio = JIO('data/1万篇训练数据集.csv', 'result.csv')
    jio.write_result()
finally:
    log.commit()