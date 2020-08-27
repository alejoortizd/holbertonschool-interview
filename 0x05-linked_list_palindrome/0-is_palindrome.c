#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - Entry Point
 * @head: Head of the list
 * Return: 1 if it is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int array[4352], i = 0, j = 0, mid;

	if (head == NULL || (tmp != NULL && tmp->next == NULL))
		return (1);

	while (tmp != NULL)
	{
		array[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	i--, mid = i / 2;
	while (i >= mid && j <= mid)
	{
		if (array[i] != array[j])
			return (0);
		i--, j++;
	}
	return (1);
}
