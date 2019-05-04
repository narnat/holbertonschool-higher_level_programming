#include "lists.h"

/**
 * dlistint_len - returns the length of a doubly linked list
 * @h: doubly linked list
 * Return: Number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t c = 0;

	while (h)
	{
		c++;
		h = h->next;
	}
	return (c);
}
