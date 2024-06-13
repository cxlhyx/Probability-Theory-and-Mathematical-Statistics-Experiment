import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题


def root():  # 菜单设置函数
    root = tk.Tk()  # 创建一个窗口
    root.title("概率论与数理统计实验, 研制者：黄堉轩")  # 定义窗口名称
    root.geometry('1100x650+250+75')  # 窗口宽度x窗口高度+窗口x轴+窗口y轴

    # 定义菜单
    bar = tk.Menu(root)  # bar为root下的菜单
    # 配置菜单栏，窗口root加入菜单bar
    root.config(menu=bar)
    bar1 = tk.Menu(bar, tearoff=0)  # bar1，2，3，4为bar下的菜单, tearoff = 0 菜单就不会有虚线
    bar2 = tk.Menu(bar, tearoff=0)  # tearoff 点击子菜单中的 ---------，可以将其“撕下“，默认为True，设为False关闭
    bar3 = tk.Menu(bar, tearoff=0)
    bar4 = tk.Menu(bar, tearoff=0)
    # 菜单bar下加入菜单bar1,2,3,4， 菜单名.add_cascade(label=菜单名，menu=菜单), 功能:级联子菜单和上层菜单
    bar.add_cascade(label='1', menu=bar1)
    bar.add_cascade(label='2', menu=bar2)
    bar.add_cascade(label='3', menu=bar3)
    bar.add_cascade(label='4', menu=bar4)
    # 菜单bar1，2，3，4下加入标签， 菜单名.add_command(label=标签名)， 功能:加入标签
    # add_command有下面几个属性：　　label：指定标签的名称 command:被点击时调用的方法 acceletor：快捷键 underline：是否拥有下划线
    # 除了默认的点击后无显示的效果，Menu还可以设置单选框（add_radiobutton）与复选框(add_checkbutton)，只需对应地替换掉add_command
    bar1.add_command(label="利用蒙特卡洛方法计算圆周率并展示结果", command=bar1_label, accelerator='Alt+1')
    bar2.add_command(
        label="验证泊松定理并展示，对于泊松分布固定的" + chr(955) + "，随着二项分布n的增加，二项分布逐渐收敛于泊松分布",
        command=bar2_lavel, accelerator='Alt+2')
    bar3.add_command(
        label="给定参数" + chr(956) + "，" + chr(963) + "，展示对应的正态分布概率密度图；通过动态调整参数" + chr(
            956) + "或" + chr(963) + "，展示图像的变化", command=bar3_lavel, accelerator='Alt+3')
    bar4.add_command(
        label="生成正态分布的样本，验证大数定律。画图展示随着样本容量的增加，随机变量的算术平均依概率收敛到数学期望",
        command=bar4_lavel, accelerator='Alt+4')
    bar.add_command(label='关于', command=state)
    # add_separator()方法可以添加分割线，调用的时候很简单，需要在哪添加，就把这行代码放在那个地方

    root.mainloop()  # 显示窗口


