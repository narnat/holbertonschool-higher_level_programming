#include "lists.h"

/**
 * print_dlistint - prints doubly linked list
 * @h: doubly linked list
 * Return: Size of linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t c = 0;

	while (h)
	{
		c++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (c);
}
