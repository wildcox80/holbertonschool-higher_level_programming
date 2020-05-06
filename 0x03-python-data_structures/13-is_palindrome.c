#include "lists.h"

/**
 * is_palindrome - calls helper to check if a singly linked list
 *                 is a palindrome
 * @head: head of listint_t linked list
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	return (_helper(head, *head));
}

/**
 * _helper - checks if a singly linked list is a palindrome
 * @head: head of listint_t linked list
 * @end: pointer to end of palindrome
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int _helper(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (_helper(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
