# -*- coding: utf-8 -*-
from keywords import *


provRevDic = {"11": u"北京市", "12": u"天津市", "13": u"河北省", "14": u"山西省", "15": u"内蒙古自治区", "21": u"辽宁省", "22": u"吉林省",
              "23": u"黑龙江省", "31": u"上海市", "32": u"江苏省", "33": u"浙江省", "34": u"安徽省", "35": u"福建省", "36": u"江西省",
              "37": u"山东省", "41": u"河南省", "42": u"湖北省", "43": u"湖南省", "44": u"广东省", "45": u"广西壮族自治区", "46": u"海南省",
              "50": u"重庆市", "51": u"四川省", "52": u"贵州省", "53": u"云南省", "54": u"西藏自治区", "61": u"陕西省", "62": u"甘肃省",
              "63": u"青海省", "64": u"宁夏回族自治区", "65": u"新疆维吾尔自治区"}


def clean(idcard):
    idcard = kickFullWidth(idcard, "")
    idcard = re.sub(u'x', u'X', idcard)
    idcard = re.sub(u'[^\d|X+]', u'', idcard)

    if len(idcard) != 18\
    or idcard[0:2] not in [x for x in provRevDic.keys()]\
    or idcard[6:10] < "1919" or idcard[6:10] > "2019":
        return ""

    # 校验码算法 https://zhuanlan.zhihu.com/p/21286417
    checkDic = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    top17Coef = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    temp = 0
    try:
        for i in range(17):
            temp = temp + int(idcard[i]) * top17Coef[i]
        if checkDic[temp % 11] != idcard[17]:
            return ""
    except:
        return ""
    return idcard