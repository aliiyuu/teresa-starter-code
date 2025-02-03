import subprocess
import signal
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--iterations", help="Number of iterations to run the interface for", type=int)
args = parser.parse_args()
if args.iterations:
   iterations = args.iterations
else:
    iterations = 500

# Start both scripts
processes = [
    subprocess.Popen(["python3", "interface.py", f"{iterations}"]),
    subprocess.Popen(["python3", "sim.py"]),
]


def terminate_processes(signal_received, frame):
    print("\nTerminating both scripts...")
    for process in processes:
        process.terminate()
    sys.exit(0)


# Handle CTRL+C
signal.signal(signal.SIGINT, terminate_processes)

# Wait for both scripts
for process in processes:
    process.wait()
