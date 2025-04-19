#載入模組
import pygame
import os
import random

#初始化
pygame.init()
pygame.mixer.pre_init()

window_width = 1920
window_height = 1080
FPS = 1000
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
running = True


#變數設定
game_win = None #結束後勝利者
mora_win = None #猜拳勝利者 
game_time = 0 #遊戲剩餘時間
difficulty = 0 #選擇難度 0:easy 1:hard 2:expert 3:master
fx = 0 #特效是否啟用
metronome = 0 #節拍器是否啟用
mode = 0 #當前階段 1:猜拳 2:移動
bpm = 0 #遊戲每分鐘節拍數
sec_per_beat = 0 #遊戲每拍秒數
beat_left = 0 #遊戲剩餘節拍數
volume = 10 #音量
scene = 0 #當前場景 1:主畫面 2:設定畫面 3:其他畫面 4:遊戲準備 5:遊戲介面 6:結束畫面
list = 0 
late = 0
time_fix = 0
blue_animation_angle = 0
red_animation_angle = 0
song_played = 0

#節拍變數設定
beat_timer = 0
beat_counter = 0
sec_per_beat_original = 0
key_insert_blue = None
key_insert_red = None
difficulty_bpm = [90, 150, 180, 240]
beat_left_list = [199, 404, 596, 604]

#玩家參數 (座標X,座標y,分數,猜拳,準確率,準確節拍數,是否行動)
red_player_parameter = {'direction_x' : 0,'direction_y' : 0, 'score' : 0,'mora' : '0','accuracy' : 0, 'beat_accurate' : 0, 'action' : 0, 'death' : 0}
blue_player_parameter = {'direction_x' : 0,'direction_y' : 0, 'score' : 0,'mora' : '0','accuracy' : 0, 'beat_accurate' : 0, 'action' : 0, 'death' : 0}

#按鍵輸入資料
blue_mora_insert = ['q', 'w', 'e']
red_mora_insert = ['9', '8', '7']
blue_move_insert = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
red_move_insert = ['7', '8', '9', '4', '5', '6', '1', '2', '3']

#圖片素材載入
leave_img = pygame.image.load(os.path.join('item', 'leave.png')).convert()
remaining_beats_img = pygame.image.load(os.path.join('item','remaining_beats.png')).convert()
background_img = pygame.image.load(os.path.join('item', 'background.png')).convert()
game_area_img = pygame.image.load(os.path.join('item','game_area.png')).convert()
back_button_img = pygame.image.load(os.path.join('item','back_button.png')).convert()
start_button_img = pygame.image.load(os.path.join('item','start_button.png')).convert()
other_button_img = pygame.image.load(os.path.join('item','other_button.png')).convert()
option_button_img = pygame.image.load(os.path.join('item','option_button.png')).convert()
option_title_img = pygame.image.load(os.path.join('item', 'option_title.png')).convert()
title_img = pygame.image.load(os.path.join('item','title.png')).convert()
game_title_img = pygame.image.load(os.path.join('item','game_title.png')).convert()
minus_img = pygame.image.load(os.path.join('item','minus.png')).convert()
plus_img = pygame.image.load(os.path.join('item','plus.png')).convert()
thankslist_img = pygame.image.load(os.path.join('item','thankslist.png')).convert()
thanksword_img = pygame.image.load(os.path.join('item','thanksword.png')).convert()
difficulty_title_img = pygame.image.load(os.path.join('item', 'difficult_title.png')).convert()
difficulty_option_easy_img = pygame.image.load(os.path.join('item', 'difficulty_option_easy.png')).convert()
difficulty_option_hard_img = pygame.image.load(os.path.join('item', 'difficulty_option_hard.png')).convert()
difficulty_option_expert_img = pygame.image.load(os.path.join('item','difficulty_option_expert.png')).convert()
difficulty_option_master_img = pygame.image.load(os.path.join('item','difficulty_option_master.png')).convert()
game_over_img = pygame.image.load(os.path.join('item', 'game_over.png')).convert()
win_img = pygame.image.load(os.path.join('item','win.png')).convert()
tie_img = pygame.image.load(os.path.join('item','tie.png')).convert()
blue_control_area_img = pygame.image.load(os.path.join('item', 'blue_control_area.png')).convert()
blue_paper_img = pygame.image.load(os.path.join('item', 'blue_paper.png')).convert()
blue_scissor_img = pygame.image.load(os.path.join('item', 'blue_scissor.png')).convert()
blue_stone_img = pygame.image.load(os.path.join('item', 'blue_stone.png')).convert()
blue_player_img = pygame.image.load(os.path.join('item','blue_player.png')).convert()
blue_player_death_img = pygame.image.load(os.path.join('item', 'blue_player_death.png')).convert()
red_control_area_img = pygame.image.load(os.path.join('item','red_control_area.png')).convert()
red_paper_img = pygame.image.load(os.path.join('item', 'red_paper.png')).convert()
red_scissor_img = pygame.image.load(os.path.join('item', 'red_scissor.png')).convert()
red_stone_img = pygame.image.load(os.path.join('item', 'red_stone.png')).convert()
red_player_img = pygame.image.load(os.path.join('item','red_player.png')).convert()
red_player_death_img = pygame.image.load(os.path.join('item','red_player_death.png')).convert()
blue_score_0_img = pygame.image.load(os.path.join('item','number', 'blue_score_0.png')).convert()
blue_score_1_img = pygame.image.load(os.path.join('item','number', 'blue_score_1.png')).convert()
blue_score_2_img = pygame.image.load(os.path.join('item','number', 'blue_score_2.png')).convert()
blue_score_3_img = pygame.image.load(os.path.join('item','number', 'blue_score_3.png')).convert()
blue_score_4_img = pygame.image.load(os.path.join('item','number', 'blue_score_4.png')).convert()
blue_score_5_img = pygame.image.load(os.path.join('item','number', 'blue_score_5.png')).convert()
blue_score_6_img = pygame.image.load(os.path.join('item','number', 'blue_score_6.png')).convert()
blue_score_7_img = pygame.image.load(os.path.join('item','number', 'blue_score_7.png')).convert()
blue_score_8_img = pygame.image.load(os.path.join('item','number', 'blue_score_8.png')).convert()
blue_score_9_img = pygame.image.load(os.path.join('item','number', 'blue_score_9.png')).convert()
red_score_0_img = pygame.image.load(os.path.join('item','number', 'red_score_0.png')).convert()
red_score_1_img = pygame.image.load(os.path.join('item','number', 'red_score_1.png')).convert()
red_score_2_img = pygame.image.load(os.path.join('item','number', 'red_score_2.png')).convert()
red_score_3_img = pygame.image.load(os.path.join('item','number', 'red_score_3.png')).convert()
red_score_4_img = pygame.image.load(os.path.join('item','number', 'red_score_4.png')).convert()
red_score_5_img = pygame.image.load(os.path.join('item','number', 'red_score_5.png')).convert()
red_score_6_img = pygame.image.load(os.path.join('item','number', 'red_score_6.png')).convert()
red_score_7_img = pygame.image.load(os.path.join('item','number', 'red_score_7.png')).convert()
red_score_8_img = pygame.image.load(os.path.join('item','number', 'red_score_8.png')).convert()
red_score_9_img = pygame.image.load(os.path.join('item','number', 'red_score_9.png')).convert()
time_0_img = pygame.image.load(os.path.join('item','number', 'time_0.png' )).convert()
time_1_img = pygame.image.load(os.path.join('item','number', 'time_1.png' )).convert()
time_2_img = pygame.image.load(os.path.join('item','number', 'time_2.png' )).convert()
time_3_img = pygame.image.load(os.path.join('item','number', 'time_3.png' )).convert()
time_4_img = pygame.image.load(os.path.join('item','number', 'time_4.png' )).convert()
time_5_img = pygame.image.load(os.path.join('item','number', 'time_5.png' )).convert()
time_6_img = pygame.image.load(os.path.join('item','number', 'time_6.png' )).convert()
time_7_img = pygame.image.load(os.path.join('item','number', 'time_7.png' )).convert()
time_8_img = pygame.image.load(os.path.join('item','number', 'time_8.png' )).convert()
time_9_img = pygame.image.load(os.path.join('item','number', 'time_9.png' )).convert()
time_10_img = pygame.image.load(os.path.join('item','number', 'time_10.png' )).convert()
colon_img = pygame.image.load(os.path.join('item','number', 'time_colon.png' )).convert()

