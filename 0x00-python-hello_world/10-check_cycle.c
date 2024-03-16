#include "lists.h"

/**
 *check_cycle - checks if there is a linked cycle
 *@list: list to be checked
 *Return: 0 for success
 *
 *The "tortoise and hare" technique
 */

int check_cycle(listint_t *list)
{  
	struct listint_s *slow = list;
	struct listint_s *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
