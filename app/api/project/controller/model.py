from fastapi import Query
import string

class Project:
    '''
    alias : API 上的參數名稱
    description : 參數說明文字
    enum : 限定參數值
    參數可預設為非必填 e.g. 
    date: Optional[str|float|...] = Query(
                    None,
                    alias='Date',
                    description=""
                )
    '''

    def __init__(
            self,
            first_char: str = Query(
                'A',
                alias='FirstChar',
                description="身分證字號字母",
                enum=list(string.ascii_uppercase)),
            gender: str = Query(
                'female',
                alias='Gender',
                description="性別",
                enum=["female", "male"])):
        
        self.first_char = first_char
        self.gender = gender