#圖片大小修正
leave_img = pygame.transform.scale(leave_img, (800, 100))
remaining_beats_img = pygame.transform.scale(remaining_beats_img, (400, 150))
background_img = pygame.transform.scale(background_img, (1920, 1080))
game_area_img = pygame.transform.scale(game_area_img, (700, 700))
back_button_img = pygame.transform.scale(back_button_img, (300, 100))
start_button_img = pygame.transform.scale(start_button_img, (300, 100))
other_button_img = pygame.transform.scale(other_button_img, (300, 100))
option_button_img = pygame.transform.scale(option_button_img, (300, 100))
option_title_img = pygame.transform.scale(option_title_img, (300, 100))
title_img = pygame.transform.scale(title_img, (1920, 1080))
game_title_img = pygame.transform.scale(game_title_img, (300, 100))
minus_img = pygame.transform.scale(minus_img, (100,100))
plus_img = pygame.transform.scale(plus_img, (100, 100))
thankslist_img = pygame.transform.scale(thankslist_img, (960, 1080))
thanksword_img = pygame.transform.scale(thanksword_img, (960, 1080))
blue_control_area_img = pygame.transform.scale(blue_control_area_img, (300, 100))
blue_player_img = pygame.transform.scale(blue_player_img, (60, 60))
blue_paper_img = pygame.transform.scale(blue_paper_img, (170, 170))
blue_scissor_img = pygame.transform.scale(blue_scissor_img, (170, 170))
blue_stone_img = pygame.transform.scale(blue_stone_img, (170, 170))
blue_player_death_img = pygame.transform.scale(blue_player_death_img, (100, 100))
red_control_area_img =pygame.transform.scale(red_control_area_img, (300, 100))
red_player_img = pygame.transform.scale(red_player_img, (50, 50))
red_paper_img = pygame.transform.scale(red_paper_img, (170, 170))
red_scissor_img = pygame.transform.scale(red_scissor_img, (170, 170))
red_stone_img = pygame.transform.scale(red_stone_img, (170, 170))
red_player_death_img = pygame.transform.scale(red_player_death_img, (100, 100))
difficulty_title_img = pygame.transform.scale(difficulty_title_img, (500, 100))
difficulty_option_easy_img = pygame.transform.scale(difficulty_option_easy_img, (800, 100))
difficulty_option_hard_img = pygame.transform.scale(difficulty_option_hard_img, (800, 100))
difficulty_option_expert_img = pygame.transform.scale(difficulty_option_expert_img, (800, 100))
difficulty_option_master_img = pygame.transform.scale(difficulty_option_master_img, (800, 100))
game_over_img = pygame.transform.scale(game_over_img, (500, 300)) 
win_img = pygame.transform.scale(win_img, (300, 100))
tie_img = pygame.transform.scale(tie_img, (100, 100))
blue_score_0_img = pygame.transform.scale(blue_score_0_img, (100, 100))
blue_score_1_img = pygame.transform.scale(blue_score_1_img, (60, 100))
blue_score_2_img = pygame.transform.scale(blue_score_2_img, (100, 100))
blue_score_3_img = pygame.transform.scale(blue_score_3_img, (100, 100))
blue_score_4_img = pygame.transform.scale(blue_score_4_img, (100, 100))
blue_score_5_img = pygame.transform.scale(blue_score_5_img, (100, 100))
blue_score_6_img = pygame.transform.scale(blue_score_6_img, (100, 100))
blue_score_7_img = pygame.transform.scale(blue_score_7_img, (100, 100))
blue_score_8_img = pygame.transform.scale(blue_score_8_img, (100, 100))
blue_score_9_img = pygame.transform.scale(blue_score_9_img, (100, 100))
red_score_0_img = pygame.transform.scale(red_score_0_img, (100, 100))
red_score_1_img = pygame.transform.scale(red_score_1_img, (50, 100))
red_score_2_img = pygame.transform.scale(red_score_2_img, (100, 100))
red_score_3_img = pygame.transform.scale(red_score_3_img, (100, 100))
red_score_4_img = pygame.transform.scale(red_score_4_img, (100, 100))
red_score_5_img = pygame.transform.scale(red_score_5_img, (100, 100))
red_score_6_img = pygame.transform.scale(red_score_6_img, (100, 100))
red_score_7_img = pygame.transform.scale(red_score_7_img, (100, 100))
red_score_8_img = pygame.transform.scale(red_score_8_img, (100, 100))
red_score_9_img = pygame.transform.scale(red_score_9_img, (100, 100))
time_0_img = pygame.transform.scale(time_0_img, (100, 100))
time_1_img = pygame.transform.scale(time_1_img, (50, 100))
time_2_img = pygame.transform.scale(time_2_img, (100, 100))
time_3_img = pygame.transform.scale(time_3_img, (100, 100))
time_4_img = pygame.transform.scale(time_4_img, (100, 100))
time_5_img = pygame.transform.scale(time_5_img, (100, 100))
time_6_img = pygame.transform.scale(time_6_img, (100, 100))
time_7_img = pygame.transform.scale(time_7_img, (100, 100))
time_8_img = pygame.transform.scale(time_8_img, (100, 100))
time_9_img = pygame.transform.scale(time_9_img, (100, 100))
time_10_img =pygame.transform.scale(time_10_img, (100, 100))

