import logging
import pickle
import copy
from modules.Textbox import *

def save_users(username, password, filename, maze_data=None):
    try:
        with open(filename, 'rb') as f:
            users = pickle.load(f)
    except (EOFError, FileNotFoundError):
        users = {}

    # Create a deep copy of the users dictionary to preserve original data
    updated_users = copy.deepcopy(users)

    if username in updated_users:
        user_info = updated_users[username]
    else:
        user_info = {'password': password, 'mazes': [{'number': i+1, 'maze': None} for i in range(7)]}

    if maze_data is not None:
        for maze in user_info['mazes']:
            if maze['maze'] is None:
                maze['maze'] = {
                    'maze_now': maze_data['maze_now'],
                    'maze_solver': maze_data['maze_solver'],
                    'hero_now': maze_data['hero_now'],
                    'num_steps': maze_data['num_steps'],
                    'Difficulty': maze_data['Difficulty'],
                }
                break

    updated_users[username] = user_info

    try:
        with open(filename, 'wb') as f:
            pickle.dump(updated_users, f)
    except Exception as e:
        logging.error(f"An error occurred while saving users: {str(e)}")
        return False

    return True

def load_users(filename, Username = None):
    try:
        with open(filename, 'rb') as f:
            users = pickle.load(f)
    except (EOFError, FileNotFoundError):
        return []
    if Username is not None:
        # Get the first (and probably only) key in the selected_user dictionary
        key = list(users[Username].keys())[1]
        user_info = users.get(key, {})
        return user_info.get('mazes', [])
    return users




