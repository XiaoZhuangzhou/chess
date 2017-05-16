import Tools


class ChessAlgorithm:
    def __init__(self, saber_start, king_position):
        self.INF = 10000000
        self.saber_move = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        self.saber_map = [[self.INF for col in range(64)] for row in range(64)]
        self.rem_map = [[col for col in range(64)] for row in range(64)]
        self.king_p = king_position
        self.min_move = self.INF
        self.saber_start = saber_start
        self.saber_index = len(saber_start)
        self.final_Pos = self.INF
        self.protect_saber = self.INF
        self.encounter_Pos = self.INF
        self.tools = Tools.tools()
        self.tmp = []
        self.sum = self.INF
        self.result_map = [[]]

    def suanchu(self, start, end):
        self.tmp = []
        self.tmp.append(start)
        temp = self.rem_map[start][end]
        while temp is not end:
            self.tmp.append(temp)
            temp = self.rem_map[temp][end]
        self.tmp.append(end)
        return self.tmp

    def run(self):
        for i in range(64):
            self.saber_map[i][i] = 0
        for i in range(64):
            for j in range(8):
                tx = self.tools.get_xy(i)[0] + self.saber_move[j][0]
                ty = self.tools.get_xy(i)[1] + self.saber_move[j][1]
                if self.tools.check(tx, ty):
                    next_step = self.tools.get_position(tx, ty)
                    self.saber_map[i][next_step] = 1
        for k in range(64):
            for i in range(64):
                for j in range(64):
                    if self.saber_map[i][k] + self.saber_map[k][j] < self.saber_map[i][j]:
                        self.saber_map[i][j] = self.saber_map[i][k] + self.saber_map[k][j]
                        self.rem_map[i][j] = k
        for final_p in range(64):
            for encounter_p in range(64):
                for enc_index in range(self.saber_index):
                    self.sum = self.tools.get_encost(self.king_p, encounter_p)
                    for sa_index in range(self.saber_index):
                        self.sum += self.saber_map[self.saber_start[sa_index]][final_p]
                        self.sum += self.saber_map[self.saber_start[enc_index]][encounter_p] \
                                + self.saber_map[encounter_p][final_p] \
                                - self.saber_map[self.saber_start[enc_index]][final_p]
                    if self.sum < self.min_move:
                        self.min_move = self.sum
                        self.final_Pos = final_p
                        self.protect_saber = enc_index
                        self. encounter_Pos = encounter_p
        dicts = {}
        for i in range(len(self.saber_start)+1):
            self.result_map = [[self.INF for col in range(len(self.saber_start)+1)] for row in range(self.min_move+1)]
            if i == self.protect_saber:
                self.mm=self.suanchu(self.saber_start[i],self.encounter_Pos)
                self.mm.remove(self.mm[len(self.mm)-1])
                self.mm.extend(self.suanchu(self.encounter_Pos,self.final_Pos))
            elif i == len(self.saber_start):
                self.mm=[]
                self.mm.append(self.king_p)
                self.x1 = (int)(self.king_p/8)
                self.x2 = (int)(self.encounter_Pos/8)
                self.y1 = self.king_p%8
                self.y2 = self.encounter_Pos%8
                while self.x1 > self.x2:
                    self.x1 -= 1
                    self.mm.append(self.tools.get_position(self.x1, self.y1))
                while self.x1 < self.x2:
                    self.x1 += 1
                    self.mm.append(self.tools.get_position(self.x1, self.y1))
                while self.y1 > self.y2:
                    self.y1 -= 1
                    self.mm.append(self.tools.get_position(self.x1, self.y1))
                while self.y1 > self.y2:
                    self.x1 += 1
                    self.mm.append(self.tools.get_position(self.x1, self.y1))
            else :
                self.mm=self.suanchu(self.saber_start[i], self.final_Pos)
            print(self.mm)
            dicts[i]=self.mm
        print(dicts)
