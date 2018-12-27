import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk # pip install pillow
import random, time

#名稱:我要成為神奇日文大師！

####缺:增加特殊模式(限時模式etc)、可以選擇難度(N1~N5)

#要改成讀一個單字檔.csv進來，先暫時用二維清單
voc = [["暖かい","warm"], ["生まれる","to be born"], ["お父さん","(honorable)\nfather"],
       ["外国人","foreigner"], ["降りる","to get off\nto descend"], ["お弁当","boxed\nlunch"],
       ["映画館","cinema"], ["風邪","a cold"],
       ['a','a'],['b','b'],['c','c'],['d','d'],['e','e'],['f','f'],['g','g'],
       ['h','h'],['i','i'],['j','j']
       ]
random.shuffle(voc)


class Japanese(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        f1 = tkFont.Font(size = 80, family = "Berlin Sans FB Demi", weight="bold") #標題
        f2 = tkFont.Font(size = 40, family = "Berlin Sans FB Demi", weight="bold") #標題

        self.lblMain1 = tk.Label(self, text = "一起背日文ㄅ", bg = "cyan", fg = "red",
                                height = 1, width = 20, font = f1) # 製作標題
        self.lblMain1.grid(row = 0, column = 0)# sticky = tk.NE + tk.SW)

        self.lblMain2 = tk.Label(self, text = "Caster", bg = "cyan", fg = "red",
                                height = 1, width = 20, font = f1) # 製作標題
        self.lblMain2.grid(row = 1, column = 0)# sticky = tk.NE + tk.SW)
        
        self.imageNtu = ImageTk.PhotoImage(file = "NTUJP.png")
        self.lblNtuPto = tk.Label(self, image = self.imageNtu, bg = "black", height = 60, width = 220)
        self.lblNtuPto.grid(row = 2, column = 0, columnspan = 2, sticky = tk.SE)

        
        self.btnGame = tk.Button(self, text = "開始遊戲",
                            command=lambda: controller.show_frame(PageOne), font = f2)
        self.btnGame.grid(row = 3, column = 0, sticky = tk.W)

        self.btnRank = tk.Button(self, text = "排行榜",
                            command=lambda: controller.show_frame(PageTwo), font = f2)
        self.btnRank.grid(row = 3, column = 0)

        self.btnFalse = tk.Button(self, text = "錯誤頻率表",
                            command=lambda: controller.show_frame(PageThree), font = f2)
        self.btnFalse.grid(row = 3, column = 0, sticky = tk.E)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        

        #self.remaining = 0
        #self.countdown(60)
        
        self.ansNum = 0
        self.trueCount, self.falseCount = 0, 0

        f1 = tkFont.Font(size = 80, family = "Berlin Sans FB Demi", weight="bold") #標題
        f2 = tkFont.Font(size = 30, family = "Helvetica") #按鈕
        f3 = tkFont.Font(size = 40, family = "Courier New")
        f4 = tkFont.Font(size = 60, family = "Fixdsys") #計時器


        self.option = [voc[0][1], voc[1][1], voc[2][1], voc[3][1]] # 存4個選項的字義
        self.ansStr = self.option[0] # 第一個當答案
        random.shuffle(self.option) # 打亂 讓第一個不會一直是答案
        
        #self.東東們########################
        self.lblCDtimer = tk.Label(self, text = "60", bg = "plum1", height = 2, width = 4, font = f4)
        self.lblCDtimer.grid(row = 0, column = 0, rowspan = 2)
        
        self.lblMain = tk.Label(self, text = voc[0][0], bg = "medium blue",fg = "light cyan",
                                height = 1, width = 14, font = f1) # 製作標題
        self.lblMain.grid(row = 0, column = 1, columnspan = 4)# sticky = tk.NE + tk.SW)
        
        self.score = tk.Label(self, text = "O：0 X：0", bg = "gray55", height = 1, width = 12, font = f3) # 圈?叉?
        self.score.grid(row = 1, column = 2, columnspan = 2)

        self.imageNtu = ImageTk.PhotoImage(file = "NTUJP.png")
        self.lblNtuPto = tk.Label(self, image = self.imageNtu, bg = "black", height = 60, width = 220)
        self.lblNtuPto.grid(row = 1, column = 4, columnspan = 2, sticky = tk.SE)

        self.btnBackMain = tk.Button(self, text="回主選單", font = f2,
                                     command=lambda: controller.show_frame(StartPage))
        self.btnBackMain.grid(row = 3, column = 2, columnspan = 2)
        #self.Btn########################
        self.btn1 = tk.Button(self, text = self.option[0], command = self.clickBtn1,
                              height = 2, width = 10, font = f2, bg = "cyan")
        self.btn2 = tk.Button(self, text = self.option[1], command = self.clickBtn2,
                              height = 2, width = 10, font = f2, bg = "green2")
        self.btn3 = tk.Button(self, text = self.option[2], command = self.clickBtn3,
                              height = 2, width = 10, font = f2, bg = "orange red2")
        self.btn4 = tk.Button(self, text = self.option[3], command = self.clickBtn4,
                              height = 2, width = 10, font = f2, bg = "yellow")
        self.btn1.grid(row = 2, column = 1, rowspan = 1)
        self.btn2.grid(row = 2, column = 2, rowspan = 1)
        self.btn3.grid(row = 2, column = 3, rowspan = 1)
        self.btn4.grid(row = 2, column = 4, rowspan = 1)

    def afterClickBtn(self, textChosen):
        #按鈕按下去會做...
        if textChosen == self.ansStr:
            self.trueCount += 1
            self.score.configure(text = "O：%d X：%d"%(self.trueCount, self.falseCount))
            
            # 做四個隨機不等整數 為答案和其他選項的index
            a, b, c, d = random.sample(range(len(voc) - 1), 4)
            while True: # 避免下一題題目跟上一題一樣
                if a == self.ansNum:
                    a = random.randint(0, len(voc) - 1)
                else:
                    if a not in (b, c, d):
                        self.ansNum = a
                        break
                    else:
                        a = self.ansNum # 避免第二圈a == b or c or d的話會跳不出迴圈

            self.option = [voc[self.ansNum][1], voc[b][1], voc[c][1], voc[d][1]] # 4個選項的字義
            random.shuffle(self.option) # 打亂選項 讓答案不會一直在第一個

            self.question = voc[self.ansNum][0] # 答案的日文
            self.ansStr = voc[self.ansNum][1] # 答案的字義

            self.btn1.configure(text = self.option[0]) # 把4個字義丟入按鈕
            self.btn2.configure(text = self.option[1])
            self.btn3.configure(text = self.option[2])
            self.btn4.configure(text = self.option[3])
            self.lblMain.configure(text = self.question)
            
        else:
            #self.remaining -= 1 # 選錯的話時間扣一秒
            self.falseCount += 1
            self.score.configure(text = "O：%d X：%d"%(self.trueCount, self.falseCount))

    def clickBtn1(self):
        textChosen = self.btn1.cget("text")
        self.afterClickBtn(textChosen)
        
    def clickBtn2(self):
        textChosen = self.btn2.cget("text")
        self.afterClickBtn(textChosen)
        
    def clickBtn3(self):
        textChosen = self.btn3.cget("text")
        self.afterClickBtn(textChosen)
        
    def clickBtn4(self):
        textChosen = self.btn4.cget("text")
        self.afterClickBtn(textChosen)

    """def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.lblCDtimer.configure(text="GG")

        else:
            self.lblCDtimer.configure(text="%d" % self.remaining)
            self.remaining -= 1
            self.after(1000, self.countdown)"""

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three!")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = Japanese()
app.mainloop()
