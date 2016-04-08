# coding: utf-8
import jio
import re
import jieba

jieba.load_userdict('../data/dict.txt')
with open('t.txt', 'r') as f:
    tr = f.read()
    print(tr)
    print('/////////////////////\n')
    tr = jio.wash_data(tr)
    sent = jio.split_sentence(tr)
    print(sent)
    for sentence in sent:
        p_v_dict = jio.get_properties_and_values(sentence)
        print(p_v_dict)

# r = '扣除该被告已支付原告的赔偿款人民币15000元'
# if re.match(r'(扣除|总计|合计).*',r):
#     print('matched')
#
# s ='生活费'
#
# print(s.replace('费费','费'))
#
# t = [('a','b','c'),('d','e','f')]
# print(t)
# t.remove(('a','b','c'))
# print(t)

# string = '住院伙食补助费930.00元'
# print(len(string))
# pattern = re.compile(
#             r'\D(((\d)[千仟])?((\d)[百佰]|零)?((\d)[十拾]|零)?(\d)?万)?((\d)[千仟]|零)?((\d)[百佰]|零)?((\d)[十拾]|零)?(\d)?元零?((\d|零)角|零)?(([1-9])分)?')
# string = re.sub(pattern, jio.repl_2dig, string)
# dict1 = jio.get_properties_and_values(string)
# print(dict1)

l = []
l.append(10)
l.append(3)
print(l)