def bar1_label():  # 实验1图像绘制函数
    root1 = tk.Tk()  # 创建一个新窗口
    root1.title('利用蒙特卡洛方法计算圆周率并展示结果')  # 窗口标题
    root1.geometry('1100x650+250+75')  # 窗口大小

    def bar1_label_0(n='1000'):  # 随机点默认为1000
        try:
            n = int(eval(n))  # 将随机点数目向下取整
        except:
            n = 1000  # 默认为1000

        figure1 = plt.figure(num='利用蒙特卡洛方法计算圆周率并展示结果', figsize=(11, 6.5))  # 设置画布，figure(),画布名，大小
        FigureCanvasTkAgg(figure1, root1).get_tk_widget().place(x=0, y=0)  # 让画布在窗口上显示
        entry = tk.Entry(root1, bg='white', fg='black', width=10)  # 在窗口添加输入框
        entry.place(x=300, y=607)  # 放置输入框位置
        tk.Button(root1, text='开始演示', command=lambda: bar1_label_0(entry.get()), height=1, fg='blue').place(x=775,
                                                                                                                y=603)  # 在窗口放置一个按钮
        tk.Label(root1, text='随机点的数目n:', bg='white').place(x=200, y=605)  # 在窗口添加标签

        plt.clf()  # 清空原来图像
        # 绘制子图，subplot命令:可以将figure对象分为多个区域，每个区域分别放置一个Axes对象进行绘图。 三个参数：行，列，序号
        # plt.subplot(221)  # 前面两个参数分别表示行和列，即将figure分为2行2列的区域，该图形的位置为第一行的左图
        # plt.subplot(222)  # 第一行的右图
        # plt.subplot(212)  # 第二整行
        # 绘制第一个子图
        plt.subplot(2, 1, 1)
        # 绘制随机点
        m = 0  # 落在圆内的随机点数目
        count = 0  # 试验次数
        pi = []  # pi列表
        x_list = np.random.uniform(-1, 1, size=n)  # 生产随机点的横坐标
        y_list = np.random.uniform(-1, 1, size=n)  # 生产随机点的纵坐标
        for x, y in zip(x_list, y_list):  # 实验
            count += 1
            if x * x + y * y <= 1:
                color = 'b'
                m += 1  # 计算落在圆内的随机点数目
            else:
                color = '#FF9900'  # 调整随机点颜色
            plt.scatter(x, y, c=color, marker='.')
            pi.append(4 * m / count)  # 添加pi
        # 绘制方框
        x_list1 = [1, 1, -1, -1, 1]  # 四个端点横坐标
        y_list1 = [-1, 1, 1, -1, -1]  # 四个端点纵坐标, 最后回到起点，形成封闭图形
        plt.plot(x_list1, y_list1, color='#FF9900', label='生成的随机点数目：n=' + str(n))
        # 绘制圆
        x_list2_0 = list(range(-1000, 1001, 1))  # range()步长为整数，横坐标初始化
        x_list2 = []  # 横坐标列表
        y_list2 = []  # 纵坐标列表
        for i in x_list2_0:  # 上半圆坐标
            x = i / 1000  # 初始横坐标/1000，得到横坐标
            x_list2.append(x)  # 横坐标列表添加横坐标
            y = (1 - x ** 2) ** 0.5  # 计算纵坐标
            y_list2.append(y)  # 纵坐标列表添加纵坐标
        x_list2.extend([x for x in x_list2[::-1]])  # 下半圆坐标
        y_list2.extend([-y for y in y_list2[::-1]])
        plt.plot(x_list2, y_list2, color='b', label='落在圆内的随机点数目：m=' + str(m))
        # 设置数轴刻度
        plt.xticks([-1, 0, 1, 2, 3])
        plt.yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
        # 创建字体，设置图例 legend()图例创建函数，prop字体设置参数，loc位置设置参数
        myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf', size=12)
        plt.legend(prop=myfont, loc='upper right')
        # 绘制第二个子图
        plt.subplot(2, 1, 2)
        plt.plot([0, n], [3.1415926, 3.1415926], label=chr(960) + '的理论值：3.1415926', color='y')  # pi理论值
        plt.plot(list(range(0, n)), pi, label=chr(960) + '的模拟计算值：' + str(pi[n - 1]), color='#006699')  # pi实验值
        # 设置数轴上下限
        plt.ylim(2.9, 3.3)
        # 设置数轴刻度
        plt.yticks([2.9, 3.0, 3.1, 3.2, 3.3])
        # 创建字体，设置图例 legend()图例创建函数，prop字体设置参数，loc位置设置参数
        myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf', size=12)
        plt.legend(prop=myfont, loc='upper right')

    bar1_label_0()  # 绘制图像
    root1.mainloop()  # 显示窗口


