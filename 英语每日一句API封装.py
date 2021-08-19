#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/8/24 5:15 下午
# @Author   : Colin.Liu
# @Email    : colin50631@gmail.com
# @File     : demo.py
# @Software : PyCharm


import arrow
import requests


class OneStatementOfEnglish:
    """
    英语每日一句
    目前支持：
        + 有道
        + 扇贝
    """
    _today = arrow.now().format('YYYY-MM-DD')

    def switchToCase(self, case):
        # print("case: ", case)
        func_name = "case_" + str(case)
        # print("func_name: ", func_name)
        method = getattr(self, func_name, self.switchToCase)
        return method

    def case_youdao(self):
        yd_url = "https://dict.youdao.com/infoline?mode=publish&date=" + self._today + "&update=auto&apiversion=5.0"
        #print(yd_url)
        result = {}
        for record in requests.get(yd_url).json()[self._today]:
            if record['type'] == '壹句':
                result['date'] = self._today
                result['content'] = record['title']
                result['translation'] = record['summary']

                break
        return result

    def case_shanbay(self):
        sb_url = "https://apiv3.shanbay.com/weapps/dailyquote/quote/?date=" + self._today
        result = {}
        record = requests.get(sb_url).json()

        result['date'] = self._today
        result['content'] = record['content']
        result['translation'] = record['translation']

        return result


if __name__ == "__main__":
    ones = OneStatementOfEnglish()
    youdao = ones.switchToCase("youdao")()
    print("有道词典: ", youdao)

    shanbay = ones.switchToCase("shanbay")()
    print("扇贝单词：", shanbay)
    while True:
        pass
