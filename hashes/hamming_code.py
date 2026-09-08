# 作者:João Gustavo A. Amorim & Gabriel Kunz
# 作者邮箱:joaogustavoamorim@gmail.com 和 gabriel-kunz@uergs.edu.br
# 编写时间:2019 年 4 月
# Black: True

"""
* 本代码实现了汉明码(Hamming code):
    https://en.wikipedia.org/wiki/Hamming_code —— 在通信领域中,
汉明码是一族线性纠错码。汉明码可以检测两位以内的错误,或在不检测
未纠正错误的情况下纠正一位错误。相比之下,简单奇偶校验码无法纠错,
也只能检测出奇数个比特错误。汉明码是完备码,也就是说,在相同码块
长度与最小距离为 3 的条件下,它们达到了尽可能高的码率。

* 本实现包括:
    * 负责对消息进行编码的函数(emitterConverter)
        * 返回编码后的消息
    * 负责对消息进行解码的函数(receptorConverter)
        * 返回解码后的消息和数据完整性确认(ack)

* 使用方法:
        使用时必须声明希望在消息中包含多少个校验位(sizePari)。
        (出于测试目的)还需要选择一个将被强制置错的比特位。
    这用于检查汉明码是否工作正常。
        最后,给出需要编码的消息/单词变量(text)。

* 工作流程:
        声明变量(sizePari、be、text)

        使用 text_to_bits 函数把消息/单词(text)转换为二进制
        按照汉明编码规则对消息进行编码
        按照汉明编码规则对消息进行解码
        打印原始消息、编码后的消息和解码后的消息

        在编码后的文本变量中强制制造一个错误
        对被强制置错的消息进行解码
        打印原始消息、编码后的消息、被篡改后的消息和解码后的消息
"""

# 导入
import numpy as np


# 二进制转换函数--------------------------------------
def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    """
    >>> text_to_bits("msg")
    '011011010111001101100111'
    """
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding="utf-8", errors="surrogatepass"):
    """
    >>> text_from_bits('011011010111001101100111')
    'msg'
    """
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


