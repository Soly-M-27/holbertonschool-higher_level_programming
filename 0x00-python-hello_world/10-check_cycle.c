#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: List
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first_node = list, *check_next_node = list;

	while (first_node && check_next_node && check_next_node->next)
	{
		first_node = first_node->next;
		check_next_node = check_next_node->next->next;
		if (first_node == check_next_node)
			return (1);
	}
	return (0);
}
