import sys

from stimpl.robustness import run_stimpl_robustness_tests
from stimpl.runtime import EmptyState, State
from stimpl.test import run_stimpl_sanity_tests
from stimpl.test_state import test_state_implementation
from stimpl.types import Boolean, Integer

if __name__ == '__main__':
    # state_test() 
    test_state_implementation()
    run_stimpl_sanity_tests()
    run_stimpl_robustness_tests()
