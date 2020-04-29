#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: number to add
 *
 * Return: address of new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp_slow;
	listint_t *tmp_fast;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	tmp_fast = NULL;
	for (tmp_slow = *head; tmp_slow != NULL && tmp_slow->n < number; )
	{
		tmp_fast = tmp_slow;
		tmp_slow = tmp_slow->next;
	}
	new->next = tmp_slow;
	if (tmp_fast != NULL)
		tmp_fast->next = new;
	else
		*head = new;

	return (new);
}

