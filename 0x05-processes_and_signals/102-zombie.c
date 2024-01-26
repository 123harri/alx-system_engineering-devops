#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Create 5 zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else if (child_pid < 0)
		{
			perror("Fork failed");
			exit(1);
		}
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
