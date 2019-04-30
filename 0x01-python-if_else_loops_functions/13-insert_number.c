#include "lists.h"

/**
 * insert_node - inserts node
 * @head: linked list
 * @number: number to be inserted
 * Return: linked list if it succsessful
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newnode = NULL;

	if (!*head || temp->n > number)
	{
		newnode = malloc(sizeof(listint_t));
		if (!newnode)
			return (NULL);
		newnode->n = number;
		newnode->next = temp;
		*head = newnode;
	}
	while (temp)
	{
		if (temp->n < number && (!temp->next || temp->next->n > number))
		{
			newnode = malloc(sizeof(listint_t));
			if (!newnode)
				return (NULL);
			newnode->n = number;
			newnode->next = temp->next;
			temp->next = newnode;
		}
		temp = temp->next;
	}
	return (*head);
}
