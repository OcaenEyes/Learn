import sys
import io
# 输出中文
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print('你好，乔克叔叔')

