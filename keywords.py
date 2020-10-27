# -*- coding: utf-8 -*-
import re

# 主要姓氏1910个，复姓在前优先识别
familyNames = [u"伊尔根觉罗", u"依尔根觉罗", u"依尔觉悟罗", u"爱新觉罗", u"愛新覺羅", u"布雅穆齊", u"成吉思汗", u"额尔德特", u"赫舍里氏", u"讷殷富察", u"萨穆希爾",
               u"乌拉纳喇", u"叶赫那拉", u"叶赫那兰", u"依尔觉罗", u"阿伏干", u"阿勒根", u"阿鹿桓", u"阿史德", u"阿史那", u"阿思沒", u"阿勿嘀", u"阿逸多",
               u"拔列蘭", u"白楊提", u"孛術魯", u"布叔滿", u"步大汗", u"步六孤", u"步鹿根", u"古口引", u"瓜尔佳", u"哈什纳", u"赫舍里", u"库雅喇", u"沒路真",
               u"莫那婁", u"钮祜禄", u"破落那", u"普六茹", u"泣伏利", u"如皋冒", u"萨克达", u"萨嘛喇", u"舒穆禄", u"术要甲", u"索绰罗", u"索绰络", u"他塔喇",
               u"乌古伦", u"喜塔腊", u"仪林淦", u"萦绰络", u"阿單", u"阿跌", u"阿賀", u"阿會", u"阿里", u"阿侖", u"阿羅", u"阿熱", u"哀牢", u"哀駘",
               u"艾歲", u"安遲", u"安都", u"安端", u"安國", u"安金", u"安陵", u"安平", u"安期", u"安丘", u"安是", u"安陽", u"傲 ", u"奧敦", u"奧魯",
               u"奧屯", u"巴公", u"拔拔", u"拔列", u"拔略", u"拔也", u"把利", u"罷敵", u"白狄", u"白公", u"白侯", u"白鹿", u"白鸞", u"白馬", u"白冥",
               u"白男", u"白象", u"白亞", u"白乙", u"百里", u"柏常", u"柏高", u"柏侯", u"班丘", u"阪泉", u"阪上", u"苞丘", u"薄姑", u"薄奚", u"薄野",
               u"鮑丘", u"鮑俎", u"卑梁", u"卑徐", u"北方", u"北宫", u"北宮", u"北郭", u"北海", u"北旄", u"北門", u"北丘", u"北人", u"北唐", u"北鄉",
               u"北野", u"北殷", u"倍俟", u"比丘", u"比人", u"苾悉", u"閉珊", u"碧鲁", u"賓牟", u"並官", u"波斯", u"波瓦", u"撥略", u"伯比", u"伯常",
               u"伯成", u"伯德", u"伯封", u"伯豐", u"伯高", u"伯昏", u"伯暋", u"伯夏", u"伯有", u"伯州", u"伯宗", u"駁馬", u"卜成", u"卜梁", u"卜馬",
               u"步都", u"步叔", u"步溫", u"步揚", u"崇侯", u"褚师", u"淳于", u"错木", u"大友", u"单于", u"澹台", u"澹臺", u"登徒", u"第八", u"第二",
               u"第六", u"第七", u"第三", u"第四", u"第五", u"第一", u"东方", u"东郭", u"东门", u"东欧", u"東方", u"東郭", u"東門", u"獨孤", u"端木",
               u"段干", u"范姜", u"方何", u"费莫", u"蚡冒", u"棼冒", u"傅其", u"傅余", u"富察", u"高陽", u"哥舒", u"公都", u"公良", u"公叔", u"公孙",
               u"公孫", u"公西", u"公绪", u"公羊", u"公冶", u"公仪", u"公义", u"公治", u"谷梁", u"穀梁", u"歸海", u"赫连", u"呼延", u"忽侖", u"皇甫",
               u"火拔", u"季孫", u"夹谷", u"晋楚", u"京兆", u"經孫", u"精纵", u"九吾", u"沮渠", u"空曾", u"空桑", u"空同", u"空桐", u"空相", u"崆峒",
               u"郎佳", u"乐正", u"荔菲", u"梁丘", u"列御", u"令狐", u"甪里", u"陆费", u"闾丘", u"閭丘", u"马佳", u"蒙山", u"孟孫", u"墨胎", u"母将",
               u"慕容", u"那拉", u"纳喇", u"納喇", u"納蘭", u"南方", u"南宫", u"南郭", u"南门", u"南門", u"南野", u"聂晁", u"欧阳", u"歐陽", u"辟閭",
               u"濮阳", u"漆雕", u"亓官", u"乞伏", u"曲沃", u"壤驷", u"萨蛮", u"三闾", u"三小", u"上官", u"申屠", u"神農", u"生驹", u"侍其", u"叔敖",
               u"叔风", u"叔梁", u"叔夙", u"叔孫", u"叔夜", u"术甲", u"司城", u"司功", u"司空", u"司寇", u"司马", u"司徒", u"素黎", u"太史", u"太叔",
               u"天其", u"田山", u"佟佳", u"禿髮", u"图门", u"凃肖", u"脫脫", u"拓拔", u"拓跋", u"完颜", u"万俟", u"王叔", u"王子", u"微生", u"尉迟",
               u"闻人", u"聞人", u"乌孙", u"乌雅", u"巫马", u"無終", u"五兆", u"西方", u"西郭", u"西门", u"西門", u"夏侯", u"鲜于", u"相查", u"轩辕",
               u"軒轅", u"羊舌", u"楊雷", u"耶律", u"有莘", u"右师", u"宇文", u"宰父", u"辗迟", u"张简", u"张廖", u"章佳", u"張簡", u"張廖", u"长孙",
               u"折娄", u"中叔", u"钟离", u"锺离", u"仲孙", u"仲长", u"诸葛", u"颛孙", u"顓孫", u"子车", u"子革", u"子南", u"子濯", u"宗政", u"左丘",
               u"阿", u"哀", u"藹", u"靄", u"艾", u"爱", u"愛", u"曖", u"安", u"俺", u"犴", u"岸", u"按", u"昂", u"盎", u"敖", u"熬",
               u"傲", u"奥", u"奧", u"八", u"仈", u"巴", u"芭", u"拔", u"跋", u"把", u"罷", u"霸", u"白", u"百", u"柏", u"摆", u"擺",
               u"拜", u"班", u"般", u"阪", u"板", u"半", u"辦", u"邦", u"榜", u"棒", u"傍", u"包", u"苞", u"褒", u"雹", u"薄", u"宝",
               u"保", u"葆", u"堡", u"飽", u"寶", u"抱", u"豹", u"報", u"鲍", u"暴", u"鮑", u"杯", u"卑", u"悲", u"碑", u"北", u"贝",
               u"孛", u"邶", u"貝", u"背", u"倍", u"被", u"備", u"奔", u"贲", u"賁", u"本", u"伻", u"崩", u"甭", u"泵", u"蹦", u"逼",
               u"鼻", u"比", u"彼", u"筆", u"鄙", u"必", u"毕", u"闭", u"庇", u"邲", u"苾", u"畢", u"閉", u"敝", u"弼", u"碧", u"薜",
               u"壁", u"璧", u"边", u"編", u"邊", u"扁", u"鴘", u"卞", u"弁", u"汴", u"便", u"辨", u"辯", u"變", u"彪", u"標", u"麃",
               u"表", u"鱉", u"別", u"别", u"邠", u"宾", u"彬", u"斌", u"賓", u"濱", u"冰", u"兵", u"丙", u"邴", u"秉", u"炳", u"稟",
               u"並", u"波", u"剝", u"缽", u"伯", u"帛", u"泊", u"勃", u"亳", u"博", u"僰", u"卜", u"补", u"捕", u"補", u"不", u"布",
               u"步", u"部", u"簿", u"才", u"采", u"彩", u"菜", u"蔡", u"仓", u"苍", u"藏", u"操", u"曹", u"草", u"策", u"岑", u"曽",
               u"曾", u"茶", u"查", u"査", u"察", u"柴", u"禅", u"产", u"昌", u"苌", u"常", u"厂", u"场", u"畅", u"倡", u"唱", u"抄",
               u"钞", u"超", u"晁", u"巢", u"朝", u"潮", u"车", u"臣", u"尘", u"沉", u"陈", u"陳", u"晨", u"谌", u"称", u"成", u"呈",
               u"承", u"城", u"乘", u"程", u"澄", u"池", u"迟", u"茌", u"赤", u"敕", u"冲", u"充", u"崇", u"宠", u"瘳", u"仇", u"丑",
               u"出", u"初", u"除", u"楮", u"储", u"楚", u"褚", u"揣", u"传", u"春", u"淳", u"啜", u"慈", u"次", u"从", u"丛", u"琮",
               u"崔", u"催", u"翠", u"寸", u"蹉", u"错", u"达", u"笪", u"答", u"大", u"逮", u"代", u"岱", u"带", u"贷", u"戴", u"丹",
               u"单", u"郸", u"旦", u"但", u"淡", u"党", u"黨", u"刀", u"道", u"德", u"登", u"邓", u"鄧", u"狄", u"迪", u"邸", u"底",
               u"地", u"第", u"典", u"佃", u"奠", u"電", u"刁", u"迭", u"丁", u"定", u"东", u"冬", u"董", u"懂", u"栋", u"都", u"钭",
               u"豆", u"窦", u"竇", u"督", u"毒", u"独", u"笃", u"堵", u"杜", u"度", u"端", u"段", u"敦", u"顿", u"多", u"铎", u"朵",
               u"俄", u"娥", u"额", u"鄂", u"恩", u"尔", u"佴", u"贰", u"法", u"番", u"藩", u"凡", u"樊", u"繁", u"范", u"方", u"芳",
               u"房", u"飞", u"肥", u"斐", u"费", u"費", u"粉", u"丰", u"风", u"封", u"酆", u"冯", u"逢", u"馮", u"凤", u"奉", u"俸",
               u"佛", u"夫", u"伏", u"扶", u"苻", u"洑", u"浮", u"符", u"福", u"甫", u"府", u"父", u"付", u"附", u"阜", u"复", u"副",
               u"傅", u"富", u"呷", u"尕", u"改", u"盖", u"甘", u"干", u"淦", u"刚", u"皋", u"高", u"髙", u"杲", u"告", u"郜", u"戈",
               u"革", u"格", u"葛", u"庚", u"耿", u"更", u"弓", u"公", u"功", u"宫", u"恭", u"龚", u"龔", u"巩", u"拱", u"共", u"贡",
               u"供", u"勾", u"缑", u"芶", u"苟", u"菇", u"辜", u"古", u"谷", u"骨", u"顾", u"顧", u"刮", u"关", u"观", u"官", u"關",
               u"管", u"贯", u"冠", u"光", u"广", u"归", u"圭", u"妫", u"媯", u"歸", u"鬼", u"贵", u"桂", u"滚", u"呙", u"郭", u"国",
               u"虢", u"果", u"过", u"過", u"哈", u"还", u"海", u"亥", u"憨", u"邗", u"函", u"韩", u"寒", u"韓", u"罕", u"汉", u"汗",
               u"撖", u"行", u"杭", u"蒿", u"好", u"郝", u"昊", u"浩", u"禾", u"合", u"何", u"和", u"河", u"盍", u"荷", u"贺", u"赫",
               u"黑", u"恒", u"衡", u"弘", u"红", u"闳", u"宏", u"洪", u"鸿", u"侯", u"后", u"郈", u"厚", u"後", u"候", u"呼", u"忽",
               u"狐", u"胡", u"斛", u"湖", u"虎", u"許", u"户", u"扈", u"花", u"华", u"滑", u"化", u"怀", u"淮", u"槐", u"环", u"桓",
               u"奂", u"宦", u"浣", u"皇", u"黄", u"黃", u"灰", u"恢", u"辉", u"翚", u"翬", u"回", u"会", u"惠", u"荤", u"浑", u"火",
               u"伙", u"霍", u"机", u"姬", u"基", u"嵇", u"箕", u"稽", u"雞", u"及", u"吉", u"汲", u"姞", u"戢", u"集", u"籍", u"己",
               u"计", u"记", u"纪", u"季", u"济", u"紀", u"继", u"祭", u"蓟", u"暨", u"冀", u"加", u"佳", u"家", u"嘉", u"郏", u"荚",
               u"甲", u"贾", u"駱", u"坚", u"菅", u"检", u"简", u"翦", u"蹇", u"謇", u"见", u"建", u"剑", u"谏", u"江", u"将", u"姜",
               u"蒋", u"蔣", u"降", u"娇", u"焦", u"角", u"佼", u"矫", u"徼", u"缴", u"教", u"接", u"揭", u"节", u"杰", u"捷", u"颉",
               u"竭", u"解", u"介", u"金", u"进", u"晋", u"晉", u"靳", u"京", u"经", u"荆", u"井", u"景", u"敬", u"靖", u"静", u"镜",
               u"九", u"酒", u"咎", u"救", u"居", u"驹", u"琚", u"鞠", u"局", u"菊", u"橘", u"巨", u"句", u"具", u"俱", u"剧", u"卷",
               u"雋", u"绝", u"矍", u"军", u"君", u"俊", u"隽", u"卡", u"开", u"凯", u"勘", u"堪", u"阚", u"康", u"亢", u"抗", u"考",
               u"柯", u"科", u"可", u"克", u"空", u"孔", u"寇", u"苦", u"库", u"蒯", u"郐", u"匡", u"狂", u"邝", u"旷", u"况", u"鄺",
               u"奎", u"夔", u"蒉", u"昆", u"阔", u"拉", u"喇", u"来", u"莱", u"赖", u"賴", u"兰", u"蓝", u"藍", u"蘭", u"烂", u"郎",
               u"郞", u"狼", u"稂", u"朗", u"劳", u"牢", u"勞", u"老", u"乐", u"勒", u"雷", u"蕾", u"类", u"冷", u"梨", u"犁", u"黎",
               u"礼", u"李", u"里", u"理", u"力", u"历", u"厉", u"立", u"丽", u"励", u"利", u"荔", u"郦", u"栗", u"连", u"莲", u"連",
               u"廉", u"敛", u"练", u"練", u"良", u"梁", u"粱", u"疗", u"聊", u"寥", u"廖", u"列", u"林", u"吝", u"蔺", u"泠", u"凌",
               u"陵", u"零", u"另", u"令", u"刘", u"留", u"劉", u"柳", u"六", u"龙", u"泷", u"隆", u"龍", u"陇", u"娄", u"婁", u"楼",
               u"樓", u"漏", u"卢", u"芦", u"庐", u"炉", u"鲁", u"魯", u"陆", u"陸", u"鹿", u"逯", u"禄", u"路", u"栾", u"伦", u"罗",
               u"羅", u"洛", u"骆", u"雒", u"闾", u"吕", u"呂", u"侣", u"旅", u"律", u"绿", u"麻", u"马", u"馬", u"买", u"麦", u"蛮",
               u"满", u"曼", u"蔄", u"漫", u"芒", u"忙", u"莽", u"猫", u"毛", u"茆", u"茅", u"卯", u"茂", u"冒", u"贸", u"媢", u"么",
               u"枚", u"梅", u"美", u"门", u"蒙", u"孟", u"梦", u"弥", u"祢", u"糜", u"米", u"芈", u"弭", u"宓", u"秘", u"密", u"苗",
               u"妙", u"庙", u"繆", u"咩", u"民", u"闵", u"闽", u"敏", u"名", u"明", u"谬", u"缪", u"摩", u"磨", u"莫", u"貊", u"墨",
               u"默", u"牟", u"母", u"木", u"目", u"沐", u"牧", u"幕", u"睦", u"慕", u"穆", u"那", u"纳", u"娜", u"乃", u"奶", u"迺",
               u"奈", u"南", u"难", u"赧", u"铙", u"能", u"尼", u"泥", u"倪", u"年", u"念", u"乜", u"聂", u"聶", u"宁", u"甯", u"牛",
               u"钮", u"农", u"侬", u"奴", u"诺", u"欧", u"殴", u"鸥", u"偶", u"藕", u"杷", u"潘", u"攀", u"盘", u"泮", u"庞", u"逄",
               u"旁", u"胖", u"裴", u"盆", u"朋", u"彭", u"蓬", u"澎", u"邳", u"皮", u"辟", u"骈", u"频", u"品", u"平", u"凭", u"颇",
               u"仆", u"蒲", u"濮", u"朴", u"浦", u"普", u"溥", u"樸", u"瀑", u"柒", u"戚", u"漆", u"亓", u"齐", u"祁", u"岐", u"其",
               u"奇", u"歧", u"祈", u"耆", u"骑", u"琦", u"綦", u"旗", u"蕲", u"麒", u"乞", u"杞", u"启", u"起", u"啟", u"泣", u"千",
               u"牵", u"前", u"钱", u"乾", u"潜", u"羌", u"强", u"墙", u"乔", u"侨", u"桥", u"谯", u"樵", u"巧", u"且", u"郄", u"钦",
               u"秦", u"琴", u"禽", u"勤", u"青", u"卿", u"清", u"庆", u"邛", u"丘", u"邱", u"秋", u"求", u"裘", u"区", u"诎", u"屈",
               u"區", u"麴", u"渠", u"璩", u"瞿", u"蘧", u"曲", u"权", u"全", u"泉", u"却", u"卻", u"雀", u"阙", u"群", u"冉", u"穰",
               u"让", u"讓", u"荛", u"饶", u"饒", u"绕", u"壬", u"仁", u"任", u"仍", u"日", u"戎", u"荣", u"容", u"榮", u"融", u"柔",
               u"如", u"茹", u"汝", u"阮", u"芮", u"锐", u"瑞", u"闰", u"润", u"若", u"洒", u"撒", u"萨", u"薩", u"塞", u"赛", u"伞",
               u"散", u"桑", u"森", u"僧", u"沙", u"厦", u"山", u"苫", u"珊", u"闪", u"陕", u"善", u"商", u"赏", u"上", u"尚", u"韶",
               u"少", u"卲", u"邵", u"绍", u"佘", u"舍", u"厍", u"申", u"莘", u"神", u"沈", u"甚", u"慎", u"升", u"生", u"声", u"绳",
               u"省", u"圣", u"盛", u"聖", u"师", u"诗", u"施", u"石", u"时", u"实", u"拾", u"史", u"矢", u"始", u"士", u"示", u"世",
               u"仕", u"市", u"似", u"势", u"侍", u"是", u"释", u"守", u"首", u"寿", u"受", u"殳", u"书", u"叔", u"舒", u"疏", u"束",
               u"树", u"帅", u"帥", u"双", u"霜", u"水", u"税", u"顺", u"舜", u"说", u"硕", u"司", u"思", u"斯", u"死", u"四", u"佀",
               u"姒", u"俟", u"松", u"宋", u"送", u"苏", u"蘇", u"夙", u"素", u"速", u"粟", u"眭", u"睢", u"隋", u"随", u"岁", u"孙",
               u"孫", u"所", u"索", u"锁", u"塔", u"台", u"邰", u"太", u"泰", u"郯", u"谈", u"覃", u"谭", u"潭", u"檀", u"镡", u"譚",
               u"汤", u"湯", u"唐", u"堂", u"塘", u"桃", u"陶", u"淘", u"腾", u"滕", u"藤", u"提", u"遆", u"天", u"田", u"帖", u"铁",
               u"庭", u"通", u"仝", u"同", u"佟", u"彤", u"桐", u"童", u"凃", u"徒", u"涂", u"屠", u"兔", u"脫", u"脱", u"佗", u"陀",
               u"庹", u"拓", u"瓦", u"完", u"宛", u"晚", u"万", u"萬", u"汪", u"王", u"网", u"枉", u"旺", u"望", u"危", u"威", u"巍",
               u"韦", u"伟", u"尾", u"委", u"隗", u"卫", u"未", u"位", u"尉", u"蔚", u"魏", u"温", u"溫", u"文", u"闻", u"聞", u"问",
               u"翁", u"瓮", u"沃", u"乌", u"邬", u"巫", u"鄔", u"无", u"毋", u"吾", u"吴", u"吳", u"梧", u"五", u"午", u"伍", u"仵",
               u"武", u"兀", u"戊", u"务", u"悟", u"夕", u"西", u"希", u"昔", u"析", u"郗", u"息", u"奚", u"悉", u"溪", u"习", u"席",
               u"袭", u"洗", u"玺", u"喜", u"戏", u"系", u"舄", u"霞", u"夏", u"仙", u"先", u"鲜", u"贤", u"咸", u"冼", u"线", u"線",
               u"相", u"香", u"湘", u"向", u"项", u"象", u"肖", u"宵", u"萧", u"箫", u"潇", u"蕭", u"小", u"晓", u"孝", u"校", u"偰",
               u"谢", u"謝", u"辛", u"忻", u"信", u"衅", u"星", u"刑", u"邢", u"兴", u"幸", u"性", u"姓", u"雄", u"熊", u"休", u"修",
               u"宿", u"吁", u"须", u"胥", u"顼", u"徐", u"许", u"勖", u"绪", u"续", u"轩", u"宣", u"禤", u"玄", u"薛", u"学", u"雪",
               u"寻", u"郇", u"荀", u"尋", u"牙", u"雅", u"亚", u"烟", u"焉", u"鄢", u"延", u"闫", u"严", u"言", u"岩", u"阎", u"颜",
               u"顏", u"嚴", u"剡", u"彦", u"艳", u"晏", u"宴", u"燕", u"秧", u"扬", u"羊", u"阳", u"杨", u"洋", u"楊", u"卬", u"仰",
               u"养", u"样", u"幺", u"夭", u"尧", u"侥", u"姚", u"珧", u"徭", u"药", u"要", u"爷", u"也", u"冶", u"野", u"业", u"叶",
               u"页", u"葉", u"伊", u"衣", u"依", u"仪", u"夷", u"怡", u"宜", u"移", u"乙", u"以", u"蚁", u"弋", u"义", u"亦", u"易",
               u"奕", u"羿", u"益", u"裔", u"翼", u"阴", u"音", u"殷", u"訚", u"银", u"鄞", u"尹", u"隐", u"印", u"胤", u"英", u"婴",
               u"盈", u"营", u"嬴", u"赢", u"郢", u"应", u"拥", u"庸", u"雍", u"永", u"勇", u"用", u"尤", u"由", u"犹", u"油", u"游",
               u"友", u"有", u"酉", u"右", u"迂", u"於", u"于", u"余", u"鱼", u"俞", u"虞", u"愚", u"宇", u"羽", u"禹", u"庾", u"玉",
               u"聿", u"郁", u"育", u"遇", u"喻", u"御", u"裕", u"愈", u"誉", u"毓", u"僪", u"豫", u"欎", u"鬻", u"元", u"贠", u"员",
               u"袁", u"原", u"源", u"远", u"苑", u"院", u"月", u"岳", u"悦", u"越", u"云", u"雲", u"允", u"运", u"恽", u"载", u"宰",
               u"在", u"昝", u"臧", u"糟", u"早", u"造", u"迮", u"泽", u"笮", u"增", u"甑", u"扎", u"乍", u"斋", u"翟", u"砦", u"粘",
               u"詹", u"瞻", u"斩", u"展", u"占", u"战", u"湛", u"戰", u"张", u"章", u"張", u"彰", u"长", u"仉", u"掌", u"钊", u"招",
               u"昭", u"召", u"兆", u"赵", u"趙", u"肇", u"折", u"者", u"禇", u"柘", u"针", u"真", u"甄", u"阵", u"镇", u"鎮", u"征",
               u"正", u"郑", u"政", u"鄭", u"之", u"支", u"只", u"枝", u"直", u"职", u"植", u"職", u"止", u"志", u"郅", u"治", u"智",
               u"擲", u"中", u"忠", u"终", u"钟", u"衷", u"锺", u"鍾", u"鐘", u"种", u"仲", u"周", u"皱", u"朱", u"邾", u"珠", u"诸",
               u"猪", u"諸", u"騶", u"竹", u"竺", u"主", u"祝", u"專", u"庄", u"荘", u"莊", u"壮", u"卓", u"禚", u"濯", u"资", u"資",
               u"子", u"紫", u"訾", u"自", u"字", u"宗", u"纵", u"縱", u"邹", u"鄒", u"鉏", u"俎", u"祖", u"左", u"佐"]

