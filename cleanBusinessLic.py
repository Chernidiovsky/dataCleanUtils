# -*- coding: utf-8 -*-
from keywords import *


def getLicenseInfo(lic):
    licTypeDic = {"1": u"机构编制", "2": u"外交", "3": u"司法行政", "4": u"文化", "5": u"民政", "6": u"旅游", "7": u"宗教", "8": u"工会",
                  "9": u"工商", "A": u"中央军委改革和编制办公室", "N": u"农业", "Y": u"其他"}
    licTypDetailDic = {"11": u"机关", "12": u"事业单位", "13": u"编办直接管理机构编制的群众团体", "19": u"其他", "21": u"外国常驻新闻机构",
                       "29": u"其他", "31": u"律师执业机构", "32": u"公证处", "33": u"基层法律服务所", "34": u"司法鉴定机构", "35": u"仲裁委员会",
                       "39": u"其他", "41": u"外国在华文化中心", "49": u"其他", "51": u"社会团体", "52": u"民办非企业单位", "53": u"基金会",
                       "59": u"其他", "61": u"外国旅游部门常驻代表机构", "62": u"港澳台地区旅游部门常驻内地（大陆）代表机构", "69": u"其他", "71": u"宗教活动场所",
                       "72": u"宗教院校", "79": u"其他", "81": u"基层工会", "89": u"其他", "91": u"企业", "92": u"个体工商户",
                       "93": u"农民专业合作社", "A1": u"军队事业单位", "A9": u"其他", "N1": u"组级集体经济组织", "N2": u"村级集体经济组织",
                       "N3": u"乡镇级集体经济组织", "N9": u"其他", "Y1": u"其他"}

    def checkAllSame(license):
        allSame = True
        for i in range(len(license) - 1):
            if license[i] != license[i + 1]:
                allSame = False
                break
        if allSame:
            return ""
        else:
            return license

    def verifyLic15(license):
        """
        https://wenku.baidu.com/view/19873704cc1755270722087c.html
        """
        p = 10
        for a in license[:-1]:
            s = p % 11 + int(a)
            remainder10 = s % 10 if s % 10 != 0 else 10
            p = remainder10 * 2
        s = p % 11 + int(license[-1])
        if s % 10 == 1:
            return "1"
        else:
            return "0"

    def verifyLic18(license):
        """
        https://zh.wikisource.org/zh-hans/GB_32100-2015_%E6%B3%95%E4%BA%BA%E5%92%8C%E5%85%B6%E4%BB%96%E7%BB%84%E7%BB%87%E7%BB%9F%E4%B8%80%E7%A4%BE%E4%BC%9A%E4%BF%A1%E7%94%A8%E4%BB%A3%E7%A0%81%E7%BC%96%E7%A0%81%E8%A7%84%E5%88%99
        """
        characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J",
                      "K", "L", "M", "N", "P", "Q", "R", "T", "U", "W", "X", "Y"]
        top17Coef = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
        word2Num = {j: i for i, j in enumerate(characters)}
        num2Word = {i: j for i, j in enumerate(characters)}
        temp = 0
        try:
            for i in range(17):
                temp = temp + word2Num[license[i]] * top17Coef[i]
            if num2Word[31 - (temp % 31)] == license[17]:
                return "1"
            else:
                return "0"
        except:
            return "0"

    lic = re.sub(u"[\u4e00-\u9fa5]+", " ", lic)
    lic1 = kickFullWidth(lic.upper())  # 全角转半角、特殊字符转空格
    licList = re.split(u"[^0-9A-Z]+", lic1)
    licList = sorted(licList, key=lambda x: len(x), reverse=True)
    lic = licList[0]
    lic = checkAllSame(lic)
    if re.search("[IOZSV]+", lic) is not None:
        lic = ""

    if re.match(re.compile(u"^\d{15}$"), lic):
        clnLic = lic
        licType = u"15位"
    elif re.match(re.compile(u"^[A-Z0-9]{2}\d{6}[A-Z0-9]{10}$"), lic):
        clnLic = lic
        licType = u"18位"
    elif re.search(re.compile(u"^\d{16}[\-\/\\\\]{1}.*$"), lic):
        clnLic = lic[:-1]
        licType = u"15位+1冗余"
    elif re.match(re.compile(u"^\d{17}$"), lic):
        clnLic = lic[:-2]
        licType = u"15位+2冗余"
    elif re.search(re.compile(u"^[A-Z0-9]{2}\d{6}[A-Z0-9]{10}\d{1}[\-\/\\\\]{1}.*$"), lic):
        clnLic = lic[:-1]
        licType = u"18位+1冗余"
    elif re.match(re.compile(u"^[A-Z0-9]{2}\d{6}[A-Z0-9]{10}\d{2}$"), lic):
        clnLic = lic[:-2]
        licType = u"18位+2冗余"
    else:
        clnLic = ""
        licType = u"未知"

    if licType.startswith(u"15位"):
        is_valid = verifyLic15(clnLic)
        if int(clnLic[6]) <= 3:
            business_type = u"内资企业"
        elif int(clnLic[6]) <= 5:
            business_type = u"外资企业"
        else:
            business_type = u"个体工商户"
        districtCode = clnLic[:6]
    elif licType.startswith(u"18位"):
        is_valid = verifyLic18(clnLic)
        try:
            check1 = licTypeDic[clnLic[0]]
        except:
            check1 = ""
        try:
            check2 = "(" + licTypDetailDic[clnLic[0:2]] + ")"
        except:
            check2 = ""
        business_type = check1 + check2
        districtCode = clnLic[2:8]
    else:
        is_valid, business_type, districtCode = "0", "", ""
    return licType, clnLic, is_valid, business_type, districtCode