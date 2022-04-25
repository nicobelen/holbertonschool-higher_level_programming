#include "lists.h"

/**
*
*
*
*
*/
int check_cycle(listint_t *list)
{
	int a = 0;

	listint_t *node1, *node2;

	node1 = node2 = list;

	while (node1 && node2 && node2->next && a == 0)
	{
		node1 = node1->next;
		node2 = node2->next->next;

		if (node1 == node2)
		{
			a = 1;
		}
	}
	return (a);
}