#圖片去背設定
leave_img.set_colorkey((0,0,0))
remaining_beats_img.set_colorkey((0,0,0))
back_button_img.set_colorkey((0,0,0))
game_area_img.set_colorkey((0,0,0))
start_button_img.set_colorkey((0,0,0))
back_button_img.set_colorkey((0,0,0))
option_button_img.set_colorkey((0,0,0))
other_button_img.set_colorkey((0,0,0))
game_title_img.set_colorkey((0,0,0))
option_title_img.set_colorkey((0,0,0))
title_img.set_colorkey((0,0,0))
minus_img.set_colorkey((0,0,0))
plus_img.set_colorkey((0,0,0))
thankslist_img.set_colorkey((0,0,0))
thanksword_img.set_colorkey((0,0,0))
blue_player_img.set_colorkey((0,0,0))
blue_control_area_img.set_colorkey((255,255,255))
blue_paper_img.set_colorkey((255,255,255))
blue_scissor_img.set_colorkey((255,255,255))
blue_stone_img.set_colorkey((255,255,255))
blue_player_death_img.set_colorkey((0,0,0))
red_player_img.set_colorkey((0,0,0))
red_control_area_img.set_colorkey((255,255,255))
red_paper_img.set_colorkey((255,255,255))
red_scissor_img.set_colorkey((255,255,255))
red_stone_img.set_colorkey((255,255,255))
red_player_death_img.set_colorkey((0,0,0))
difficulty_title_img.set_colorkey((0,0,0))
difficulty_option_easy_img.set_colorkey((0,0,0))
difficulty_option_hard_img.set_colorkey((0,0,0))
difficulty_option_expert_img.set_colorkey((0,0,0))
difficulty_option_master_img.set_colorkey((0,0,0))
game_over_img.set_colorkey((0,0,0))
win_img.set_colorkey((0,0,0))
tie_img.set_colorkey((0,0,0))
blue_score_0_img.set_colorkey((255,255,255))
blue_score_1_img.set_colorkey((255,255,255))
blue_score_2_img.set_colorkey((255,255,255))
blue_score_3_img.set_colorkey((255,255,255))
blue_score_4_img.set_colorkey((255,255,255))
blue_score_5_img.set_colorkey((255,255,255))
blue_score_6_img.set_colorkey((255,255,255))
blue_score_7_img.set_colorkey((255,255,255))
blue_score_8_img.set_colorkey((255,255,255))
blue_score_9_img.set_colorkey((255,255,255))
red_score_0_img.set_colorkey((255,255,255))
red_score_1_img.set_colorkey((255,255,255))
red_score_2_img.set_colorkey((255,255,255))
red_score_3_img.set_colorkey((255,255,255))
red_score_4_img.set_colorkey((255,255,255))
red_score_5_img.set_colorkey((255,255,255))
red_score_6_img.set_colorkey((255,255,255))
red_score_7_img.set_colorkey((255,255,255))
red_score_8_img.set_colorkey((255,255,255))
red_score_9_img.set_colorkey((255,255,255))
time_0_img.set_colorkey((0,0,0))
time_1_img.set_colorkey((0,0,0))
time_2_img.set_colorkey((0,0,0))
time_3_img.set_colorkey((0,0,0))
time_4_img.set_colorkey((0,0,0))
time_5_img.set_colorkey((0,0,0))
time_6_img.set_colorkey((0,0,0))
time_7_img.set_colorkey((0,0,0))
time_8_img.set_colorkey((0,0,0))
time_9_img.set_colorkey((0,0,0))
time_10_img.set_colorkey((0,0,0))

