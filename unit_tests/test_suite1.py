import unittest

import sort_test
import intersect_test

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(sort_test)
suite.addTests(loader.loadTestsFromModule(intersect_test))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)