class tools():
  def check(self, x, y):
    if 8 > x >= 0 and 8 > y >= 0:
      return True
    else:
      return False

  def get_xy(self, p):
    return [int(p/8), p%8]

  def get_position(self, x_num, y_num):
    return int(8*x_num+y_num)

  def get_encost(self, x, y):
    return abs(int(x/8)-int(y/8))+abs(x%8-y%8)

  def pos_to_posxy(self, pos, CHESS_SIZE):
      posxy = [(pos % 8)*CHESS_SIZE+CHESS_SIZE/2,int(pos/8)*CHESS_SIZE+CHESS_SIZE/2]
      return posxy

  def pos_to_pos12xy(self,pos1,pos2,CHESS_SIZE):
      pos12xy = [(pos1 % 8-pos2 % 8)*CHESS_SIZE,(int(pos1/8)-int(pos2/8))*CHESS_SIZE]
      return pos12xy