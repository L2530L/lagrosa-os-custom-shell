# Activity 1 – System Call Trace Analysis

## 1. Syscall Identification

The system call used for keyboard input was `read()`.

## 2. Fork Return Value

The parent process received `59443`, which is the child PID.

The child process received `0`.

## 3. Privilege Boundary

A Ring 3 program cannot directly create a process because it has limited privileges. It must request the kernel in Ring 0 through a system call. The kernel creates the process, then returns control to the program.
