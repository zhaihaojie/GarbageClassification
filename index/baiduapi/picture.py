from .api_client import client

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_result(file):
    image = get_file_content(file)

    """ 调用通用物体和场景识别 """
    result = client.advancedGeneral(image)
    print(result)
    return result
# """ 如果有可选参数 """
# options = {}
# options["baike_num"] = 5
#
# """ 带参数调用通用物体和场景识别 """
# result = client.advancedGeneral(image, options)
# print(result)
if "__name__" == "main":
    trash = {}
    dry = '餐巾纸、卫生间用纸、尿不湿、狗尿垫、猫砂、烟蒂、污损纸张、干燥剂、污损塑料、尼龙制品、编织袋、防醉气泡膜、大骨头、硬贝壳、硬果实、毛发、灰土、炉渣、檬皮泥、太空沙、陶瓷花盆、带胶制品、旧毛巾、一次胜餐具、镜子、陶瓷制品、竹制品、成分复杂的制品 '
    trash['recyclable'] = ['废纸张', '废塑料', '废玻璃制品', '废金属', '废织物', '其他']
    trash['dry'] = dry.split('、')
    trash['wet'] = ['食材废料', '剩菜剩饭', '过期食品', '瓜皮果核', '花卉植物', '中药药渣']
    trash['harmful'] = ['废电池', '废荧光灯管', '废药品及其包装物', '废油漆和溶剂及其包装物', '废矿物油及其包装物', '废含汞温度计', '废含汞血压计']
    print(trash)
