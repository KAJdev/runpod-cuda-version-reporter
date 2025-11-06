import time
import runpod
import subprocess


def handler(job):
    """get CUDA version"""
    output = subprocess.check_output(["nvcc", "--version"]).decode("utf-8")
    print(output)
    return output.split("\n")[3]

runpod.serverless.start({"handler": handler})
