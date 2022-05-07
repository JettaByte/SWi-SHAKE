"""
NIDE API CLASS

출처 : https://kwatch-24h.net/EQLevel.json

원작자 : 뷰잉풍

수정자 : KimTaeMin99
"""

# 해당 모듈에 필요한 라이브러리 추가
import requests


class NIDE:

    # 초기화 함수
    def __init__(self):
        self.url = "https://kwatch-24h.net/EQLevel.json"
        self.response = None
        self.json = None
        self.eewinfo = None

    # 실시간 데이터를 가지고 옵니다.
    async def __getCurrentData(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        if self.json["e"] == 1:
            self.eewinfo = self.json["eewinfo"]

    # 실시간 정보 조회
    async def current(self, *args):
        data = None

        await self.__getCurrentData()
        if args[0] == "leval":
            data = self.json["l"]
        elif args[0] == "green":
            data = self.json["g"]
        elif args[0] == "yellow":
            data = self.json["y"]
        elif args[0] == "red":
            data = self.json["r"]
        elif args[0] == "time":
            data = self.json["t"]
        elif args[0] == "status":
            data = self.json["e"]
        elif args[0] == "eew":
            if self.json["e"] == 1:
                data = self.json["eewinfo"]
        elif args[0] == "all":
            if self.json["e"] == 1:
                data = {
                    "leval": self.json["l"],
                    "green": self.json["g"],
                    "yellow": self.json["y"],
                    "red": self.json["r"],
                    "time": self.json["t"],
                    "status": self.json["e"],
                    "eew": self.json["eewinfo"]
                }
            else:
                data = {
                    "leval": self.json["l"],
                    "green": self.json["g"],
                    "yellow": self.json["y"],
                    "red": self.json["r"],
                    "time": self.json["t"],
                    "status": self.json["e"]
                }
        else:
            data = None

        if args[1] == "Y":
            print(data)

        return data
