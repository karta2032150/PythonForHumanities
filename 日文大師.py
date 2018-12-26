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

class Japanese(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.creatWidgets()
        self.remaining = 0
        self.countdown(60)
        
        self.ansNum = 0
        self.trueCount, self.falseCount = 0, 0

    def creatWidgets(self):
        f1 = tkFont.Font(size = 80, family = "Berlin Sans FB Demi", weight="bold") #標題
        f2 = tkFont.Font(size = 30, family = "Helvetica") #按鈕
        f3 = tkFont.Font(size = 40, family = "Courier New")
        f4 = tkFont.Font(size = 60, family = "Fixdsys") #計時器
        rgb1      = (183,247,49)           #rgb 顏色設定
        bgcolor   = "#%02x%02x%02x" % rgb1 #將rgb格式轉成hex格式


        self.option = [voc[0][1], voc[1][1], voc[2][1], voc[3][1]] # 存4個選項的字義
        self.ansStr = self.option[0] # 第一個當答案
        random.shuffle(self.option) # 打亂 讓第一個不會一直是答案
        
        self.lblMain = tk.Label(self, text = voc[0][0], bg = "medium blue",fg = "light cyan",
                            height = 1, width = 10, font = f1) # 製作標題
        self.score = tk.Label(self, text = "O：0 X：0", bg = "gray55",
                              height = 1, width = 12, font = f3) # 圈?叉?
        
        self.imageNtu = ImageTk.PhotoImage(file = "NTUJP.png")
        self.lblNtu = tk.Label(self, image = self.imageNtu, bg = "black",
                            height = 60, width = 220)
        self.lblCDtimer = tk.Label(self, text = "60", bg = "plum1",
                            height = 2, width = 4, font = f4)

        #製作按鈕、按鈕格式 , command = 指定成一個函式
        self.btn1 = tk.Button(self, text = self.option[0], command = self.clickBtn1,
                              height = 3, width = 14, font = f2, bg = "cyan")
        self.btn2 = tk.Button(self, text = self.option[1], command = self.clickBtn2,
                              height = 3, width = 14, font = f2, bg = "green2")
        self.btn3 = tk.Button(self, text = self.option[2], command = self.clickBtn3,
                              height = 3, width = 14, font = f2, bg = "orange red2")
        self.btn4 = tk.Button(self, text = self.option[3], command = self.clickBtn4,
                              height = 3, width = 14, font = f2, bg = "yellow")

        #Label Grid
        self.lblMain.grid(row = 1, column = 0, columnspan = 25)# sticky = tk.NE + tk.SW)
        self.score.grid(row = 2, column = 5, columnspan = 10)
        self.lblNtu.grid(row = 2, column = 20, columnspan = 13, rowspan = 2)
        self.lblCDtimer.grid(row = 1, column = 1, rowspan = 2)

        #Button Grid
        self.btn1.grid(row = 5, column = 1, rowspan = 4, columnspan = 2)
        self.btn2.grid(row = 5, column = 7, rowspan = 4, columnspan = 2)# sticky = tk.NE + tk.SW)
        self.btn3.grid(row = 5, column = 13, rowspan = 4, columnspan = 2)# sticky = tk.NE + tk.SW)
        self.btn4.grid(row = 5, column = 19, rowspan = 4, columnspan = 2)
   
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
            self.remaining -= 1 # 選錯的話時間扣一秒
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

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.lblCDtimer.configure(text="GG")

        else:
            self.lblCDtimer.configure(text="%d" % self.remaining)
            self.remaining -= 1
            self.after(1000, self.countdown)
            
jp = Japanese()
jp.master.title("成為日文大師吧！")
jp.mainloop()
    