# 取出四个字以上的名字，分词后汇总，统计词频高于10且明显属于店铺名的词语
shopKeywords = [u"阿呷", u"阿牛", u"安徽", u"白酒", u"百货", u"百姓", u"百杂", u"宝贝", u"保健", u"报刊", u"报摊", u"报亭", u"便利", u"便民", u"宾馆",
                u"槟榔", u"饼屋", u"不夜城", u"部落", u"才店", u"彩票", u"菜店", u"菜馆", u"菜市", u"参茸", u"餐馆", u"餐厅", u"餐饮", u"仓储",
                u"仓买", u"仓卖", u"藏餐", u"曹庄", u"茶店", u"茶坊", u"茶房", u"茶府", u"茶馆", u"茶行", u"茶楼", u"茶社", u"茶室", u"茶业", u"茶叶",
                u"茶艺", u"茶园", u"茶苑", u"茶庄", u"茶荘", u"茶莊", u"茶座", u"超批", u"超市", u"炒货", u"车行", u"大楼", u"大曲", u"大全", u"大厦",
                u"代销", u"蛋糕", u"地摊", u"电话", u"电料", u"电脑", u"电器", u"电信", u"店铺", u"碟屋", u"豆浆", u"二部", u"二店", u"发店", u"发廊",
                u"发屋", u"饭店", u"饭馆", u"饭庄", u"房产", u"肥牛", u"分店", u"服饰", u"服务", u"服装", u"付食", u"复印", u"副食", u"副杂", u"干果",
                u"干货", u"干洗", u"干杂", u"糕点", u"歌城", u"歌厅", u"工地", u"公厕", u"公话", u"公路", u"公司", u"公寓", u"贡酒", u"供销", u"购物",
                u"瓜子", u"管业", u"广场", u"广告", u"国际", u"果行", u"果品", u"果蔬", u"果业", u"果园", u"海鲜", u"行业", u"好又多", u"合肥",
                u"合家", u"红府", u"花店", u"花园", u"华联", u"华停", u"话吧", u"话亭", u"汇总", u"会馆", u"会所", u"婚庆", u"火锅", u"货店", u"货亭",
                u"货栈", u"机关", u"集团", u"集镇", u"加油", u"家电", u"家园", u"监狱", u"建材", u"酱菜", u"酱油", u"酱园", u"饺子", u"经销", u"经营",
                u"精品", u"酒吧", u"酒厂", u"酒城", u"酒店", u"酒鼎", u"酒坊", u"酒馆", u"酒行", u"酒家", u"酒楼", u"酒水", u"酒业", u"酒庄", u"卷烟",
                u"军店", u"咖啡", u"烤吧", u"科技", u"客房", u"客户", u"客栈", u"快餐", u"来购", u"兰停", u"劳保", u"老店", u"老窖", u"老酒", u"乐购",
                u"乐园", u"冷冻", u"冷库", u"冷批", u"冷食", u"冷饮", u"礼品", u"理发", u"连锁", u"联华", u"联通", u"粮店", u"粮行", u"粮液", u"粮油",
                u"量贩", u"淋浴", u"零食", u"零售", u"卤肉", u"路店", u"轮胎", u"旅店", u"旅馆", u"旅社", u"卖部", u"卖点", u"卖店", u"茅台", u"贸易",
                u"煤矿", u"美发", u"美食", u"门店", u"门面", u"门市", u"门业", u"米店", u"米行", u"面馆", u"名茶", u"名酒", u"名品", u"名烟", u"名饮",
                u"茗茶", u"奶亭", u"奶屋", u"奶站", u"南货", u"南杂", u"内衣", u"年华", u"牛奶", u"牛肉", u"农庄", u"农资", u"排档", u"配件", u"配送",
                u"批发", u"批零", u"啤酒", u"品店", u"平价", u"铺子", u"汽车站", u"汽配", u"千乡", u"全羊", u"人家", u"日化", u"日用", u"日杂",
                u"肉店", u"肉食", u"乳品", u"乳业", u"瑞安市", u"山泉", u"山庄", u"商场", u"商超", u"商城", u"商店", u"商行", u"商号", u"商贸",
                u"商铺", u"商厦", u"商社", u"商摊", u"商亭", u"商务", u"商业", u"烧烤", u"社区", u"生店", u"生活", u"生鲜", u"石化", u"石油", u"食店",
                u"食府", u"食品", u"食堂", u"食杂", u"世纪", u"世家", u"世界", u"市部", u"市藏", u"市场", u"饰品", u"书店", u"书社", u"书亭", u"书屋",
                u"蔬菜", u"蔬果", u"熟食", u"涮锅", u"水吧", u"水产", u"水店", u"水果", u"水饺", u"台球", u"摊床", u"摊点", u"摊位", u"糖茶", u"糖果",
                u"糖酒", u"糖食", u"糖烟", u"淘宝", u"特产", u"体彩", u"天下", u"调料", u"调味", u"停业", u"通信", u"通讯", u"网吧", u"网城", u"网咖",
                u"网络", u"网苑", u"维修", u"文化", u"文具", u"文体", u"无字", u"五金", u"舞厅", u"物流", u"洗化", u"洗浴", u"喜铺", u"喜士多",
                u"鲜果", u"鲜奶", u"相馆", u"相山区", u"香烟", u"消费", u"销售", u"小百", u"小部", u"小吃", u"小店", u"小卖", u"小铺", u"小摊",
                u"小屋", u"小学", u"小院", u"鞋店", u"鞋业", u"兴盛", u"烟草", u"烟床", u"烟店", u"烟柜", u"烟行", u"烟酒", u"烟铺", u"烟摊", u"烟亭",
                u"烟杂", u"阳光", u"氧气站", u"药店", u"药房", u"一百", u"一店", u"医院", u"移动", u"驿站", u"音像", u"银行", u"饮料", u"饮食",
                u"印务", u"影碟", u"用品", u"邮亭", u"游乐城", u"有限", u"鱼馆", u"鱼庄", u"渔村", u"渔港", u"渔家", u"渔具", u"浴场", u"浴池",
                u"浴馆", u"浴室", u"杂店", u"杂货", u"招待所", u"诊所", u"之家", u"枝江", u"纸行", u"纸业", u"中国", u"中石化", u"中心", u"中学",
                u"粥铺", u"住宿", u"专卖", u"庄园", u"装饰", u"自选", u"综合", u"总汇", ]