def bar2_lavel():  # 实验2图像绘制函数
    def jiechen(x):
        if x == 0:
            return 1
        else:
            return x * jiechen(x - 1)

    root2 = tk.Tk()  # 创建一个新窗口
    root2.title(
        "验证泊松定理并展示，对于泊松分布固定的" + chr(955) + "，随着二项分布n的增加，二项分布逐渐收敛于泊松分布")  # 窗口标题
    root2.geometry('1100x650+250+75')  # 窗口大小

    def bar2_lavel_0(lamela='5.00'):
        try:
            lamela = eval(lamela)
        except:
            lamela = 5.00

        figure2 = plt.figure(
            num="验证泊松定理并展示，对于泊松分布固定的" + chr(955) + "，随着二项分布n的增加，二项分布逐渐收敛于泊松分布",
            figsize=(11, 6.5))
        FigureCanvasTkAgg(figure2, root2).get_tk_widget().place(x=0, y=0)  # 让画布在窗口上显示
        entry = tk.Entry(root2, bg='white', fg='black', width=10)  # 在窗口添加输入框
        entry.place(x=350, y=607)  # 放置输入框位置
        tk.Button(root2, text='开始演示', command=lambda: bar2_lavel_0(entry.get()), height=1, fg='blue').place(x=775,
                                                                                                                y=603)  # 在窗口放置一个按钮
        tk.Label(root2, text='参数(请输入4~15之间的数)' + chr(955) + '=', bg='white').place(x=175, y=605)  # 在窗口添加标签

        plt.clf()
        x_list = list(range(0, 21))
        n = 400
        e = 2.71828
        p_n = lamela / n
        y_1_list = [jiechen(n) / jiechen(n - i) / jiechen(i) * p_n ** i * (1 - p_n) ** (n - i) for i in x_list]  # 二项分布
        y_2_list = [lamela ** i * e ** (lamela * (-1)) / jiechen(i) for i in x_list]  # 泊松分布
        plt.subplot(2, 1, 1)
        plt.title('n=' + str(n) + ',p$_n$=' + str(p_n) + ',' + chr(955) + '=np$_n$=' + str(lamela))
        plt.bar(x_list, y_1_list, width=0.05, color='#006699')
        plt.scatter(x_list, y_1_list, s=28, marker='.', color='#006699')
        plt.subplot(2, 1, 2)
        plt.title(chr(955) + '=' + str(lamela))
        plt.bar(x_list, y_2_list, width=0.05, color='#006699')
        plt.scatter(x_list, y_2_list, s=28, marker='.', color='#006699')
        plt.xlabel('随机变量')

    bar2_lavel_0()
    root2.mainloop()  # 显示窗口


def bar3_lavel():  # 实验3图像绘制函数
    root3 = tk.Tk()  # 创建一个新窗口
    root3.title("给定参数" + chr(956) + "，" + chr(963) + "，展示对应的正态分布概率密度图；通过动态调整参数" + chr(
        956) + "或" + chr(963) + "，展示图像的变化")  # 窗口标题
    root3.geometry('1100x650+250+75')  # 窗口大小

    def bar3_lavel_0(miu='0.00', sigema2='1.00'):
        try:
            miu = eval(miu)
        except:
            miu = 0.00
        try:
            sigema2 = eval(sigema2)
        except:
            sigema2 = 1.00

        figure3 = plt.figure(
            num="给定参数" + chr(956) + "，" + chr(963) + "，展示对应的正态分布概率密度图；通过动态调整参数" + chr(
                956) + "或" + chr(963) + "，展示图像的变化", figsize=(11, 6.5))
        FigureCanvasTkAgg(figure3, root3).get_tk_widget().place(x=0, y=0)  # 让画布在窗口上显示
        entry1 = tk.Entry(root3, bg='white', fg='black', width=10)  # 在窗口添加输入框u
        entry1.place(x=200, y=605)  # 放置输入框位置
        entry2 = tk.Entry(root3, bg='white', fg='black', width=10)  # sigema
        entry2.place(x=350, y=607)
        tk.Button(root3, text='均值' + chr(956) + '变化[1,50]',
                  command=lambda: bar3_lavel_0(str(miu + 1.00), str(sigema2)), height=1, ).place(x=625, y=603)
        tk.Button(root3, text='方差' + chr(963) + '\u00B2变化[1,4]',
                  command=lambda: bar3_lavel_0(str(miu), str(sigema2 + 1.00)), height=1).place(x=750, y=603)
        tk.Button(root3, text='开始演示', command=lambda: bar3_lavel_0(entry1.get(), entry2.get()), height=1,
                  fg='blue').place(x=875, y=603)  # 在窗口放置一个按钮
        tk.Label(root3, text='均值' + chr(956) + '=', bg='white').place(x=150, y=605)  # 在窗口添加标签
        tk.Label(root3, text='方差' + chr(963) + '\u00B2=', bg='white').place(x=300, y=605)  # 在窗口添加标签

        plt.clf()
        e = 2.71828
        pi = 3.14
        x_list = [i / 1000 for i in range(int(1000 * miu - 6000), int(1000 * miu + 6001))]
        y_list = [1 / (((2 * pi) ** 0.5) * (sigema2 ** 0.5)) * e ** (-1 * (i - miu) ** 2 / (2 * sigema2)) for i in
                  x_list]
        plt.title(chr(956) + '=' + str(miu) + ';' + chr(963) + '$^2$=' + str(sigema2))
        plt.plot(x_list, y_list, color='#006699')
        plt.xlabel('随机变量')
        plt.ylabel('概率密度')
        plt.plot([miu, miu], [0.00, 1 / (((2 * pi) ** 0.5) * (sigema2 ** 0.5))], color='red', linestyle='--')

    bar3_lavel_0()
    root3.mainloop()  # 显示窗口


