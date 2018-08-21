import os
import re
from aip import AipSpeech
import time

APP_ID = '11478815'
API_KEY = '2m4bO8OV8F21saqe96H8Q0MV'
SECRET_KEY = 'IO5faSMp7tPkeIjBwClDFTjiaNP921au'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# txt_path = '重生六零空间纪事.txt'
txt_path = '重生之爸爸不好当.txt'

# with open(txt_path, 'r', encoding='utf8') as f:
#     text = f.read()
#     text = re.sub(r'(.{30})', lambda x: '{}\n'.format(x.group(1)), text)

# with open(txt_path, 'w', encoding='utf8') as f:
#     f.write(text)

with open(txt_path, 'r', encoding='utf8') as f:
    for index, line in enumerate(f):
        index = '2B%06d'%index
        # if index < 8331:
        #     continue
        line = line.strip()

        try:
            res = client.synthesis(line, 'zh', 1, {'per': '4', 'spd': '5', 'vol': '7', 'aue': '6'})
        except Exception:
            time.sleep(5)
            res = client.synthesis(line, 'zh', 1, {'per': '4', 'spd': '5', 'vol': '7', 'aue': '6'})
        if not isinstance(res, dict):
            with open('./wav/{}.wav'.format(index), 'wb') as f:
                f.write(res)
                
            with open('./txt/{}.txt'.format(index), 'w') as f:
                f.write(line)
        else:
            print(index, 'err')

        print(index)            
        # index += 1
