# -*- coding: utf-8 -*-
from keywords import *


def clean(names):
    """
    输入一串人名、店名的的list
    输出店名list和人名list
    """
    # 去重、去短、去店铺关键字
    nameList = []
    for name in names:
        if name not in nameList and name not in shopKeywords and name != "" and len(name) > 1:
            nameList.append(name)
    nameList = [kickFullWidth(name, None) for name in nameList]
    shopNames, artificialNames = [], []
    if nameList is None or len(nameList) == 0:
        return shopNames, artificialNames

    likelyShops = [shop for shop in nameList if len(shop) >= 4]
    for shop in likelyShops:  # 包含店铺关键字或以店铺尾字结束的name从nameList剔除
        for kw in shopKeywords:
            if shop.find(kw) >= 0 or shop[-1] in shopEndWords:
                nameList.remove(shop)
                shopNames.append(shop)
                break
    if shopNames:
        shopNames = sorted(shopNames, key=lambda x: len(x), reverse=True)  # 最长的放前面

    likelyPersons = [re.sub(u'[^\u4e00-\u9fa5]+', u'', person) for person in nameList]
    likelyPersons = [person for person in likelyPersons if len(person) <= 7]
    for person in likelyPersons:
        for fn in familyNames:
            if person.startswith(fn):

                # 1姓 + 1名
                # 1姓 + 1姓 + 1名
                # 复姓+名
                if (len(fn) == 1 and len(person) == 2)\
                or (len(fn) == 1 and len(person) == 4 and person[1] in familyNames)\
                or (1 < len(fn) < len(person)):
                    artificialNames.append(person)

                # 1姓 + 2名
                # 2名不含店铺关键字
                elif len(fn) == 1 and len(person) == 3:
                    skip = False
                    for kw in shopKeywords:
                        if person.find(kw) >= 0:
                            skip = True
                            break
                    if not skip:
                        artificialNames.append(person)  # 保持原有顺序
    return shopNames, artificialNames