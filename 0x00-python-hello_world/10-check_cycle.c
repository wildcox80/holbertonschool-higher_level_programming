#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: singly linked list to check
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;

	if (list == NULL)
		return (0);

	ptr1 = list;
	ptr2 = list;
	while (ptr2->next != NULL)
	{
		if (ptr2->next->next == NULL)
			return (0);
		ptr2 = ptr2->next->next;
		ptr1 = ptr1->next;
		if (ptr2 == ptr1)
			return (1);
	}
	return (0);
}

