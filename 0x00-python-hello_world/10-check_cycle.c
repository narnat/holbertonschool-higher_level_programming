#include "lists.h"

/**
 * check_cycle - checks if the linked list has a loop
 * @list: linked list
 * Return: 1 if it has a loop, 0 if there is no loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast->next->next && slow->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
