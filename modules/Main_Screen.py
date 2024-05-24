import sys
import pygame
import threading
import pickle
import os
import cfg
import time
import Main
from modules.Textbox import *
from modules.Accounts import *
from modules.Load_Game import *
from modules.Maze_Generator import *
from modules.maze_solver import *
from modules.Hero import *
from modules.Leaderboard import *


'''Game start / level switching / game end interface'''


def Interface_Game_Start(screen, cfg, Username, Password):
    pygame.display.set_mode(cfg.SCREENSIZE)
    font = pygame.font.SysFont('Consolas', 30)
    clock = pygame.time.Clock()
    Interface_Running = True
    while Interface_Running:
        screen.fill((192, 192, 192))
        BackGround = Background('resources/images/tamvagiahuy.png', [0, 0])
        screen.blit(BackGround.image, BackGround.rect)
        buttons = []
        
        buttons.append(Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//3), 'START', font))
        buttons.append(Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//2), 'LOAD GAME', font))
        buttons.append(Button(screen, ((cfg.SCREENSIZE[0]-200)//2, (cfg.SCREENSIZE[1]//2)+(cfg.SCREENSIZE[1]//2-cfg.SCREENSIZE[1]//3)), 'LEADERBOARD', font))
        buttons.append(Button(screen, ((cfg.SCREENSIZE[0]-200)//2, (cfg.SCREENSIZE[1]//2)+(cfg.SCREENSIZE[1]//2-cfg.SCREENSIZE[1]//3)*2), 'QUIT', font))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    expanded_button = button.inflate(130, 130)
                    if expanded_button.collidepoint(pygame.mouse.get_pos()):
                        print("Button clicked") 
                        if i == len(buttons) - 1:  # If the last button (quit button) is clicked
                            pygame.quit()
                            sys.exit(-1)
                        elif i == 1:  # Next_Button=
                            return 'Load_Game'
                        elif i == 2:
                            return 'Leaderboard'
                        else:
                            return 'Difficulty' # If any other button is clicked

        pygame.display.update()
        clock.tick(cfg.FPS)
def Interface_Game_Switch(screen, cfg):
    pygame.display.set_mode(cfg.SCREENSIZE)
    font = pygame.font.SysFont('Consolas', 30)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((192, 192, 192))
        BackGround = Background('resources/images/tamvagiahuy.png', [0, 0])
        screen.blit(BackGround.image, BackGround.rect)
        next_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//3), 'NEXT', font)
        main_menu_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//2), 'MAIN MENU', font)
        quit_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, (cfg.SCREENSIZE[1]//2)+(cfg.SCREENSIZE[1]//2-cfg.SCREENSIZE[1]//3)), 'QUIT', font)
        expanded_next_button = next_button.inflate(130, 130)
        expanded_main_menu_button = main_menu_button.inflate(130, 130)
        expanded_quit_button = quit_button.inflate(130, 130)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if expanded_quit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit(-1)
                elif expanded_next_button.collidepoint(pygame.mouse.get_pos()):
                    return True
                elif expanded_main_menu_button.collidepoint(pygame.mouse.get_pos()):
                    return True
                    

        pygame.display.update()
        clock.tick(cfg.FPS)
def Interface_Difficulty(screen, cfg, Username, Password):
    pygame.display.set_mode(cfg.SCREENSIZE)
    font = pygame.font.SysFont('Consolas', 30)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((192, 192, 192))
        BackGround = Background('resources/images/tamvagiahuy.png', [0, 0])
        screen.blit(BackGround.image, BackGround.rect)
        easy_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//3), 'EASY', font)
        medium_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//2), 'MEDIUM', font)
        hard_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, (cfg.SCREENSIZE[1]//2)+(cfg.SCREENSIZE[1]//2-cfg.SCREENSIZE[1]//3)), 'HARD', font)
        main_menu_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, (cfg.SCREENSIZE[1]//2)+(cfg.SCREENSIZE[1]//2-cfg.SCREENSIZE[1]//3)*2), 'MAIN MENU', font)
        expanded_easy_button = easy_button.inflate(130, 130)
        expanded_medium_button = medium_button.inflate(130, 130)
        expanded_hard_button = hard_button.inflate(130, 130)
        expanded_main_menu_button = main_menu_button.inflate(130, 130)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if expanded_easy_button.collidepoint(pygame.mouse.get_pos()):
                    return True, (20, 20), 'easy'
                elif expanded_medium_button.collidepoint(pygame.mouse.get_pos()):
                    return True, (40, 40), 'medium'
                elif expanded_hard_button.collidepoint(pygame.mouse.get_pos()):
                    return True, (100, 100), 'hard'
                elif expanded_main_menu_button.collidepoint(pygame.mouse.get_pos()):
                    Interface_Game_Start(screen, cfg, Username, Password)

        pygame.display.update()
        clock.tick(cfg.FPS)
def Interface_Load_Game(screen, cfg, Username, Password):
    pygame.display.set_mode(cfg.SCREENSIZE)
    font = pygame.font.SysFont('Consolas', 30)
    clock = pygame.time.Clock()
    user_data=load_users('Data_Users.pkl')
    running = True

    while running:
        screen.fill((29, 89, 98))
        BackGround = Background('resources/images/tamvagiahuy.png', [0, 0])
        screen.blit(BackGround.image, BackGround.rect)
        main_menu_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//3), 'MAIN MENU', font)
        expanded_main_menu_button = main_menu_button.inflate(130, 130)
        Pass = Password
        showText(screen, font, f'USERNAME: {Username}', (0, 0, 0), ((cfg.SCREENSIZE[0]-1000)//2, cfg.SCREENSIZE[1]//2.5))
        # Display numbers 1 to 7 as text
        play_buttons=[]
        exit_buttons=[]
        for i in range(1, 8):
            showText(screen, font, str(i)+'.', (0, 0, 0), ((cfg.SCREENSIZE[0]-1000)//2, cfg.SCREENSIZE[1]//2.5 + i*50))
            maze_data = user_data[f'{Username}']['mazes'][i-1]['maze']
            if maze_data is not None:
                maze_now = maze_data['maze_now']
                maze_solver = maze_data['maze_solver']
                hero_now = maze_data['hero_now']
                num_steps = maze_data['num_steps']
                time = maze_data['time']
                formatted_time = "{:.2f}".format(maze_data['time'])
                Difficulty = maze_data['Difficulty']
                showText(screen, font, f'Used Steps: {num_steps}, Time:{formatted_time}s, Difficulty: {Difficulty}', (0, 0, 0), ((cfg.SCREENSIZE[0]-1000)//2+30, cfg.SCREENSIZE[1]//2.5 + i*50))
                play_buttons.append(HalfButton(screen, ((cfg.SCREENSIZE[0]+600)//2, cfg.SCREENSIZE[1]//2.6 + i*50), 'PLAY', font))
                exit_buttons.append(HalfButton(screen, ((cfg.SCREENSIZE[0]+600)//2+150, cfg.SCREENSIZE[1]//2.6 + i*50), 'DEL', font))
            else:
                showText(screen, font, 'No maze data', (0, 0, 0), ((cfg.SCREENSIZE[0]-1000)//2+30, cfg.SCREENSIZE[1]//2.5 + i*50))
                play_buttons.append(HalfButton(screen, ((cfg.SCREENSIZE[0]+600)//2, cfg.SCREENSIZE[1]//2.6 + i*50), 'PLAY', font))
                exit_buttons.append(HalfButton(screen, ((cfg.SCREENSIZE[0]+600)//2+150, cfg.SCREENSIZE[1]//2.6 + i*50), 'DEL', font))
            
            # Display the username as text
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, button in enumerate(play_buttons):
                    expanded_button = button.inflate(50, 40)
                    if expanded_button.collidepoint(pygame.mouse.get_pos()):
                        return True, user_data[f'{Username}']['mazes'][i]['maze']['maze_now'], user_data[f'{Username}']['mazes'][i]['maze']['maze_solver'], user_data[f'{Username}']['mazes'][i]['maze']['hero_now'], user_data[f'{Username}']['mazes'][i]['maze']['num_steps'], user_data[f'{Username}']['mazes'][i]['maze']['time'],user_data[f'{Username}']['mazes'][i]['maze']['Difficulty']

                for j, button in enumerate(exit_buttons):
                    expanded_button = button.inflate(50, 40)
                    if expanded_button.collidepoint(pygame.mouse.get_pos()):
                        print(f"Before update: {user_data[f'{Username}']['mazes'][j]['maze']}")
                        user_data[f'{Username}']['mazes'][j]['maze'] = None
                        print(f"After update: {user_data[f'{Username}']['mazes'][j]['maze']}")
                        update_pickle_file(user_data, 'Data_Users.pkl')
                        pygame.display.update()
                        clock.tick(cfg.FPS)
                if expanded_main_menu_button.collidepoint(pygame.mouse.get_pos()):
                    return False, None, None, None, None, None, None
                    

        pygame.display.update()
        clock.tick(cfg.FPS)
def Interface_Game_Play(screen, cfg, font, clock, maze_now, maze_solver, hero_now, draw_solution, num_steps, start_time, num_levels, best_scores, Difficulty_Level, BLOCKSIZE, oak_wood_color, Username, Password):
    if start_time is None:
        start_time = time.time()
    else: 
        start_time = time.time() - start_time
    # Some thing to switching 
    Auto_Off = True
    A_On = True
    Customize_Off = True
    click_count = 0
    def move_hero(solution):
        for point in solution:
            if Auto_Off: 
                break
            hero_now.coordinate = list(point.coordinate)
            pygame.time.wait(300)
            pygame.display.update()
    saving = None
    while True:
        dt = clock.tick(cfg.FPS)
        screen.fill(oak_wood_color)
        is_move = False
        if A_On:
            solution = maze_solver.a_star_search(maze_now.blocks_list[hero_now.coordinate[1]][hero_now.coordinate[0]])
        else: 
            solution = maze_solver.bfs_search(maze_now.blocks_list[hero_now.coordinate[1]][hero_now.coordinate[0]])
        hero_now.draw(screen)
        maze_now.draw(screen)
        estimated_steps = len(solution)
        # ---Show some info
        showText(screen, font, 'LEVEL DONE: %d' % num_levels, (242, 197, 40), (10, 10))
        showText(screen, font, 'BEST SCORE: %s' % best_scores, (242, 197, 40), (210, 10))
        showText(screen, font, 'USED STEPS: %s' % num_steps, (242, 197, 40), (410, 10))
        showText(screen, font, 'ESTIMATED STEPS: %s' % estimated_steps, (242, 197, 40), (610, 10))
        # End the timer and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        showText(screen, font, 'TIME: %d:%02d' % (minutes, seconds), (242, 197, 40), (810, 10))
        #Content box
        Playing_Mode = ['Manual', 'Auto']
        Pathfinding_Algorithm = ['A*', 'BFS']
        Customize_Mode = ['Enable', 'Disable']   
        Content_Box = Box(screen, 0, 50, 250, 600, (192, 192, 192), (0,255,0), 3)
        Content_Box.draw()
        showText(screen, font, f'PLAYING MODE: {Playing_Mode[0] if Auto_Off else Playing_Mode[1]}', (0, 0, 0), (10, 60))
        showText(screen, font, f'PATHFINDING ALGORITHM: {Pathfinding_Algorithm[0] if A_On else Pathfinding_Algorithm[1]}', (0, 0, 0), (10, 110))
        showText(screen, font, f'CUSTOMIZE: {Customize_Mode[1] if Customize_Off else Customize_Mode[0]}', (0, 0, 0), (10, 160))
        display_resized_image(screen, 'resources/images/jerry.png', (maze_solver.end.coordinate[0] * BLOCKSIZE + cfg.BORDERSIZE[0], maze_solver.end.coordinate[1] * BLOCKSIZE + cfg.BORDERSIZE[1] + 17), BLOCKSIZE)
        if saving:
            showText(screen, font, 'SAVED SUCCESSFULLY!', (0, 0, 0), (10, 260))    
        elif saving == False:
            showText(screen, font, 'FAILED TO SAVE! Please delete a maze before saving a new one.', (0, 0, 0), (10, 260))
        # Start and end signs
        key_to_direction = {
            pygame.K_UP: 'up',
            pygame.K_DOWN: 'down',
            pygame.K_LEFT: 'left',
            pygame.K_RIGHT: 'right',
        }
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                mods = pygame.key.get_mods()
                if event.key in key_to_direction and Auto_Off:
                    direction = key_to_direction[event.key]
                    is_move = hero_now.move(direction, maze_now)
                elif event.key == pygame.K_ESCAPE:
                    pass
                elif event.key == pygame.K_1:
                    Auto_Off = not Auto_Off
                    if Auto_Off == False:
                        threading.Thread(target=move_hero, args=(solution,)).start()
                elif event.key == pygame.K_2:   
                    A_On = not A_On
                elif event.key == pygame.K_3:
                    Customize_Off = not Customize_Off
                elif event.key == pygame.K_r:
                    hero_now.coordinate[0] = maze_solver.end.coordinate[0]
                    hero_now.coordinate[1] = maze_solver.end.coordinate[1]
                elif event.key == pygame.K_SPACE:
                    draw_solution = True
                elif event.key == pygame.K_BACKSPACE:
                    draw_solution = False
                elif mods & pygame.KMOD_CTRL and keys[pygame.K_s]:
                    saving = save_users(Username, Password, 'Data_Users.pkl', {'maze_now': maze_now, 'maze_solver': maze_solver, 'hero_now': hero_now, 'num_steps': num_steps, "time": elapsed_time,"Difficulty": Difficulty_Level})
                    
                if is_move:
                    num_steps += 1    
            elif event.type == pygame.MOUSEBUTTONDOWN and Customize_Off == False:
                # maze_solver.start.coordinate = None
                # maze_solver.end.coordinate = None
                pos = pygame.mouse.get_pos()  # Get the position of the mouse click
                grid_pos = ((pos[0] - cfg.BORDERSIZE[0]) // BLOCKSIZE, (pos[1] - cfg.BORDERSIZE[1]) // BLOCKSIZE)
                if click_count == 0 and grid_pos[1] == 0:
                    if maze_solver.start is not None:  # If a start point already exists
                        maze_solver.start.has_walls[0] = True  # Reset the has_walls attribute
                    maze_solver.START(grid_pos)
                    hero_now.coordinate = list(grid_pos)
                    click_count += 1
                elif click_count == 1 and grid_pos[1] == maze_solver.maze_size[1] - 1:
                    if maze_solver.end is not None:  # If an end point already exists
                        maze_solver.end.has_walls[1] = True  # Reset the has_walls attribute
                    maze_solver.END(grid_pos)
                    click_count += 1
                else:
                    click_count = 0                 
        # ----↑↓←→Control hero
        
        if draw_solution and solution != False:
            current = maze_solver.end
            while current in solution:
                prev = current
                current = solution[current]
                pygame.draw.line(screen, (0, 255, 0), 
                                (prev.coordinate[0]*BLOCKSIZE + cfg.BORDERSIZE[0] + BLOCKSIZE//2, prev.coordinate[1]*BLOCKSIZE + cfg.BORDERSIZE[1] + BLOCKSIZE//2), 
                                (current.coordinate[0]*BLOCKSIZE + cfg.BORDERSIZE[0] + BLOCKSIZE//2, current.coordinate[1]*BLOCKSIZE + cfg.BORDERSIZE[1] + BLOCKSIZE//2), 
                                BLOCKSIZE//4)
        if (hero_now.coordinate[0] == maze_solver.end.coordinate[0]) and (hero_now.coordinate[1] == maze_solver.end.coordinate[1]):
            save_to_leaderboard(Difficulty_Level, Username, num_steps, elapsed_time)
            break
        pygame.display.update()
def Interface(screen, cfg, Username, Password):
    Game_Start = Interface_Game_Start(screen, cfg, Username, Password)
    if Game_Start == 'Difficulty':
        _,MAZESIZE,Difficulty_Level = Interface_Difficulty(screen, cfg, Username, Password) 
        BLOCKSIZE = 600//MAZESIZE[0]
        maze_now = RandomMaze(MAZESIZE, BLOCKSIZE, cfg.BORDERSIZE)
        # --Generate maze solver
        maze_solver = Maze_solver(maze_now, screen)
        # --Generate hero
        hero_now = Hero(cfg.HEROPICPATH, list(maze_solver.start.coordinate), BLOCKSIZE, cfg.BORDERSIZE)
        # --Statistics steps
        num_steps = 0
        return MAZESIZE, BLOCKSIZE, maze_now, maze_solver, hero_now, num_steps, None, Difficulty_Level
    elif Game_Start == 'Leaderboard':
        _, maze_now, maze_solver, hero_now, num_steps, time, Difficulty_Level = Interface_Leaderboard(screen, cfg)
        if _== False:
            return Interface(screen, cfg, Username, Password)
    elif Game_Start == 'Load_Game':
        _, maze_now, maze_solver, hero_now, num_steps, time, Difficulty_Level = Interface_Load_Game(screen, cfg, Username, Password)
        if _== False:
            return Interface(screen, cfg, Username, Password)
        elif _ == True: 
            if Difficulty_Level == 'easy':
                MAZESIZE = (20,20)
                BLOCKSIZE = 600//MAZESIZE[0]
            elif Difficulty_Level == 'medium':
                MAZESIZE = (40,40)
                BLOCKSIZE = 600//MAZESIZE[0]
            elif Difficulty_Level == 'hard':
                MAZESIZE = (100,100)	
                BLOCKSIZE = 600//MAZESIZE[0]
            return MAZESIZE, BLOCKSIZE, maze_now, maze_solver, hero_now, num_steps, time, Difficulty_Level 

def Interface_Leaderboard(screen, cfg):
    leaderboard_data = load_leaderboard()

    font = pygame.font.SysFont('Consolas', 30)
    screen.fill(oak_wood_color)
    BackGround = Background('resources/images/tamvagiahuy.png', [0, 0])
    screen.blit(BackGround.image, BackGround.rect)
    # Create a box
    Leaderboard_Box = Box(screen, 200, 50, 800, 700, (192, 192, 0), (0,255,0), 3)
    # Create buttons  
    main_menu_button = Button(screen, ((cfg.SCREENSIZE[0]-200)//2, cfg.SCREENSIZE[1]//2), 'MAIN MENU', font)
    expanded_main_menu_button = main_menu_button.inflate(130, 130)
    easy_button = HalfButton(screen, (300, 15), 'EASY', font)
    medium_button = HalfButton(screen, (500, 15), 'MED', font)
    hard_button = HalfButton(screen, (700, 15), 'HARD', font)
    left_button = HalfButton(screen, (300, 750), 'LEFT', font)
    right_button = HalfButton(screen, (950, 750), 'RIGHT', font)    
    expanded_easy_button = easy_button.inflate(50, 40)
    expanded_medium_button = medium_button.inflate(50, 40)
    expanded_hard_button = hard_button.inflate(50, 40)
    expanded_left_button = left_button.inflate(50, 40)
    expanded_right_button = right_button.inflate(50, 40)
    selected_difficulty = 'easy'
    Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao = 0
    while True:
        for event in pygame.event.get():
            Leaderboard_Box.draw()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(-1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if expanded_main_menu_button.collidepoint(event.pos):
                    return False, None, None, None, None, None, None
                elif expanded_easy_button.collidepoint(event.pos):
                    selected_difficulty = 'easy'
                    Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao = 0
                elif expanded_medium_button.collidepoint(event.pos):
                    selected_difficulty = 'medium'
                    Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao = 0
                elif expanded_hard_button.collidepoint(event.pos):
                    selected_difficulty = 'hard'
                    Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao = 0
                elif expanded_left_button.collidepoint(event.pos):
                    if Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao > 0:
                        Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao -= 10
                elif expanded_right_button.collidepoint(event.pos):
                    if len(leaderboard_data[selected_difficulty]) > Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao + 10:
                        Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao += 10
            # Draw the leaderboard for the selected difficulty
        if selected_difficulty is not None:
            for i, player_data in enumerate(leaderboard_data[selected_difficulty][Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao:Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao+10]):
                # print(f"Rank {i+1}: Player {player_data['Players']}, Steps {player_data['used_steps']}, Time {player_data['time']}")
                if selected_difficulty is not None:
                    formatted_time = "{:.2f}".format(player_data['time'])
                    showText(screen, font, f"{i+Oh_Wow_Anh_Ta_Tim_Toi_Toi_Sao+1}. Player: {player_data['Players']}, Steps: {player_data['used_steps']}, Time: {formatted_time} s", (255, 0, 0), (300, 100 + i*50))
        pygame.display.update()
