import os
import sys
import pdb
import subprocess

class Debugger(pdb.Pdb):
    def __init__(self, filepath):
        self.process = subprocess.Popen(
        ["python", "-m", 'pdb', filepath],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
    )
        sys.argv = [filepath]
        sys.path.append(os.path.dirname(filepath))

        super().__init__()

    def execute_debug_cmd(self, command):
        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()
        # mimic standard pdb shell interaction

        output = self.process.stdout.readline()

        return output