import subprocess
import sys
import unittest
from pathlib import Path


class ScenarioCardLintCliTest(unittest.TestCase):
    def test_sample_runs(self):
        root = Path(__file__).resolve().parents[1]
        script = root / "scenario_card_lint.py"
        sample = root / "sample_input.json"
        result = subprocess.run([sys.executable, str(script), str(sample)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertIn("DISCUSSION_READY", result.stdout)
        self.assertIn("not certification", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
