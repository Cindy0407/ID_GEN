import random
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

class NumberGen():
    def __init__(self):
        self.char_map = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20,
        'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25,
        'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
        'Y': 31, 'Z': 33
        }
        self.gender_map = {'male':1,'female':2}

    def get_id(self, args, redis_client):
        number_result = ''
        first_char = args.get('first_char', '').upper()
        gender = args.get('gender', '').lower()

        if first_char and gender:
            para_key = f"{first_char}-{gender}"
            cached = redis_client.get(para_key)
            if cached:
                number_result = cached
            else:
                first_char_number = self.char_map.get(first_char)
                gender_number = self.gender_map.get(gender)
                d1, d2 = divmod(first_char_number, 10) # 得到商數和餘數(10位數和個位數)
                first_char_number_cal = d1*1 + d2*9 # 英文字母轉換
                total = first_char_number_cal + gender_number*8 # 先計算前2位的和
                number_result = f'{first_char}{str(gender_number)}'

                for i in range(1,8):
                    num = random.randint(0,9) # 隨機產生0-9的數字
                    total += num*(8-i)
                    number_result += str(num)

                last_nmuber = (10 - total % 10) % 10 # 由10-餘數取最後一碼
                number_result += str(last_nmuber)
                redis_client.set(para_key, number_result, ex=60)

        if number_result:
            r_desc = 'Success!'
            r_code = '0000'
        else:
            r_desc = '查無資料'
            r_code = '0001'

        result = {
            "Data": number_result,
            "rDesc": r_desc,
            "rCode": r_code
        }

        return JSONResponse(jsonable_encoder(result))
