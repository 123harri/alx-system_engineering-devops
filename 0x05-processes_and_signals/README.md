# Process Management and Zombie Creation

This repository contains Bash scripts and a C program for process management and creating zombie processes.

## Bash Scripts

### 1. Display PID Script

- **Filename:** `0-what-is-my-pid`
- **Description:** Bash script that displays its own PID.

### 2. List Processes Script

- **Filename:** `1-list_your_processes`
- **Description:** Bash script that displays a list of currently running processes.

### 3. Filter Processes Script

- **Filename:** `2-show_your_bash_pid`
- **Description:** Bash script that displays lines containing the word "bash."

### 4. PID and Process Name Script

- **Filename:** `3-show_your_bash_pid_made_easy`
- **Description:** Bash script that displays the PID along with the process name of processes containing the word "bash."

### 5. Infinite Loop Script

- **Filename:** `4-to_infinity_and_beyond`
- **Description:** Bash script that displays "To infinity and beyond" indefinitely with a sleep of 2 seconds between each iteration.

### 6. Stop Infinite Loop Script

- **Filename:** `5-dont_stop_me_now`
- **Description:** Bash script that stops the infinite loop process.

### 7. Stop Another Process Script

- **Filename:** `7-highlander`
- **Description:** Bash script that stops another process (e.g., "highlander") using signals.

### 8. Process Management Script

- **Filename:** `101-manage_my_process, manage_my_process`
- **Description:** Bash script that creates, stops, and restarts a process, managing its PID.

## C Program

### 9. Zombie Creation Program

- **Filename:** `zombie.c`
- **Description:** C program that creates 5 zombie processes and enters an infinite loop.

## How to Run

1. **Bash Scripts:**
    - Make scripts executable: `chmod +x script_name.sh`
    - Run: `./script_name.sh`

2. **C Program:**
    - Compile: `gcc zombie.c -o zombie`
    - Run: `./zombie`

## Author

- [Harriet Muwe]
