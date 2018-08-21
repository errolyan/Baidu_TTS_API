import os
import re
from aip import AipSpeech

APP_ID = '11478815'
API_KEY = '2m4bO8OV8F21saqe96H8Q0MV'
SECRET_KEY = 'IO5faSMp7tPkeIjBwClDFTjiaNP921au'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# txt_path = '重生六零空间纪事.txt'
txt_path = '重生之爸爸不好当.txt'
with open(txt_path, encoding='utf8') as f:
    index = 1
    for line in f:
        line = line.strip()

        if line != '':
            match = re.match(r'第(\d+)章', line)
            if match:
                cha_num = match.group(1)
                index = 1
                continue

            if int(cha_num) < 17:
                continue

            res = client.synthesis(line, 'zh', 1, {'per': '4', 'spd': '5', 'vol': '7', 'aue': '6'})
            if not isinstance(res, dict):
                with open('./wav/{}_{}.wav'.format(cha_num, index), 'wb') as f:
                    f.write(res)
                    
                with open('./txt/{}_{}.txt'.format(cha_num, index), 'w') as f:
                    f.write(line)
            else:
                print(cha_num, index, 'err')

            print(cha_num, index)            
            index += 1
