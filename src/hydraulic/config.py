DATA_PATH = './data/'
DATA_OUTPUT_PATH = f"{DATA_PATH}outputs/"
SEPERATOR = '\t'
PROFILE_COLUMNS= ['cooler','valve', 'pump_lekage', 'accumulator', 'stable_flag']

FILES_NAMES = {
    'temperature': ['TS1', 'TS2', 'TS3', 'TS4'],
    'pressure': ['PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'PS6'],
    'motor_power': ['EPS1'],
    'volume_flow': ['FS1', 'FS2'],
    'vibration': ['VS1'],
    'cooling_efficiency': ['CE'],
    'cooling_power': ['CP'],
    'efficiency_factor': ['SE']
}

TARGET_FILE_NAME = 'profile.txt'