# 四个字以上且以这部分汉字结尾的极有可能为店铺
shopEndWords = [u"店", u"馆", u"坊", u"点", u"行", u"酒", u"社", u"吧"]

# 座机号
regionCodes3 = ["010", "020", "021", "022", "023", "024", "025", "027", "028", "029", "310", "371", "393", "510", "511",
                "512", "513", "516", "519", "535", "570", "571", "572", "574", "575", "576", "577", "579", "592", "631",
                "660", "662", "663", "714", "715", "728", "750", "752", "754", "755", "756", "757", "760", "768", "769",
                "852", "853"]
regionCodes4 = ["0310", "0311", "0312", "0313", "0314", "0315", "0316", "0317", "0318", "0319", "0335", "0349", "0350",
                "0351", "0352", "0353", "0354", "0355", "0356", "0357", "0358", "0359", "0370", "0371", "0372", "0373",
                "0374", "0375", "0376", "0377", "0379", "0391", "0392", "0393", "0394", "0395", "0396", "0398", "0411",
                "0412", "0415", "0416", "0417", "0418", "0419", "0421", "0427", "0429", "0431", "0432", "0433", "0434",
                "0435", "0436", "0437", "0438", "0439", "0451", "0452", "0453", "0454", "0455", "0456", "0457", "0458",
                "0459", "0464", "0467", "0468", "0469", "0470", "0471", "0472", "0473", "0474", "0475", "0476", "0477",
                "0478", "0479", "0482", "0483", "0510", "0511", "0512", "0513", "0514", "0515", "0516", "0517", "0518",
                "0519", "0523", "0527", "0530", "0531", "0532", "0533", "0534", "0535", "0536", "0537", "0538", "0539",
                "0543", "0546", "0550", "0551", "0552", "0553", "0554", "0555", "0556", "0557", "0558", "0559", "0561",
                "0562", "0563", "0564", "0565", "0566", "0570", "0571", "0572", "0573", "0574", "0575", "0576", "0577",
                "0578", "0579", "0580", "0591", "0592", "0593", "0594", "0595", "0596", "0597", "0598", "0599", "0631",
                "0632", "0633", "0634", "0635", "0660", "0662", "0663", "0668", "0691", "0692", "0701", "0710", "0711",
                "0712", "0713", "0714", "0715", "0716", "0717", "0718", "0719", "0722", "0724", "0728", "0730", "0731",
                "0734", "0735", "0736", "0737", "0738", "0739", "0743", "0744", "0745", "0746", "0750", "0751", "0752",
                "0753", "0754", "0755", "0756", "0757", "0758", "0759", "0760", "0762", "0763", "0766", "0768", "0769",
                "0770", "0771", "0772", "0773", "0774", "0775", "0776", "0777", "0778", "0779", "0790", "0791", "0792",
                "0793", "0794", "0795", "0796", "0797", "0798", "0799", "0812", "0813", "0816", "0817", "0818", "0825",
                "0826", "0827", "0830", "0831", "0832", "0833", "0834", "0835", "0836", "0837", "0838", "0839", "0851",
                "0852", "0853", "0854", "0855", "0856", "0857", "0858", "0859", "0870", "0871", "0872", "0873", "0874",
                "0875", "0876", "0877", "0878", "0879", "0883", "0886", "0887", "0888", "0891", "0892", "0893", "0894",
                "0895", "0896", "0897", "0898", "0901", "0902", "0903", "0906", "0908", "0909", "0911", "0912", "0913",
                "0914", "0915", "0916", "0917", "0919", "0930", "0931", "0932", "0933", "0934", "0935", "0936", "0937",
                "0938", "0939", "0941", "0943", "0951", "0952", "0953", "0954", "0955", "0970", "0971", "0972", "0973",
                "0974", "0975", "0976", "0977", "0979", "0990", "0991", "0992", "0993", "0994", "0995", "0996", "0997",
                "0998", "0999"]

