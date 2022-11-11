import sys

from stimpl.robustness import run_stimpl_robustness_tests
from stimpl.runtime import EmptyState, State
from stimpl.test import run_stimpl_sanity_tests
from stimpl.types import Boolean, Integer


def state_test():
    state = EmptyState()
    if None != state.get_value("x"):
        print("Failure A!")
        sys.exit(-1)

    state2 = state.set_value("x", 5, Integer())
    if (5, Integer()) != state2.get_value("x"):
        print("Failure B!")
        sys.exit(-1)

    state3 = state2.set_value("k", True, Boolean())
    if (True, Boolean()) != state3.get_value("k"):
        print("Failure C!")
        sys.exit(-1)

    state4 = state3.set_value("x", 7, Integer())
    if (7, Integer()) != state4.get_value("x"):
        print("Failure D!")
        sys.exit(-1)

    if (5, Integer()) != state2.get_value("x"):
        print("Failure E!")
        sys.exit(-1)

    print("Success.")

if __name__ == '__main__':
    # state_test() 
    run_stimpl_sanity_tests()
    run_stimpl_robustness_tests()
