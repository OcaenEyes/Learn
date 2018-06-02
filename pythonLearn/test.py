import sys
import io

# 设置输出模式为UTF-8
sys.stdout =  io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')

a = int(raw_input("qingshuru"))