# 银行代码
bankMap = {"SRCB": u"深圳农村商业银行", "BGB": u"广西北部湾银行", "SHRCB": u"上海农村商业银行", "BJBANK": u"北京银行", "WHCCB": u"威海市商业银行",
           "BOZK": u"周口银行", "KORLABANK": u"库尔勒市商业银行", "SPABANK": u"平安银行", "SDEB": u"顺德农商银行", "HURCB": u"湖北省农村信用社",
           "WRCB": u"无锡农村商业银行", "BOCY": u"朝阳银行", "CZBANK": u"浙商银行", "HDBANK": u"邯郸银行", "BOC": u"中国银行", "BOD": u"东莞银行",
           "CCB": u"中国建设银行", "ZYCBANK": u"遵义市商业银行", "SXCB": u"绍兴银行", "GZRCU": u"贵州省农村信用社", "ZJKCCB": u"张家口市商业银行",
           "BOJZ": u"锦州银行", "BOP": u"平顶山银行", "HKB": u"汉口银行", "SPDB": u"上海浦东发展银行", "NXRCU": u"宁夏黄河农村商业银行",
           "NYNB": u"广东南粤银行", "GRCB": u"广州农商银行", "BOSZ": u"苏州银行", "HZCB": u"杭州银行", "HSBK": u"衡水银行", "HBC": u"湖北银行",
           "JXBANK": u"嘉兴银行", "HRXJB": u"华融湘江银行", "BODD": u"丹东银行", "AYCB": u"安阳银行", "EGBANK": u"恒丰银行", "CDB": u"国家开发银行",
           "TCRCB": u"江苏太仓农村商业银行", "NJCB": u"南京银行", "ZZBANK": u"郑州银行", "DYCB": u"德阳商业银行", "YBCCB": u"宜宾市商业银行",
           "SCRCU": u"四川省农村信用", "KLB": u"昆仑银行", "LSBANK": u"莱商银行", "YDRCB": u"尧都农商行", "CCQTGB": u"重庆三峡银行",
           "FDB": u"富滇银行", "JSRCU": u"江苏省农村信用联合社", "JNBANK": u"济宁银行", "CMB": u"招商银行", "JINCHB": u"晋城银行JCBANK",
           "FXCB": u"阜新银行", "WHRCB": u"武汉农村商业银行", "HBYCBANK": u"湖北银行宜昌分行", "TZCB": u"台州银行", "TACCB": u"泰安市商业银行",
           "XCYH": u"许昌银行", "CEB": u"中国光大银行", "NXBANK": u"宁夏银行", "HSBANK": u"徽商银行", "JJBANK": u"九江银行",
           "NHQS": u"农信银清算中心", "MTBANK": u"浙江民泰商业银行", "LANGFB": u"廊坊银行", "ASCB": u"鞍山银行", "KSRB": u"昆山农村商业银行",
           "YXCCB": u"玉溪市商业银行", "DLB": u"大连银行", "DRCBCL": u"东莞农村商业银行", "GCB": u"广州银行", "NBBANK": u"宁波银行",
           "BOYK": u"营口银行", "SXRCCU": u"陕西信合", "GLBANK": u"桂林银行", "BOQH": u"青海银行", "CDRCB": u"成都农商银行", "QDCCB": u"青岛银行",
           "HKBEA": u"东亚银行", "HBHSBANK": u"湖北银行黄石分行", "WZCB": u"温州银行", "TRCB": u"天津农商银行", "QLBANK": u"齐鲁银行",
           "GDRCC": u"广东省农村信用社联合社", "ZJTLCB": u"浙江泰隆商业银行", "GZB": u"赣州银行", "GYCB": u"贵阳市商业银行", "CQBANK": u"重庆银行",
           "DAQINGB": u"龙江银行", "CGNB": u"南充市商业银行", "SCCB": u"三门峡银行", "CSRCB": u"常熟农村商业银行", "SHBANK": u"上海银行",
           "JLBANK": u"吉林银行", "CZRCB": u"常州农村信用联社", "BANKWF": u"潍坊银行", "ZRCBANK": u"张家港农村商业银行", "FJHXBC": u"福建海峡银行",
           "ZJNX": u"浙江省农村信用社联合社", "LZYH": u"兰州银行", "JSB": u"晋商银行", "BOHAIB": u"渤海银行", "CZCB": u"浙江稠州商业银行",
           "YQCCB": u"阳泉银行", "SJBANK": u"盛京银行", "XABANK": u"西安银行", "BSB": u"包商银行", "JSBANK": u"江苏银行", "FSCB": u"抚顺银行",
           "HNRCU": u"河南省农村信用", "COMM": u"交通银行", "XTB": u"邢台银行", "CITIC": u"中信银行", "HXBANK": u"华夏银行",
           "HNRCC": u"湖南省农村信用社", "DYCCB": u"东营市商业银行", "ORBANK": u"鄂尔多斯银行", "BJRCB": u"北京农村商业银行", "XYBANK": u"信阳银行",
           "ZGCCB": u"自贡市商业银行", "CDCB": u"成都银行", "HANABANK": u"韩亚银行", "CMBC": u"中国民生银行", "LYBANK": u"洛阳银行",
           "GDB": u"广东发展银行", "ZBCB": u"齐商银行", "CBKF": u"开封市商业银行", "H3CB": u"内蒙古银行", "CIB": u"兴业银行",
           "CRCBANK": u"重庆农村商业银行", "SZSBK": u"石嘴山银行", "DZBANK": u"德州银行", "SRBANK": u"上饶银行", "LSCCB": u"乐山市商业银行",
           "JXRCU": u"江西省农村信用", "ICBC": u"中国工商银行", "JZBANK": u"晋中市商业银行", "HZCCB": u"湖州市商业银行", "NHB": u"南海农村信用联社",
           "XXBANK": u"新乡银行", "JRCB": u"江苏江阴农村商业银行", "YNRCC": u"云南省农村信用社", "ABC": u"中国农业银行", "GXRCU": u"广西省农村信用",
           "PSBC": u"中国邮政储蓄银行", "BZMD": u"驻马店银行", "ARCU": u"安徽省农村信用社", "GSRCU": u"甘肃省农村信用", "LYCB": u"辽阳市商业银行",
           "JLRCU": u"吉林农信", "URMQCCB": u"乌鲁木齐市商业银行", "XLBANK": u"中山小榄村镇银行", "CSCB": u"长沙银行", "JHBANK": u"金华银行",
           "BHB": u"河北银行", "NBYZ": u"鄞州银行", "LSBC": u"临商银行", "BOCD": u"承德银行", "SDRCU": u"山东农信", "NCB": u"南昌银行",
           "TCCB": u"天津银行", "WJRCB": u"吴江农商银行", "CBBQS": u"城市商业银行资金清算中心", "HBRCU": u"河北省农村信用社", "BOHN": u"海南省农村信用社",
           "LNRCC": u"辽宁省农村信用社", "SXRCU": u"山西省农村信用社", "XJRCU": u"新疆农村信用社", "WHB": u"永亨银行", "WHBANK": u"乌海银行",
           "TJBHB": u"天津滨海农村商业银行", "YZBANK": u"银座银行", "TLBANK": u"铁岭银行", "PZBANK": u"盘锦市商业银行", "SLH": u"湖南农村信用社联合社",
           "HLJRCU": u"黑龙江省农村信用社", "FJNX": u"福建省农村信用社", "SCBHK": u"渣打银行", "CJCCB": u"江苏长江银行", "BOCFCB": u"中银富登村银行"}


