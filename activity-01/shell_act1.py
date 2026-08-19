import os
import sys


def main():
    while True:
        try:
            sys.stdout.write("py-sh> ")
            sys.stdout.flush()

            user_input = sys.stdin.readline()

            # Ctrl+D / EOF
            if user_input == "":
                print()
                break

            args = user_input.strip().split()

            # Empty input guard
            if not args:
                continue

            try:
                pid = os.fork()
            except OSError as error:
                print(f"Fork failed: {error}", file=sys.stderr)
                continue

            # Child process
            if pid == 0:
                print(
                    f"[CHILD] PID: {os.getpid()} | "
                    f"PPID: {os.getppid()} | "
                    f"Target: {args[0]}",
                    flush=True
                )

                os._exit(0)

            # Parent process
            elif pid > 0:
                print(
                    f"[PARENT] Spawned child with PID: {pid} | "
                    f"Shell PID: {os.getpid()}"
                )

            else:
                print("Error: fork failed.", file=sys.stderr)

        except KeyboardInterrupt:
            # Ctrl+C
            print()
            break


if __name__ == "__main__":
    main()