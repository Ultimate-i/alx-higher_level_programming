#include "lists.h"

/**
 * insert_node - inserts a number in a sorted singly linked list.
 * @head: double pointer to the first element in the singly linked list.
 * @number: number to add in the linked list.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *new_node = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	node = *head;
	while (node != NULL)
	{
		if (node->n <= number && (node->next == NULL || node->next->n > number))
		{
			new_node->next = node->next;
			node->next = new_node;
			break;
		}
		node = node->next;
	}
	return (new_node);
}