def kickFullWidth(string, fillExcept):
    """全角转半角:
    全角字符unicode编码65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
    半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）
    空格全角为 12288（0x3000），半角为 32（0x20）
    除空格外，按unicode编码排序半角 + 0x7e= 全角"""
    result = re.sub(u"，", u",", string)
    result = re.sub(u"。", u".", result)
    result = re.sub(u"、", u",", result)
    result = re.sub(u"“", u'"', result)
    result = re.sub(u"”", u'"', result)
    result = re.sub(u"‘", u"'", result)
    result = re.sub(u"’", u"'", result)
    result = re.sub(u"【", u"[", result)
    result = re.sub(u"】", u"]", result)
    result = re.sub(u"《", u"<", result)
    result = re.sub(u"》", u">", result)
    result = re.sub(u"『", u"[", result)
    result = re.sub(u"』", u"]", result)
    result = re.sub(u"「", u"[", result)
    result = re.sub(u"」", u"]", result)
    result = re.sub(u"﹃", u"[", result)
    result = re.sub(u"﹄", u"]", result)
    result = re.sub(u"〔", u"{", result)
    result = re.sub(u"〕", u"}", result)
    result = re.sub(u"—", u"-", result)
    result = re.sub(u"·", u"-", result)
    resultStr = u""
    for i in result:
        try:
            # 返回字符对应的ASCII或Unicode数值
            inside_code = ord(i)
            if inside_code == 12288:
                inside_code = 32
            if 65281 <= inside_code <= 65374:
                inside_code -= 65248
            # 用一个范围在0～255的整数作参数，返回一个对应的字符
            resultStr += chr(inside_code)
        except:
            if fillExcept is None:
                resultStr += i
            else:
                resultStr += fillExcept
    return resultStr
