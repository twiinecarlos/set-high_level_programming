#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *second;
	listint_t *prev;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second = slow->next;
	prev = NULL;

	while (second != NULL)
	{
		temp = second->next;
		second->next = prev;
		prev = second;
		second = temp;
	}

	second = prev;
	temp = *head;

	while (second != NULL)
	{
		if (temp->n != second->n)
			return (0);

		temp = temp->next;
		second = second->next;
	}

	return (1);
}
