"""
INDONESIA EARTHQUAKE DETECTION APPLICATION
I use function modularization
"""
import indomagnitude

if __name__ == '__main__':
    print('Main Application')
    result = indomagnitude.data_extc()
    indomagnitude.data_vis(result)
