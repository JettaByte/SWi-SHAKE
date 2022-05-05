#https://kwatch-24h.net/EQLevel.json API 클래스
class kel:

    #현재 레벨 리턴
    def lv(*arg):
        import json, requests, discord

        url = requests.get("https://kwatch-24h.net/EQLevel.json")
        text = url.text

        data = json.loads(text)

        mdata = data['l']

        lresult = str(mdata)

        return lresult

    #현재 Green 리턴
    def g(*arg):
        import json, requests, discord

        url = requests.get("https://kwatch-24h.net/EQLevel.json")
        text = url.text

        data = json.loads(text)

        mdata = data['g']

        lresult = str(mdata)

        return lresult

    #현재 Yellow 리턴
    def y(*arg):
        import json, requests, discord

        url = requests.get("https://kwatch-24h.net/EQLevel.json")
        text = url.text

        data = json.loads(text)

        mdata = data['y']

        lresult = str(mdata)

        return lresult

    #현재 Red 리턴
    def r(*arg):
        import json, requests, discord

        url = requests.get("https://kwatch-24h.net/EQLevel.json")
        text = url.text

        data = json.loads(text)

        mdata = data['r']

        lresult = str(mdata)

        return lresult