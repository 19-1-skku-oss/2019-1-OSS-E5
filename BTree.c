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

BTreeNode* createNode(bool _leaf)
{
	BTreeNode* newNode = (BTreeNode*)malloc(sizeof(BTreeNode));
	int i;

	newNode->leaf = _leaf;

	newNode->keys = (int*)malloc(sizeof(int)*(degree+1));
	newNode->C = (BTreeNode**)malloc(sizeof(BTreeNode*)*(degree+2));
	
	for(i=0; i<degree+2; i++)
		newNode->C[i] = NULL;
	
	newNode->n = 0;
	newNode->P = NULL;
	
	return newNode;
}

void traverse(BTreeNode* present)
{
	if (root != NULL)
	{
		int i;
		for(i=0; i<present->n; i++)
		{
			if (present->leaf == false)
				traverse(present->C[i]);
			printf(" ");
			printf("%d", present->keys[i]);
		}
		
		if (present->leaf == false)
			traverse(present-C[i]);
	}
}

BTreeNode* search(int k)
{
	return (root==NULL)?NULL:_search(root, k);
}

BTreeNode* _search(BTreeNode* present, int k)
{
	int i=0;
	while(i<present->n && k > present->keys[i])
		i++;

	if(present->keys[i] == k)
		return present;

	if(present->leaf == true)
		return NULL;

	return _search(present->C[i], k);
}

void insertElement(int k)
{
	if (search(k) != NULL)
	{
		printf("The tree already has %d \n", k);
		return;
	}

	if (root == NULL)
	{
		root = createNode(true);
		root->P = NULL;
		root->keys[0] = k;
		root->n = 1;
	}
	else
		_insert(root, k);
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
