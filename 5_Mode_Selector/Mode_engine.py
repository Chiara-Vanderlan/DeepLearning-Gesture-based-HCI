import sys

sys.path.append('../2_Application_Actions')
from Orchestrator import orchestrator

def engine(argument, gestures):
    switcher = {
        1: default_function,
        2: orchestrator,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)


def default_function(gesture):
    print("Invalid action called!")