#include <stdio.h>
#include <string.h>

int degree;
typedef struct BTreeNode
{
	int *keys; // An array of keys
	struct BTreeNode *P; // An array of parent pointer
	struct BTreeNode **C; // An array of child pointers
	int n; // Current number of Keys
	bool leaf; // Is true when node is leaf
} BTreeNode;

void BTreeInit(int _degree)
{
	root = NULL;
	degree = _degree - 1;
}

int main()
{
	BTreeNode temp;
	int arr[3] = {1, 2, 3};
	temp.keys = arr;
	temp.leaf = False;
	temp.n = strlen(arr);
	return 0;
}
