import os
import sys
import pdb
import subprocess
import time
import html

class Debugger(pdb.Pdb):
    def __init__(self, filepath):

        self.output_file = open("output.txt", "r+")

        self.process = subprocess.Popen(
        ["python", "-m", 'pdb', filepath],
        stdin=subprocess.PIPE,
        stdout=self.output_file,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
        bufsize=1
        )

        sys.argv = [filepath]
        sys.path.append(os.path.dirname(filepath))

        super().__init__()

    def execute_debug_cmd(self, command):
        self.output_file.truncate(0)
        # Empty the output file, this is really just preference for output
        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()
        # mimic standard pdb shell interaction

        time.sleep(0.2)

        self.output_file.flush()

        self.output_file.seek(0)
        output = self.output_file.readlines()

        output = [html.escape(out.lstrip("\x00")) for out in output]

        output = ("".join(output)).replace("(Pdb)", "")

        return output