#圖片位置設定
leave_img_rect = leave_img.get_rect(center=(window_width // 2, window_height * 3 // 4))
remaining_beats_img_rect = remaining_beats_img.get_rect(center=(window_width // 2 - 200 , window_height // 8 - 30))
background_img_rect = background_img.get_rect(center=(window_width // 2, window_height // 2))
game_area_img_rect = game_area_img.get_rect(center=(window_width // 2, window_height // 2))
start_button_img_rect_1 = start_button_img.get_rect(center=(window_width // 2, window_height * 3 // 8))
start_button_img_rect_2 = start_button_img.get_rect(center=(window_width // 2, window_height * 7 // 8))
back_button_img_rect = back_button_img.get_rect(center=(200, 150))
option_button_img_rect = option_button_img.get_rect(center=(window_width // 2, window_height // 2))
other_button_img_rect = other_button_img.get_rect(center=(window_width // 2, window_height * 5 // 8))
game_title_img_rect = game_title_img.get_rect(center=(window_width // 2, window_height // 10))
option_title_img_rect = option_title_img.get_rect(center=(window_width // 2, window_height // 10))
title_img_rect = title_img.get_rect(center=(window_width // 2, window_height // 2))
minus_rect = minus_img.get_rect(center=(window_width // 2 - 500, window_height // 2))
plus_rect = plus_img.get_rect(center=(window_width // 2 + 500 , window_height // 2))
thankslist_img_rect = thankslist_img.get_rect(center=(window_width // 2,window_height // 2))
thanksword_img_rect = thanksword_img.get_rect(center=(window_width // 4, window_height * 2 // 3))
blue_player_img_rect = blue_player_img.get_rect(center=(window_width // 2, window_height // 2))
blue_control_area_img_rect = blue_control_area_img.get_rect(center=(window_width // 8, window_height * 5 // 6))
blue_paper_img_rect = blue_paper_img.get_rect(center=(window_width // 8, window_height // 2))
blue_scissor_img_rect = blue_scissor_img.get_rect(center=(window_width // 8, window_height // 2))
blue_stone_img_rect = blue_stone_img.get_rect(center=(window_width // 8, window_height // 2))
blue_player_death_img_rect = blue_player_death_img.get_rect(center=(window_width // 4, window_height // 2))
red_paper_img_rect = red_paper_img.get_rect(center=(window_width * 7 // 8, window_height // 2))
red_scissor_img_rect = red_scissor_img.get_rect(center=(window_width * 7 // 8, window_height // 2))
red_stone_img_rect = red_stone_img.get_rect(center=(window_width * 7 // 8, window_height // 2))
red_player_img_rect = red_player_img.get_rect(center=(window_width // 2, window_height // 2))
red_control_area_img_rect = red_control_area_img.get_rect(center=(window_width * 7 // 8, window_height * 5 // 6))
red_player_death_img_rect = red_player_death_img.get_rect(center=(window_width * 3 // 4, window_height // 2))
difficulty_title_img_rect = difficulty_title_img.get_rect(center=(window_width // 2, window_height // 10))
difficulty_option_easy_img_rect = difficulty_option_easy_img.get_rect(center=(window_width // 2 , window_height // 2))
difficulty_option_hard_img_rect = difficulty_option_hard_img.get_rect(center=(window_width // 2 , window_height // 2))
difficulty_option_expert_img_rect = difficulty_option_expert_img.get_rect(center=(window_width // 2 , window_height // 2))
difficulty_option_master_img_rect = difficulty_option_master_img.get_rect(center=(window_width // 2 , window_height // 2))
game_over_img_rect = game_over_img.get_rect(center=(window_width // 2 , window_height // 8))
win_blue_rect = win_img.get_rect(center=(window_width // 8 , window_height // 2))
win_red_rect = win_img.get_rect(center=(window_width * 7 // 8 , window_height // 2))
tie_img_rect = tie_img.get_rect(center=(window_width // 2 , window_height // 2)) 
blue_score_0_img_rect = blue_score_0_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_1_img_rect = blue_score_1_img.get_rect(center=(window_width // 8 + 150, window_height // 8))
blue_score_2_img_rect = blue_score_2_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_3_img_rect = blue_score_3_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_4_img_rect = blue_score_4_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_5_img_rect = blue_score_5_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_6_img_rect = blue_score_6_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_7_img_rect = blue_score_7_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_8_img_rect = blue_score_8_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_9_img_rect = blue_score_9_img.get_rect(center=(window_width // 8 , window_height // 8))
blue_score_00_img_rect = blue_score_0_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_10_img_rect = blue_score_1_img.get_rect(center=(window_width // 8 + 50 , window_height // 8))
blue_score_20_img_rect = blue_score_2_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_30_img_rect = blue_score_3_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_40_img_rect = blue_score_3_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_50_img_rect = blue_score_5_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_60_img_rect = blue_score_6_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_70_img_rect = blue_score_6_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_80_img_rect = blue_score_8_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
blue_score_90_img_rect = blue_score_9_img.get_rect(center=(window_width // 8 - 100 , window_height // 8))
red_score_00_img_rect = red_score_0_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_10_img_rect = red_score_1_img.get_rect(center=(window_width * 7 // 8 + 50 , window_height // 8))
red_score_20_img_rect = red_score_2_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_30_img_rect = red_score_3_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_40_img_rect = red_score_4_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_50_img_rect = red_score_5_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_60_img_rect = red_score_6_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_70_img_rect = red_score_7_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_80_img_rect = red_score_8_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_90_img_rect = red_score_9_img.get_rect(center=(window_width * 7 // 8 - 100 , window_height // 8))
red_score_0_img_rect = red_score_0_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_1_img_rect = red_score_1_img.get_rect(center=(window_width * 7 // 8 + 200 , window_height // 8))
red_score_2_img_rect = red_score_2_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_3_img_rect = red_score_3_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_4_img_rect = red_score_4_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_5_img_rect = red_score_5_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_6_img_rect = red_score_6_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_7_img_rect = red_score_7_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_8_img_rect = red_score_8_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
red_score_9_img_rect = red_score_9_img.get_rect(center=(window_width * 7 // 8 , window_height // 8))
volume_0_img_rect = time_0_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_1_img_rect = time_1_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_2_img_rect = time_2_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_3_img_rect = time_3_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_4_img_rect = time_4_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_5_img_rect = time_5_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_6_img_rect = time_6_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_7_img_rect = time_7_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_8_img_rect = time_8_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_9_img_rect = time_9_img.get_rect(center=(window_width // 2 , window_height // 2))
volume_10_img_rect = time_10_img.get_rect(center=(window_width // 2 , window_height // 2))
colon_img_rect = colon_img.get_rect(center=(window_width // 2 , window_height // 8))
left_beat_0_img_rect = time_0_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_1_img_rect = time_1_img.get_rect(center=(window_width // 2 + 450, window_height // 8))
left_beat_2_img_rect = time_2_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_3_img_rect = time_3_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_4_img_rect = time_4_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_5_img_rect = time_5_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_6_img_rect = time_6_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_7_img_rect = time_7_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_8_img_rect = time_8_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_9_img_rect = time_9_img.get_rect(center=(window_width // 2 + 300, window_height // 8))
left_beat_00_img_rect = time_0_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_10_img_rect = time_1_img.get_rect(center=(window_width // 2 + 350, window_height // 8))
left_beat_20_img_rect = time_2_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_30_img_rect = time_3_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_40_img_rect = time_4_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_50_img_rect = time_5_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_60_img_rect = time_6_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_70_img_rect = time_7_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_80_img_rect = time_8_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_90_img_rect = time_9_img.get_rect(center=(window_width // 2 + 200, window_height // 8))
left_beat_000_img_rect = time_0_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_100_img_rect = time_1_img.get_rect(center=(window_width // 2 + 250, window_height // 8))
left_beat_200_img_rect = time_2_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_300_img_rect = time_3_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_400_img_rect = time_4_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_500_img_rect = time_5_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_600_img_rect = time_6_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_700_img_rect = time_7_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_800_img_rect = time_8_img.get_rect(center=(window_width // 2 + 100, window_height // 8))
left_beat_900_img_rect = time_9_img.get_rect(center=(window_width // 2 + 100, window_height // 8))

#圖片陣列
time_img = [time_0_img, time_1_img, time_2_img, time_3_img, time_4_img, time_5_img, time_6_img, time_7_img, time_8_img, time_9_img, time_10_img]
valume_rect = [volume_0_img_rect, volume_1_img_rect, volume_2_img_rect, volume_3_img_rect, volume_4_img_rect, volume_5_img_rect, volume_6_img_rect, volume_7_img_rect, volume_8_img_rect, volume_9_img_rect, volume_10_img_rect]
blue_score = [blue_score_0_img, blue_score_1_img, blue_score_2_img, blue_score_3_img, blue_score_4_img, blue_score_5_img, blue_score_6_img, blue_score_7_img, blue_score_8_img, blue_score_9_img]
red_score = [red_score_0_img, red_score_1_img, red_score_2_img, red_score_3_img, red_score_4_img, red_score_5_img, red_score_6_img, red_score_7_img, red_score_8_img, red_score_9_img]
blue_0_score_rect = [blue_score_0_img_rect, blue_score_1_img_rect, blue_score_2_img_rect, blue_score_3_img_rect, blue_score_4_img_rect, blue_score_5_img_rect, blue_score_6_img_rect, blue_score_7_img_rect, blue_score_8_img_rect, blue_score_9_img_rect]
red_0_score_rect = [red_score_0_img_rect, red_score_1_img_rect, red_score_2_img_rect, red_score_3_img_rect, red_score_4_img_rect, red_score_5_img_rect, red_score_6_img_rect, red_score_7_img_rect, red_score_8_img_rect, red_score_9_img_rect]
blue_00_score_rect = [blue_score_00_img_rect, blue_score_10_img_rect, blue_score_20_img_rect, blue_score_30_img_rect, blue_score_40_img_rect, blue_score_50_img_rect, blue_score_60_img_rect, blue_score_70_img_rect, blue_score_80_img_rect, blue_score_90_img_rect]
red_00_score_rect = [red_score_00_img_rect, red_score_10_img_rect, red_score_20_img_rect, red_score_30_img_rect, red_score_40_img_rect, red_score_50_img_rect, red_score_60_img_rect, red_score_60_img_rect, red_score_70_img_rect, red_score_80_img_rect, red_score_90_img_rect]

difficulty_images = [difficulty_option_easy_img, difficulty_option_hard_img, difficulty_option_expert_img, difficulty_option_master_img] 

#遊戲內部座標
blue_player_rect_ingame = blue_player_img_rect
red_player_rect_ingame = red_player_img_rect

#音樂素材載入
pygame.mixer.init()
master_play_music = pygame.mixer.Sound(os.path.join('music','gameplay_master.mp3'))
expert_play_music_2 = pygame.mixer.Sound(os.path.join("music", "gameplay_expert_remake.mp3"))
expert_play_music_1 = pygame.mixer.Sound(os.path.join("music", "gameplay_expert.mp3"))
hard_play_music = pygame.mixer.Sound(os.path.join("music", "gameplay_hard.mp3"))
easy_play_music_2 = pygame.mixer.Sound(os.path.join("music", "gameplay_easy_another.mp3"))
easy_play_music_1 = pygame.mixer.Sound(os.path.join("music", "gameplay_easy.mp3"))
main_loop_music = pygame.mixer.Sound(os.path.join("music", "main_loop.mp3"))
end_music = pygame.mixer.Sound(os.path.join("music", "end.mp3"))

#音效素材載入
beat_sound = pygame.mixer.Sound(os.path.join("music", "sound", "8beat.mp3"))
mora_win_sound = pygame.mixer.Sound(os.path.join("music", "sound", "mouse.mp3"))
move_sound = pygame.mixer.Sound(os.path.join("music", "sound", "move.mp3"))
button_sound = pygame.mixer.Sound(os.path.join("music", "sound", "button.mp3"))
mora_sound = pygame.mixer.Sound(os.path.join("music", "sound", "mora.mp3"))

#音量大小設定
master_play_music.set_volume(1)
expert_play_music_2.set_volume(1)
expert_play_music_1.set_volume(1)
hard_play_music.set_volume(1)
easy_play_music_2.set_volume(1)
easy_play_music_1.set_volume(1)
main_loop_music.set_volume(1)
beat_sound.set_volume(1)
mora_win_sound.set_volume(1)
move_sound.set_volume(1)
button_sound.set_volume(1)
mora_win_sound.set_volume(1)
end_music.set_volume(1)

difficulty_music = [easy_play_music_2, hard_play_music, expert_play_music_2, master_play_music] #音樂陣列

#腳色行為定義
def update ():
    
    global volume
    global scene
    global mode
    global key_insert_blue
    global key_insert_red
    global difficulty
    global blue_player_rect_ingame
    global red_player_rect_ingame
    global sec_per_beat
    global beat_timer
    global beat_counter
    global late
    global mora_win
    global time_fix
    global sec_per_beat_original
    global beat_left
    global song_played
    global game_win
    global running

    if scene == 1: #場景:主畫面
        
        #重複循環 main_loop_music
        if not pygame.mixer.get_busy(): 
            main_loop_music.play(0)
            
        #素材顯示    
        screen.blit(title_img, title_img_rect) 
        screen.blit(start_button_img, start_button_img_rect_1)
        screen.blit(option_button_img, option_button_img_rect)
        screen.blit(other_button_img, other_button_img_rect)
        screen.blit(leave_img, leave_img_rect)
        
        #按鈕設置
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if option_button_img_rect.collidepoint(event.pos): #option_button
                    button_sound.play()
                    scene = 2

                elif other_button_img_rect.collidepoint(event.pos): #other_button
                    button_sound.play()
                    scene = 3

                elif start_button_img_rect_1.collidepoint(event.pos): #start_button
                    button_sound.play()
                    scene = 4

    elif scene == 2: #場景:設定畫面

        #素材顯示
        screen.blit(option_title_img,option_title_img_rect)
        screen.blit(minus_img, minus_rect)
        screen.blit(plus_img, plus_rect)
        screen.blit(back_button_img, back_button_img_rect)
        screen.blit(time_img[volume], valume_rect[volume])
        
        #音量大小固定
        master_play_music.set_volume(volume / 10)
        expert_play_music_2.set_volume(volume / 10)
        expert_play_music_1.set_volume(volume / 10)
        hard_play_music.set_volume(volume / 10)
        easy_play_music_2.set_volume(volume / 10)
        easy_play_music_1.set_volume(volume / 10)
        main_loop_music.set_volume(volume / 10)
        beat_sound.set_volume(volume / 10)
        mora_win_sound.set_volume(volume / 10)
        move_sound.set_volume(volume / 10)
        button_sound.set_volume(volume / 10)
        mora_sound.set_volume(volume / 10)
        end_music.set_volume(volume / 10)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if minus_rect.collidepoint(event.pos): #音量下降
                    if volume > 0:
                        button_sound.play()
                        volume -= 1

                elif plus_rect.collidepoint(event.pos): #音量上升
                    if volume < 10:
                        button_sound.play()
                        volume += 1

                elif back_button_img_rect.collidepoint(event.pos): #返回主畫面
                    button_sound.play()
                    scene = 1

    elif scene == 3: #場景:其他
        
        #素材顯示
        screen.blit(thankslist_img , thankslist_img_rect)

        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                
                if back_button_img_rect.collidepoint(event.pos): #返回主畫面
                    button_sound.play()
                    scene = 1
                            
    elif scene == 4: #場景:遊戲準備
        
        #素材顯示
        screen.blit(difficulty_images[difficulty], difficulty_option_easy_img_rect)
        screen.blit(difficulty_title_img, difficulty_title_img_rect)
        screen.blit(minus_img, minus_rect)
        screen.blit(plus_img, plus_rect)
        screen.blit(back_button_img, back_button_img_rect)
        screen.blit(start_button_img, start_button_img_rect_2)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if minus_rect.collidepoint(event.pos): #難度下降
                    button_sound.play()
                    if difficulty > 0:
                        difficulty -= 1

                elif plus_rect.collidepoint(event.pos): #難度上升
                    button_sound.play()
                    if difficulty < 3:
                        difficulty += 1

                elif back_button_img_rect.collidepoint(event.pos): #返回主畫面
                    button_sound.play()
                    scene = 1


                elif start_button_img_rect_2.collidepoint(event.pos): #遊戲開始
                    
                    # 停止目前播放的背景音樂
                    pygame.mixer.stop()
                    button_sound.play()

                    #玩家分數
                    blue_player_parameter['score'] = 0
                    red_player_parameter['score'] = 0

                    #內部座標重置
                    blue_player_rect_ingame = blue_player_img_rect
                    red_player_rect_ingame = red_player_img_rect
                    blue_player_parameter['direction_x'] = 0
                    blue_player_parameter['direction_y'] = 0
                    red_player_parameter['direction_x'] = 0
                    red_player_parameter['direction_y'] = 0
                    blue_player_parameter['beat_accurate'] = 0
                    red_player_parameter['beat_accurate'] = 0

                    # 定義每一拍的時間（毫秒）
                    sec_per_beat_original = ( 60 / difficulty_bpm[difficulty] ) * 1000
                    sec_per_beat = sec_per_beat_original
                    beat_timer = 0
                    beat_counter = 0
                    late = 0
                    beat_left = beat_left_list[difficulty]

                    # 定義每一拍的狀態
                    mode = "mora"

                    #紀錄勝利者為何方玩家
                    mora_win = None

                    # 設定播放音樂並切換場景
                    song_played = 0
                    scene = 5

    elif scene == 5: #場景:遊戲畫面(主遊戲循環)

        #素材顯示
        screen.blit(blue_control_area_img, blue_control_area_img_rect)
        screen.blit(game_area_img, game_area_img_rect)
        screen.blit(red_control_area_img, red_control_area_img_rect)
        screen.blit(blue_player_img, blue_player_rect_ingame)
        screen.blit(red_player_img, red_player_rect_ingame)
        screen.blit(blue_score[blue_player_parameter['score'] // 10], blue_score_00_img_rect)
        screen.blit(blue_score[blue_player_parameter['score'] % 10], blue_score_0_img_rect)
        screen.blit(red_score[red_player_parameter['score'] // 10], red_score_00_img_rect)
        screen.blit(red_score[red_player_parameter['score'] % 10], red_score_0_img_rect)
        
        if beat_counter >= 8:
            screen.blit(remaining_beats_img, remaining_beats_img_rect)
            screen.blit(time_img[beat_left // 100], left_beat_000_img_rect)
            screen.blit(time_img[beat_left // 10 % 10], left_beat_00_img_rect)
            screen.blit(time_img[beat_left % 10], left_beat_0_img_rect)
            
        elif beat_counter == 5:
            time_3_img_new = pygame.transform.scale(time_3_img,(300,300))
            volume_3_img_rect_new = time_3_img_new.get_rect(center = volume_3_img_rect.center)
            screen.blit(time_3_img_new, volume_3_img_rect_new)
            
        elif beat_counter == 6:
            time_2_img_new = pygame.transform.scale(time_2_img,(300,300))
            volume_2_img_rect_new = time_2_img_new.get_rect(center = volume_2_img_rect.center)
            screen.blit(time_2_img_new, volume_2_img_rect_new)
            
        elif beat_counter == 7:
            time_1_img_new = pygame.transform.scale(time_1_img,(150,300))
            volume_1_img_rect_new = time_1_img_new.get_rect(center = volume_1_img_rect.center)
            screen.blit(time_1_img_new, volume_1_img_rect_new)
            
        if beat_counter == 8:
            start_button_img_new = pygame.transform.scale(start_button_img,(600,200))
            start_button_img_rect_new = start_button_img_new.get_rect(center = volume_1_img_rect.center)
            screen.blit(start_button_img_new, start_button_img_rect_new)
        
        if blue_player_parameter['mora'] == 'paper':
            screen.blit(blue_paper_img, blue_paper_img_rect)
            
        elif blue_player_parameter['mora'] == 'stone':
            screen.blit(blue_stone_img, blue_stone_img_rect)
            
        elif blue_player_parameter['mora'] == 'scissor':
            screen.blit(blue_scissor_img, blue_scissor_img_rect)
            
           
        if red_player_parameter['mora'] == 'paper':
            screen.blit(red_paper_img, red_paper_img_rect)
            
        elif red_player_parameter['mora'] == 'stone':
            screen.blit(red_stone_img, red_stone_img_rect)
            
        elif red_player_parameter['mora'] == 'scissor':
            screen.blit(red_scissor_img, red_scissor_img_rect)
            
        #重置輸入
        key_insert_blue = None
        key_insert_red = None
        judgement_early = sec_per_beat_original - 35
        judgement_late = 35
        
        for event in pygame.event.get():
        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.stop()
                button_sound.play()
                scene = 1

        # 主遊戲
        if beat_counter > 8:
            
            if song_played == 0:
                difficulty_music[difficulty].play()
                song_played = 1
                    
        if beat_counter >= 8:
            
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if mode == "mora": #階段:猜拳

                        if beat_timer >= judgement_early or beat_timer < judgement_late:
                            blue_player_parameter['beat_accurate'] += 1
                            
                            if event.key == pygame.K_q:
                                key_insert_blue = 'q'
                                
                            elif event.key == pygame.K_w:
                                key_insert_blue = 'w'
                                
                            elif event.key == pygame.K_e:
                                key_insert_blue = 'e'

                        else:
                            key_insert_blue = random.choice(blue_mora_insert)

                        if beat_timer >= judgement_early or beat_timer < judgement_late:
                            red_player_parameter['beat_accurate'] += 1
                            
                            if event.key == pygame.K_7:
                                key_insert_red = '7'
                                
                            elif event.key == pygame.K_8:
                                key_insert_red = '8'
                                
                            elif event.key == pygame.K_9:
                                key_insert_red = '9'
                            
                        else:
                            key_insert_red = random.choice(red_mora_insert)

                    elif mode == "move": #階段:移動

                        if beat_timer >= judgement_early or beat_timer < judgement_late:
                            blue_player_parameter['beat_accurate'] += 1
                            
                            if event.key == pygame.K_q:
                                key_insert_blue = 'q'
                                
                            elif event.key == pygame.K_w:
                                key_insert_blue = 'w'
                                
                            elif event.key == pygame.K_e:
                                key_insert_blue = 'e'
                                
                            elif event.key == pygame.K_a:
                                key_insert_blue = 'a'
                                
                            elif event.key == pygame.K_s:
                                key_insert_blue = 's'
                                
                            elif event.key == pygame.K_d:
                                key_insert_blue = 'd'
                                
                            elif event.key == pygame.K_z:
                                key_insert_blue = 'z'
                                
                            elif event.key == pygame.K_x:
                                key_insert_blue = 'x'
                                
                            elif event.key == pygame.K_c:
                                key_insert_blue = 'c' 

                        else:
                            key_insert_blue = random.choice(blue_move_insert)
                        
                        if beat_timer >= judgement_early or beat_timer < judgement_late:
                            red_player_parameter['beat_accurate'] += 1
                            
                            if event.key == pygame.K_7:
                                key_insert_red = '7'
                                
                            elif event.key == pygame.K_8:
                                key_insert_red = '8'
                                
                            elif event.key == pygame.K_9:
                                key_insert_red = '9'
                                
                            elif event.key == pygame.K_4:
                                key_insert_red = '4'
                                
                            elif event.key == pygame.K_5:
                                key_insert_red = '5'
                                
                            elif event.key == pygame.K_6:
                                key_insert_red = '6'
                                
                            elif event.key == pygame.K_1:
                                key_insert_red = '1'
                                
                            elif event.key == pygame.K_2:
                                key_insert_red = '2'
                                
                            elif event.key == pygame.K_3:
                                key_insert_red = '3'    
                            
                        else:
                            key_insert_red = random.choice(red_move_insert)         

        beat_timer += clock.get_time()    # 更新計時器
        
        if blue_player_parameter['death'] == 1:
            blue_death_animation()
            
        if red_player_parameter['death'] == 1:
            red_death_animation()
        

        if beat_timer >= sec_per_beat: # 檢查是否到達下一拍
            
            late += beat_timer - sec_per_beat_original
            sec_per_beat = sec_per_beat_original - time_fix
            
            if late >= 5 :
                time_fix = 5
                
            elif late <= -5:
                time_fix = -5
                
            else:
                time_fix = 0
                
            beat_timer = 0 # 重置計時器
            beat_counter += 1
            beat_left -= 1 
            
            if beat_counter > 8:
                    
                blue_player_parameter['accuracy'] = blue_player_parameter['beat_accurate'] / ( beat_counter - 8 )  
            
                # 根據當前拍的狀態處理遊戲邏輯
                if mode == "mora": #處理猜拳選擇
                    
                    if key_insert_blue is None:       
                        random_mora_blue()
                        
                    else:
                        mora_blue()

                    if key_insert_red is None:
                        random_mora_red()

                    else:
                        mora_red()
                        
                    
                    mora_detect()        
                    # 檢查是否有勝利者
                    if mora_win == 'tie':
                        
                        pass
                    
                    else:
                        
                        # 如果有勝利者，進入下一拍的狀態
                        mode = "move" 
                        
                    blue_player_parameter['action'] = 0
                    red_player_parameter['action'] = 0          

                elif mode == "move": #處理移動選擇
                    
                    # 處理移動方向選擇
                    if key_insert_blue is None:
                        random_move_blue()

                    else:
                        move_blue()
                        
                    if key_insert_red is None:
                        random_move_red()

                    # 根據移動方向更新玩家位置(x,y座標分開用於偵測)
                    else:
                        move_red()

                    # 檢查是否有玩家在同一行或同一列
                    direction_detect()
                    
                    blue_player_parameter['mora'] = '0'
                    red_player_parameter['mora'] = '0'
                    mode = "mora"
                    blue_player_parameter['action'] = 0
                    red_player_parameter['action'] = 0
            else: 
                beat_sound.play()
                    
            screen.blit(blue_player_img, blue_player_rect_ingame)
            screen.blit(red_player_img, red_player_rect_ingame)
            key_insert_blue = None 
            key_insert_red = None
                
        if beat_left <= 0: # 檢查遊戲是否結束（音樂是否停止）
            if blue_player_parameter['score'] > red_player_parameter['score']:
                game_win = "blue"
                
            elif red_player_parameter['score'] > blue_player_parameter['score']:
                game_win = "red"
                
            else:
                game_win = "tie"
                
            scene = 6
            
    elif scene == 6:
        
        back_button_img_rect_new = back_button_img.get_rect(center=(window_width // 2, window_height * 7 // 8))
        
        screen.blit(blue_score[blue_player_parameter['score'] // 10], blue_score_00_img_rect)
        screen.blit(blue_score[blue_player_parameter['score'] % 10], blue_score_0_img_rect)
        screen.blit(red_score[red_player_parameter['score'] // 10], red_score_00_img_rect)
        screen.blit(red_score[red_player_parameter['score'] % 10], red_score_0_img_rect)
        screen.blit(game_over_img, game_area_img_rect)
        screen.blit(back_button_img, back_button_img_rect_new)
        
        if game_win == "blue":
            screen.blit(win_img, win_blue_rect)
            
        elif game_win == "red":
            screen.blit(win_img, win_red_rect)
            
        elif game_win == "tie":
            scene.blit(tie_img, tie_img_rect)
            
        if not pygame.mixer.get_busy(): 
            end_music.play(0)
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:
                    
                    if back_button_img_rect_new.collidepoint(event.pos):
                        pygame.mixer.stop()
                        button_sound.play()
                        scene = 1

def insert_blue_mora():
    
    global key_insert_blue
    
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_q:
                key_insert_blue = 'q'
                
            elif event.key == pygame.K_w:
                key_insert_blue = 'w'
                
            elif event.key == pygame.K_e:
                key_insert_blue = 'e'   
                
def insert_red_mora():
    
    global key_insert_red
    
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_7:
                key_insert_red = '7'
                
            elif event.key == pygame.K_8:
                key_insert_red = '8'
                
            elif event.key == pygame.K_9:
                key_insert_red = '9'                            
            
def mora_detect ():

    global mora_win

    if blue_player_parameter['mora'] == 'paper':

        if red_player_parameter['mora'] == 'paper':
            mora_win = 'tie'

        elif red_player_parameter['mora'] == 'stone':
            mora_win = 'blue'

        elif red_player_parameter['mora'] == 'scissor':
            mora_win = 'red'

    elif blue_player_parameter['mora'] == 'stone':

        if red_player_parameter['mora'] == 'paper':
            mora_win = 'red'

        elif red_player_parameter['mora'] == 'stone':
            mora_win = 'tie'

        elif red_player_parameter['mora'] == 'scissor':
            mora_win = 'blue'

    elif blue_player_parameter['mora'] == 'scissor':

        if red_player_parameter['mora'] == 'scissor':
            mora_win = 'tie'

        elif red_player_parameter['mora'] == 'stone':
            mora_win = 'red'

        elif red_player_parameter['mora'] == 'paper':
            mora_win = 'blue'
    
    if mora_win == 'blue' or mora_win =='red':
        mora_sound.play()
        
    else:
        button_sound.play()

def direction_detect():

    global red_player_rect_ingame
    global blue_player_rect_ingame
    global blue_animation_angle
    global red_animation_angle
    global blue_player_death_img_rect
    global red_player_death_img_rect
    
    if blue_player_parameter['direction_x'] == red_player_parameter['direction_x'] or blue_player_parameter['direction_y'] == red_player_parameter['direction_y'] :
        mora_win_sound.play()
        if mora_win == 'blue':      
            red_player_death_img_rect = red_player_rect_ingame
            
            blue_player_parameter['score'] += 1
            red_player_parameter['direction_x'] = 0
            red_player_parameter['direction_y'] = 0
            red_player_parameter['death'] = 1
            red_animation_angle = 0
        
        elif mora_win == 'red':
            blue_player_death_img_rect = blue_player_rect_ingame
            
            red_player_parameter['score'] += 1
            blue_player_parameter['direction_x'] = 0
            blue_player_parameter['direction_y'] = 0
            blue_player_parameter['death'] = 1 
            blue_animation_angle = 0
    else:
        move_sound.play()
  
    blue_player_rect_ingame = blue_player_img.get_rect(center=(window_width // 2 + blue_player_parameter['direction_x'] * 100, window_height // 2 - blue_player_parameter['direction_y'] * 100))
    red_player_rect_ingame = red_player_img.get_rect(center=(window_width // 2 + red_player_parameter['direction_x'] * 100, window_height // 2 - red_player_parameter['direction_y'] * 100))

def move_blue():

    global blue_player_rect_ingame
    global key_insert_blue
    
    if blue_player_parameter['action'] == 0:
        
        if key_insert_blue == 'q':
            
            if blue_player_parameter['direction_x'] >= -2 and blue_player_parameter['direction_y'] <= 2:
                blue_player_parameter['direction_x'] -= 1
                blue_player_parameter['direction_y'] += 1

        elif key_insert_blue == 'w':
            
            if blue_player_parameter['direction_y'] < 2:
                blue_player_parameter['direction_y'] += 2

        elif key_insert_blue == 'e':
            
            if blue_player_parameter['direction_x'] <= 2 and blue_player_parameter['direction_y'] <= 2:
                blue_player_parameter['direction_x'] += 1
                blue_player_parameter['direction_y'] += 1

        elif key_insert_blue == 'a':
            
            if blue_player_parameter['direction_x'] > -2:
                blue_player_parameter['direction_x'] -= 2

        elif key_insert_blue == 's':
            pass

        elif key_insert_blue == 'e':
            
            if blue_player_parameter['direction_x'] < 2:
                blue_player_parameter['direction_x'] += 2

        elif key_insert_blue == 'z':
            
            if blue_player_parameter['direction_x'] >= -2 and blue_player_parameter['direction_y'] >= -2:
                blue_player_parameter['direction_x'] -= 1
                blue_player_parameter['direction_y'] -= 1

        elif key_insert_blue == 'x':
            
            if blue_player_parameter['direction_y'] > -2:
                blue_player_parameter['direction_y'] -= 2

        elif key_insert_blue == 'c':
            
            if blue_player_parameter['direction_x'] <= 2 and red_player_parameter['direction_y'] >= -2:
                blue_player_parameter['direction_x'] += 1
                blue_player_parameter['direction_y'] -= 1
        
        blue_player_parameter['action'] = 1

        blue_player_rect_ingame = blue_player_img.get_rect(center=(window_width + blue_player_parameter['direction_x'] * 100, window_height + blue_player_parameter['direction_y'] * 100))

def move_red():

    global red_player_rect_ingame
    global key_insert_red
    if red_player_parameter['action'] == 0:

        if key_insert_red == '7':
            
            if red_player_parameter['direction_x'] >= -2 and red_player_parameter['direaction_y'] <= 2:
                red_player_parameter['direction_x'] -= 1
                red_player_parameter['direction_y'] += 1

        elif key_insert_red == '8':
            
            if red_player_parameter['direction_y'] < 2:
                red_player_parameter['direction_y'] += 2

        elif key_insert_red == '9':
            
            if red_player_parameter['direction_x'] <= 2 and red_player_parameter['direaction_y'] <= 2:
                red_player_parameter['direction_x'] += 1
                red_player_parameter['direction_y'] += 1

        elif key_insert_red == '4':
            
            if red_player_parameter['direction_x'] > -2:
                red_player_parameter['direction_x'] -= 2

        elif key_insert_red == '5':
            pass

        elif key_insert_red == '6':
            
            if red_player_parameter['direction_x'] < 2:
                red_player_parameter['direction_x'] += 2

        elif key_insert_red == '1':
            
            if red_player_parameter['direction_x'] >= -2 and red_player_parameter['direaction_y'] >= -2:
                red_player_parameter['direction_x'] -= 1
                red_player_parameter['direction_y'] -= 1

        elif key_insert_red == '2':
            
            if red_player_parameter['direction_y'] > -2:
                red_player_parameter['direction_y'] -= 2

        elif key_insert_red == '3':
            
            if red_player_parameter['direction_x'] <= 2 and red_player_parameter['direaction_y'] >= -2:
                red_player_parameter['direction_x'] += 1
                red_player_parameter['direction_y'] -= 1
                
        red_player_parameter['action'] = 1
        
        red_player_rect_ingame = red_player_img.get_rect(center=(window_width + red_player_parameter['direction_x'] * 100, window_height + red_player_parameter['direction_y'] * 100))

def random_move_blue():

    global blue_player_rect_ingame      
    rand = 0
    rand = random.randint(1,9)
    
    if blue_player_parameter['action'] == 0:
        
        if rand == 1:
            
            if blue_player_parameter['direction_x'] >= -2 and blue_player_parameter['direction_y'] <= 2:  
                blue_player_parameter['direction_x'] -= 1
                blue_player_parameter['direction_y'] += 1
            
        elif rand == 2:
            
            if blue_player_parameter['direction_y'] < 2:
                blue_player_parameter['direction_y'] += 2

        elif rand == 3:
            
            if blue_player_parameter['direction_x'] <= 2 and blue_player_parameter['direction_y'] <= 2:
                blue_player_parameter['direction_x'] += 1
                blue_player_parameter['direction_y'] += 1

        elif rand == 4:
            
            if blue_player_parameter['direction_x'] > -2:
                blue_player_parameter['direction_x'] -= 2

        elif rand == 5:
            pass
        
        elif rand == 6:
            
            if blue_player_parameter['direction_x'] < 2:
                blue_player_parameter['direction_x'] += 2

        elif rand == 7:
            
            if blue_player_parameter['direction_x'] >= -2 and blue_player_parameter['direction_y'] >= -2:
                blue_player_parameter['direction_x'] -= 1
                blue_player_parameter['direction_y'] -= 1

        elif rand == 8:
            
            if blue_player_parameter['direction_y'] > -2:
                blue_player_parameter['direction_y'] -= 2

        elif rand == 9:
            
            if blue_player_parameter['direction_x'] <= 2 and blue_player_parameter['direction_y'] >= -2:
                blue_player_parameter['direction_x'] += 1
                blue_player_parameter['direction_y'] -= 1
                
        blue_player_parameter['action'] = 1

        blue_player_rect_ingame = blue_player_img.get_rect(center=(window_width // 2 + blue_player_parameter['direction_x'] * 100, window_height // 2 - blue_player_parameter['direction_y'] * 100))

def random_move_red():

    global red_player_rect_ingame
    
    rand = 0
    rand = random.randint(1,9)
    
    if red_player_parameter['action'] == 0:
        
        if rand == 1:
            
            if red_player_parameter['direction_x'] >= -2 and red_player_parameter['direction_y'] <= 2:
                red_player_parameter['direction_x'] -= 1
                red_player_parameter['direction_y'] += 1

        elif rand == 2:
            
            if red_player_parameter['direction_y'] < 2:
                red_player_parameter['direction_y'] += 2

        elif rand == 3:
            
            if red_player_parameter['direction_x'] <= 2 and red_player_parameter['direction_y'] <= 2:
                red_player_parameter['direction_x'] += 1
                red_player_parameter['direction_y'] += 1

        elif rand == 4:
            
            if red_player_parameter['direction_x'] > -2:
                red_player_parameter['direction_x'] -= 2

        elif rand == 5:
            pass

        elif rand == 6:
            
            if red_player_parameter['direction_x'] < 2:
                red_player_parameter['direction_x'] += 2

        elif rand == 7:
            
            if red_player_parameter['direction_x'] >= -2 and red_player_parameter['direction_y'] >= -2:
                red_player_parameter['direction_x'] -= 1
                red_player_parameter['direction_y'] -= 1

        elif rand == 8:
            
            if red_player_parameter['direction_y'] > -2:
                red_player_parameter['direction_y'] -= 2

        elif rand == 9:
            
            if red_player_parameter['direction_x'] <= 2 and red_player_parameter['direction_y'] >= -2:
                red_player_parameter['direction_x'] += 1
                red_player_parameter['direction_y'] -= 1
                
        red_player_parameter['action'] = 1
        
        red_player_rect_ingame = red_player_img.get_rect(center=(window_width // 2 + red_player_parameter['direction_x'] * 100, window_height // 2 - red_player_parameter['direction_y'] * 100))

def mora_blue():
    
    global key_insert_blue
    
    if blue_player_parameter['action'] == 0:
        
        if key_insert_blue == 'q':
            blue_player_parameter['mora'] = 'paper'

        elif key_insert_blue == 'w':
            blue_player_parameter['mora'] = 'stone'
            

        elif key_insert_blue == 'e':
            blue_player_parameter['mora'] = 'scissor'
            
        blue_player_parameter['action'] = 1

def mora_red():
    
    global key_insert_red
    
    if red_player_parameter['action'] == 0:
        
        if key_insert_red == '7':
            red_player_parameter['mora'] = 'paper'

        elif key_insert_red == '8':
            red_player_parameter['mora'] = 'stone'

        elif key_insert_red == '9':
            red_player_parameter['mora'] = 'scissor'
            
        red_player_parameter['action'] = 1

def random_mora_blue():

    rand = 0
    rand = random.randint(1,3)
    
    if blue_player_parameter['action'] == 0:
        
        if rand == 1:
            blue_player_parameter['mora'] = 'paper'

        elif rand == 2:  
            blue_player_parameter['mora'] = 'stone'

        elif rand == 3:
            blue_player_parameter['mora'] = 'scissor'

        blue_player_parameter['action'] = 1

def random_mora_red():

    rand = 0
    rand = random.randint(1,3)
    
    if red_player_parameter['action'] == 0:
        
        if rand == 1:
            red_player_parameter['mora'] = 'paper'

        elif rand == 2:  
            red_player_parameter['mora'] = 'stone'

        elif rand == 3:
            red_player_parameter['mora'] = 'scissor'
            
        red_player_parameter['action'] = 1

def blue_death_animation():
    global blue_player_death_img
    global blue_player_death_img_rect
    global blue_animation_angle
    
    blue_player_death_img_new = pygame.transform.rotate(blue_player_death_img, blue_animation_angle % 360)
    blue_player_death_img_rect_new = blue_player_death_img_new.get_rect(center=blue_player_death_img_rect.center)
    screen.blit(blue_player_death_img_new , blue_player_death_img_rect_new)
  
    blue_animation_angle += 10
    
    if blue_animation_angle >= 1800:
        blue_player_parameter['death'] = 0
        
def red_death_animation():
    global red_player_death_img
    global red_player_death_img_rect
    global red_animation_angle

    red_player_death_img_new = pygame.transform.rotate(red_player_death_img, red_animation_angle % 360)
    red_player_death_img_rect_new = red_player_death_img_new.get_rect(center=red_player_death_img_rect.center)
    screen.blit(red_player_death_img_new, red_player_death_img_rect_new)
    
    red_animation_angle += 10
    
    if red_animation_angle >= 1800:
        red_player_parameter['death'] = 0   
        
#遊戲迴圈
running = True

scene = 1
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    screen.fill((0,0,0))
    

    update()
    
    pygame.display.flip()

pygame.quit()