def bar4_lavel():  # 实验4图像绘制函数
    root4 = tk.Tk()  # 创建一个新窗口
    root4.title(
        "生成正态分布的样本，验证大数定律。画图展示随着样本容量的增加，随机变量的算术平均依概率收敛到数学期望")  # 窗口标题
    root4.geometry('1100x650+250+75')  # 窗口大小

    def bar4_lavel_0(n='200', miu='85', sigema2='4'):
        try:
            n = eval(n)
        except:
            n = 200
        try:
            miu = eval(miu)
        except:
            miu = 85
        try:
            sigema2 = eval(sigema2)
        except:
            sigema2 = 4

        figure4 = plt.figure(
            num="生成正态分布的样本，验证大数定律。画图展示随着样本容量的增加，随机变量的算术平均依概率收敛到数学期望",
            figsize=(11, 6.5))
        FigureCanvasTkAgg(figure4, root4).get_tk_widget().place(x=0, y=0)  # 让画布在窗口上显示
        entry1 = tk.Entry(root4, bg='white', fg='black', width=10)  # 在窗口添加输入框评委人数
        entry1.place(x=215, y=605)  # 放置输入框位置
        entry2 = tk.Entry(root4, bg='white', fg='black', width=10)  # 数学期望
        entry2.place(x=365, y=607)
        entry3 = tk.Entry(root4, bg='white', fg='black', width=10)  # 方差
        entry3.place(x=500, y=605)
        tk.Button(root4, text='开始演示', command=lambda: bar4_lavel_0(entry1.get(), entry2.get(), entry3.get()),
                  height=1, fg='blue').place(x=875, y=603)  # 在窗口放置一个按钮
        tk.Label(root4, text='评委人数=', bg='white').place(x=150, y=605)  # 在窗口添加标签
        tk.Label(root4, text='数学期望=', bg='white').place(x=300, y=605)  # 在窗口添加标签
        tk.Label(root4, text='方差=', bg='white').place(x=460, y=605)  # 在窗口添加标签

        plt.clf()
        x_list = list(range(1, n + 1))
        y_list1 = [i * sigema2 ** 0.5 + miu for i in np.random.standard_normal(n)]
        y_list2 = [sum(y_list1[1:i + 1]) / i for i in range(1, n + 1)]
        plt.bar(x_list, y_list1, width=0.77, color='#006699')
        plt.scatter(x_list, y_list1, s=28, marker='.', color='#006699', label='评委打分')
        plt.plot(x_list, y_list2, color='red', label='前n项均值')
        plt.plot([0, n], [miu, miu], color='green', label='数学期望')
        # 创建字体，设置图例 legend()图例创建函数，prop字体设置参数，loc位置设置参数
        myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf', size=12)
        plt.legend(prop=myfont, loc='upper right')
        plt.ylim(miu - 7, miu + 7)
        plt.xlim(0, n)

    bar4_lavel_0()
    root4.mainloop()  # 显示窗口


def state():  # 关于函数
    root_state = tk.Tk()
    root_state.title('关于')
    root_state.geometry('300x300+650+250')
    tk.Label(root_state, text='制作者：黄堉轩\n 版本：1.0.0').pack()
    root_state.mainloop()


if __name__ == '__main__':
    root()
