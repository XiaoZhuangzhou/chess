import Tools

INF = 10000000
saber_move = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
saber_map = [[INF for col in range(64)] for row in range(64)]
path_map = [[col for col in range(64)] for row in range(64)]
final_Pos = INF
protect_saber = INF
encounter_Pos = INF
tools = Tools.tools()
sucurrent_listary = INF


def get_path(start, end, path_list=[]):
    temp_node = path_map[start][end]
    while temp_node != end:
      path_list.append(temp_node)
      temp_node = path_map[temp_node][end]
    if len(path_list) == 0 or path_list[-1] != end:
      path_list.append(end)
    return path_list


def run(saber_start, king_position):
    saber_start = saber_start
    saber_index = len(saber_start)
    print(saber_start,king_position)
    for i in range(64):
        saber_map[i][i] = 0
    for i in range(64):
        for j in range(8):
           tx = tools.get_xy(i)[0] + saber_move[j][0]
           ty = tools.get_xy(i)[1] + saber_move[j][1]
           if tools.check(tx, ty):
               next_step = tools.get_position(tx, ty)
               saber_map[i][next_step] = 1
    for k in range(64):
        for i in range(64):
           for j in range(64):
              if saber_map[i][k] + saber_map[k][j] < saber_map[i][j]:
                 saber_map[i][j] = saber_map[i][k] + saber_map[k][j]
                 path_map[i][j] = k
    min_move = INF
    for final_p in range(64):
        for encounter_p in range(64):
           for enc_index in range(saber_index):
               sucurrent_listary = tools.get_encost(king_position, encounter_p)
               for sa_index in range(saber_index):
                   sucurrent_listary += saber_map[saber_start[sa_index]][final_p]
               sucurrent_listary += saber_map[saber_start[enc_index]][encounter_p] \
                           + saber_map[encounter_p][final_p] \
                           - saber_map[saber_start[enc_index]][final_p]
               if sucurrent_listary < min_move:
                     min_move = sucurrent_listary
                     final_Pos = final_p
                     protect_saber = enc_index
                     encounter_Pos = encounter_p
    dicts = {}
    for i in range(len(saber_start)+1):
       current_list = list()
       if i == protect_saber:
          current_list.append(saber_start[i])
          current_list=get_path(saber_start[i],encounter_Pos,current_list)
          current_list.extend(get_path(encounter_Pos,final_Pos))
       elif i == len(saber_start):
          current_list.append(king_position)
          x1 = (int)(king_position/8)
          x2 = (int)(encounter_Pos/8)
          y1 = king_position%8
          y2 = encounter_Pos%8
          while x1 > x2:
             x1 -= 1
             current_list.append(tools.get_position(x1, y1))
          while x1 < x2:
             x1 += 1
             current_list.append(tools.get_position(x1, y1))
          while y1 > y2:
             y1 -= 1
             current_list.append(tools.get_position(x1, y1))
          while y1 > y2:
             x1 += 1
             current_list.append(tools.get_position(x1, y1))
          current_list.extend(get_path(encounter_Pos, final_Pos))
       else :
          current_list.append(saber_start[i])
          current_list=get_path(saber_start[i], final_Pos,current_list)
       dicts[i] = current_list
    return dicts, min_move, encounter_Pos, final_Pos, protect_saber
