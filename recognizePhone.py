# -*- coding: utf-8 -*-
from keywords import *


def clean(phones):
    mobile_phones, telephones = [], []
    pattern = "(13[0-9]|14[579]|15[0-3,5-9]|16[5-6]|17[0135678]|18[0-9]|19[89])\d{8}"

    # 先拆分，再尝试合并
    _phones, drop = [], []
    for phone in phones:
        phone = kickFullWidth(phone, None)
        phone = re.sub(u'[^\d]+', u'|', phone)
        for subPhone in phone.split("|"):
            if len(subPhone) >= 3 and subPhone not in _phones:
                _phones.append(subPhone)

    # 因为有区号而被分成两个号的座机号需要重新拼凑，因为前3、4后7、8，不可能存在一个号同时前后满足
    for i in range(len(_phones) - 1):
        if _phones[i] in regionCodes3 + regionCodes4 and len(_phones[i + 1]) in [7, 8]:
            telephones.append(_phones[i] + _phones[i + 1])  # 满足的座机直接写入座机list
            drop.extend([_phones[i], _phones[i + 1]])

    _phones = [x for x in _phones if x not in drop]
    for phone in set(_phones):
        allSame = True
        for i in range(len(phone) - 1):
            if phone[i] != phone[i + 1]:
                allSame = False
                break
        if allSame:
            continue
        if len(phone) == 11 and re.search(pattern, phone) is not None:
            mobile_phones.append(phone)
        elif len(phone) > 11:
            for i in range(len(phone) - 11):
                tmp = phone[i:i + 11]
                if re.search(pattern, tmp) is not None:
                    mobile_phones.append(tmp)
        elif len(phone) in [7, 8]:
            telephones.append(phone)
        elif len(phone) in [10, 11, 12] and (phone[0:3] in regionCodes3 or phone[0:4] in regionCodes4):
            telephones.append(phone)

    return mobile_phones, telephones