import numpy as np
from tkinter import *
import math

class Game2048:
    def __init__(self, size=4):
        self.size = size
        self.matrix = np.zeros((self.size, self.size), dtype=int)
        self.score = 0
        self.reset()

    def reset(self):
        """初始化游戏并在两个随机位置添加初始数字"""
        self.new_game()
        self.add_tile()
        self.add_tile()
        self.score = 0

    def new_game(self):
        """创建一个空的矩阵"""
        self.matrix = np.zeros((self.size, self.size), dtype=int)

    def add_tile(self):
        """在矩阵中随机添加一个数字（2或4），使用最小值位置策略"""
        empty_cells, min_value, min_pos = self.find_empty_and_min()
        if len(empty_cells) == 0:
            return self.matrix

        # 找到离最小数字最近的空格子
        if np.array_equal(min_pos, (-1, -1)) or min_value != 2:
            index_pair = empty_cells[np.random.randint(len(empty_cells))]
        else:
            # 找到离最小数字最近的空格子
            
            distances = np.array([self.distance(pos, min_pos) for pos in empty_cells])
            index_pair = empty_cells[np.argmin(distances)]
            
        if min_value == 2:
            ran = np.random.random()  # 确保 ran 是标量
        else:
            ran = np.random.random() * int(math.log(max(self.score, 1), 2))  # 生成一个标量

        # 生成2或4
        new_value = 2 if ran < 0.9 else 4
        
        self.matrix[index_pair[0], index_pair[1]] = new_value


    def distance(self, pos1, pos2):
        """计算两个位置的曼哈顿距离"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def find_empty_and_min(self, flag='all'):
        """查找空格子和最小值的位置"""
        empty_cells = np.argwhere(self.matrix == 0)
        non_zero_elements = self.matrix[self.matrix != 0]
        
        if non_zero_elements.size > 0:
            min_value = np.min(non_zero_elements)
            min_pos = np.argwhere(self.matrix == min_value)[0]
        else:
            min_value, min_pos = float('inf'), (-1, -1)

        if flag == 'empty':
            return empty_cells
        elif flag == 'min':
            return min_value, min_pos
        elif flag == 'all':
            return empty_cells, min_value, min_pos
        else:
            raise ValueError(f"Invalid flag value: {flag}. Must be 'empty', 'min', or 'all'.")

    def slide_and_combine(self, row):
        """将一行的数字先滑动，然后合并，再次滑动"""
        # 移除0并将数字靠一边
        non_zero = row[row != 0]
        new_row = np.zeros_like(row)
        
        # 合并相邻相同的数字
        skip = False
        idx = 0
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                new_row[idx] = 2 * non_zero[i]
                self.score += new_row[idx]
                skip = True
            else:
                new_row[idx] = non_zero[i]
            idx += 1

        return new_row

    def move_left(self):
        """左滑操作"""
        for i in range(self.size):
            self.matrix[i] = self.slide_and_combine(self.matrix[i])

    def move_right(self):
        """右滑操作"""
        for i in range(self.size):
            self.matrix[i] = np.flip(self.slide_and_combine(np.flip(self.matrix[i])))

    def move_up(self):
        """上滑操作"""
        self.matrix = np.transpose(self.matrix)
        self.move_left()  # 上滑等效于左滑转置
        self.matrix = np.transpose(self.matrix)

    def move_down(self):
        """下滑操作"""
        self.matrix = np.transpose(self.matrix)
        self.move_right()  # 下滑等效于右滑转置
        self.matrix = np.transpose(self.matrix)
        
    def move(self, direction):
        if direction == 0:  # 上
            self.move_up()
        elif direction == 1:  # 下
            self.move_down()
        elif direction == 2:  # 左
            self.move_left()
        elif direction == 3:  # 右
            self.move_right()


    def is_game_over(self):
        """判断游戏是否结束，返回 True 表示游戏结束，False 表示游戏未结束"""
        # 检查是否有空格子
        if np.any(self.matrix == 0):
            return False

        # 检查相邻元素是否可以合并
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.matrix[i, j] == self.matrix[i, j + 1] or self.matrix[j, i] == self.matrix[j + 1, i]:
                    return False

        # 如果没有可合并的格子，游戏结束
        return True
SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }

CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }

FONT = ("Verdana", 40, "bold")

class GameGrid(Game2048, Frame):
    def __init__(self, master=None):
        Game2048.__init__(self)  # 初始化游戏逻辑
        Frame.__init__(self, master)  # 初始化图形界面
        self.grid()
        self.master.title('2048')

        
        
        # 添加显示分数的Label
        self.score_label = Label(self, text=f"Score: {self.score}", font=("Verdana", 24, "bold"))
        self.score_label.grid(row=0, column=0, columnspan=4, sticky=W)
        
        #初始化
        self.grid_cells = []
        self.init_grid()
        self.update_grid_cells()
        
        # 绑定键盘事件
        self.master.bind("<Key>", self.key_press)

    def init_grid(self):
        """初始化图形界面的网格"""
        background = Frame(self, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        background.grid()
        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        """更新图形界面的网格"""
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]  # NumPy矩阵中的数字
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        
        self.score_label.configure(text=f"Score: {self.score}")
        self.update_idletasks()

    def key_press(self, event):
        """捕获键盘输入并执行相应操作"""
        key = event.keysym

        if key == 'Up':
            self.move(0)  # 上移
        elif key == 'Down':
            self.move(1)  # 下移
        elif key == 'Left':
            self.move(2)  # 左移
        elif key == 'Right':
            self.move(3)  # 右移
        else:
            return

        # 每次移动后更新图形界面
        self.update_grid_cells()

        # 判断游戏是否结束
        if self.is_game_over():
            self.grid_cells[1][1].configure(text="Game", bg=BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(text="Over!", bg=BACKGROUND_COLOR_CELL_EMPTY)
        else:
            self.add_tile()  # 每次有效移动后添加一个新数字
            self.update_grid_cells()

if __name__ == "__main__":
    root = Tk()
    game = GameGrid(master=root)
    root.mainloop()
