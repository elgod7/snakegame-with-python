import cProfile
import pstats
from main import main  # Import the module that contains your main function

if __name__ == '__main__':
    # Profiling the main function
    cProfile.run('main()', 'snake_game_profile')

    # Analyzing the profile results
    stats = pstats.Stats('snake_game_profile')
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()