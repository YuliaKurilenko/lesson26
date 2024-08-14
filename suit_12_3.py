import unittest
import homework31
runnerST = unittest.TestSuite
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework31.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(homework31.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)