# 汉明码相关函数-------------------------------------------
def emitter_converter(size_par, data):
    """
    :param size_par: 消息必须包含的校验位个数
    :param data: 信息位
    :return: 将通过不可靠信道传输的消息
            ——信息位与校验位合并后的序列

    >>> emitter_converter(4, "101010111111")
    ['1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1']
    >>> emitter_converter(5, "101010111111")
    Traceback (most recent call last):
        ...
    ValueError: size of parity don't match with size of data
    """
    if size_par + len(data) <= 2**size_par - (len(data) - 1):
        raise ValueError("size of parity don't match with size of data")

    data_out = []
    parity = []
    bin_pos = [bin(x)[2:] for x in range(1, size_par + len(data) + 1)]

    # 按输出数据的规模整理后的信息数据
    data_ord = []
    # 数据位置模板 + 校验位
    data_out_gab = []
    # 校验位计数器
    qtd_bp = 0
    # 数据位的位置计数器
    cont_data = 0

    for x in range(1, size_par + len(data) + 1):
        # 生成比特位置模板——哪些位置放数据位,
        # 哪些位置放校验位
        if qtd_bp < size_par:
            if (np.log(x) / np.log(2)).is_integer():
                data_out_gab.append("P")
                qtd_bp = qtd_bp + 1
            else:
                data_out_gab.append("D")
        else:
            data_out_gab.append("D")

        # 把数据重新排布到新的输出规模中
        if data_out_gab[-1] == "D":
            data_ord.append(data[cont_data])
            cont_data += 1
        else:
            data_ord.append(None)

    # 计算校验位
    for bp in range(1, size_par + 1):
        # 给定校验位对应的 1 比特计数器
        cont_bo = 0
        # 控制循环读取的计数器
        for cont_loop, x in enumerate(data_ord):
            if x is not None:
                try:
                    aux = (bin_pos[cont_loop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1" and x == "1":
                    cont_bo += 1
        parity.append(cont_bo % 2)

    # 组装消息
    cont_bp = 0  # 校验位计数器
    for x in range(size_par + len(data)):
        if data_ord[x] is None:
            data_out.append(str(parity[cont_bp]))
            cont_bp += 1
        else:
            data_out.append(data_ord[x])

    return data_out


def receptor_converter(size_par, data):
    """
    >>> receptor_converter(4, "1111010010111111")
    (['1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1'], True)
    """
    # 数据位置模板 + 校验位
    data_out_gab = []
    # 校验位计数器
    qtd_bp = 0
    # 数据位读取计数器
    cont_data = 0
    # 收到的校验位列表
    parity_received = []
    data_output = []

    for i, item in enumerate(data, 1):
        # 生成比特位置模板——哪些位置放数据位,
        #  哪些位置放校验位
        if qtd_bp < size_par and (np.log(i) / np.log(2)).is_integer():
            data_out_gab.append("P")
            qtd_bp = qtd_bp + 1
        else:
            data_out_gab.append("D")

        # 把数据重新排布到新的输出规模中
        if data_out_gab[-1] == "D":
            data_output.append(item)
        else:
            parity_received.append(item)

    # -----------用数据计算校验位
    data_out = []
    parity = []
    bin_pos = [bin(x)[2:] for x in range(1, size_par + len(data_output) + 1)]

    #  按输出数据的规模整理后的信息数据
    data_ord = []
    # 数据位置反馈 + 校验位
    data_out_gab = []
    # 校验位计数器
    qtd_bp = 0
    # 数据位读取计数器
    cont_data = 0

    for x in range(1, size_par + len(data_output) + 1):
        # 生成比特位置模板——哪些位置放数据位,
        # 哪些位置放校验位
        if qtd_bp < size_par and (np.log(x) / np.log(2)).is_integer():
            data_out_gab.append("P")
            qtd_bp = qtd_bp + 1
        else:
            data_out_gab.append("D")

        # 把数据重新排布到新的输出规模中
        if data_out_gab[-1] == "D":
            data_ord.append(data_output[cont_data])
            cont_data += 1
        else:
            data_ord.append(None)

    # 计算校验位
    for bp in range(1, size_par + 1):
        # 给定校验位对应的 1 比特计数器
        cont_bo = 0
        for cont_loop, x in enumerate(data_ord):
            if x is not None:
                try:
                    aux = (bin_pos[cont_loop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1" and x == "1":
                    cont_bo += 1
        parity.append(str(cont_bo % 2))

    # 组装消息
    cont_bp = 0  # 校验位计数器
    for x in range(size_par + len(data_output)):
        if data_ord[x] is None:
            data_out.append(str(parity[cont_bp]))
            cont_bp += 1
        else:
            data_out.append(data_ord[x])

    ack = parity_received == parity
    return data_output, ack


# ---------------------------------------------------------------------
"""
# 使用示例

# 校验位个数
sizePari = 4

# 将被强制置错的比特位置
be = 2

# 需要用汉明码编码和解码的消息/单词
# text = input("Enter the word to be read: ")
text = "Message01"

# 把消息转换为二进制
binaryText = text_to_bits(text)

# 打印字符串的二进制形式
print("Text input in binary is '" + binaryText + "'")

# 总传输比特数
totalBits = len(binaryText) + sizePari
print("Size of data is " + str(totalBits))

print("\n --Message exchange--")
print("Data to send ------------> " + binaryText)
dataOut = emitterConverter(sizePari, binaryText)
print("Data converted ----------> " + "".join(dataOut))
dataReceiv, ack = receptorConverter(sizePari, dataOut)
print(
    "Data receive ------------> "
    + "".join(dataReceiv)
    + "\t\t -- Data integrity: "
    + str(ack)
)


print("\n --Force error--")
print("Data to send ------------> " + binaryText)
dataOut = emitterConverter(sizePari, binaryText)
print("Data converted ----------> " + "".join(dataOut))

# 强制制造错误
dataOut[-be] = "1" * (dataOut[-be] == "0") + "0" * (dataOut[-be] == "1")
print("Data after transmission -> " + "".join(dataOut))
dataReceiv, ack = receptorConverter(sizePari, dataOut)
print(
    "Data receive ------------> "
    + "".join(dataReceiv)
    + "\t\t -- Data integrity: "
    + str(ack)
)
"""
