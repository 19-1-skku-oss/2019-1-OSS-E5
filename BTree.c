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

void _insert(BTreeNode *present, int k)
{
	int i=present->n;
	
	if(present->leaf == true)
	{
		while(i>0 && (present->keys[i-1]) > k)
		{
			present->keys[i] = present->keys[i-1];
			i--;
		}
		present->keys[i] = k;
		(present->n)++;
		_balancing(present);
	}
	else
	{
		while(i>0 && (present->keys[i-1] > k))
		{
			i--;
		}
		
		_insert(present->C[i], k);
	}
}

void _balancing(BTreeNode* present)
{
	BTreeNode* parent;
	
	if (present->n <= t)
		return;

	else if (present->P == NULL)
	{
		root = _splitChild (present);
		return;
	}
	
	else
	{
		parent = _splitChild(present);
		_balancing(parent);
	}
}

BTreeNode* _splitChild(BTreeNode* present)
{
	int i;
	int splitIndex;
	int risingKey;
	int parentIndex;
	
	BTreeNode* currentParent;
	BTreeNode* left;
	BTreeNode* right = _createNode(present->leaf);
	
	splitIndex = t/2;

	right->n = present->n - splitIndex - 1;
	risingKey = present->keys[splitIndex];

	if(present->P != NULL)
	{
		currentParent = present->P;
		for(parentIndex = 0; parentIndex < currentParent->n + 1 && currentParent->C[parentIndex] != present; parentIndex++);
		for(i=currentParent->n; i > parentIndex; i--)
		{
			currentParent->C[i+1] = currentParent->C[i];
			currentParent->keys[i] = currentParent->keys[i-1];
		}
		currentParent->n = currentParent->n + 1;
		currentParent->keys[parentIndex] = risingKey;
		
		currentParent->C[parentIndex + 1] = right;
		right->P = currentParent;
	}
	
	for(i=splitIndex + 1; i<present->n + 1; i++)
	{
		right->C[i - spliIndex - 1] = present->C[i];
		if (present->C[i] != NULL)
		{
			right->leaf = false;
			
			if(present->C[i] != NULL)
			{
				present->C[i]->P = right;
			}
			present->C[i] = NULL;
		}
	}

	for(i=splitIndex + 1; i < present->n; i++)
		right->keys[i - splitIndex - 1] = present->keys[i];
	
	left = present;
	left->n = splitIndex;

	if (present->P != NULL)
		return present->P;
	else
	{
		root = _createNode(present->leaf);
		root->keys[0] = risingKey;
		root->n = 1;
		root->C[0] = left;
		root->C[1] = right;
		left->P = root;
		right->P = root;
		root->leaf = false;
		return root;
	}
}


void removeElement(int k)
{
	if(!root)
	{
		printf("The tree is empty\n");
		return;
	}

	_remove(root, k);

	if (root->n == 0)
	{
		BTreeNode *tmp = root;
		if(root->leaf)
			root = NULL;
		else
		{
			root = root->C[0];
			root->P = NULL;
		}
		free(tmp);
	}
	return;
}


void _remove(BTreeNode* present, int k)
{
	BTreeNode* del_node = search(k)
	if(del_node == NULL)
	{
		printf("%d is not exist\n", k);
		return;
	}

	int child_num = del_node->n;
	int i = del_node->n;
	i--;
	int temp = del_node->keys[i];
	if(del_node->leaf)
	{
		while(i>0 && temp != k)
		{
			del_node->keys[i-1] = temp;
			temp = del_node->keys[i-1];
			i--;
		}
		(del_node->n)--;
		_balancingAfterDel(del_node);
	}
	

	else
	{
		while(i>0 && temp!=k)
			i--;
		del_node->keys[i] = del_node->C[i]->keys[del_node->C[i]->n-1];
		(del_node->C[i]->n)--;
		_balancingAfterDel(del_node->C[i]);
	}
	
	return;
}

void _balancingAfterDel(BTreeNode* present)
{
	int minKeys = (degree+2)/2 - 1;
	BTreeNode* parent;
	BTreeNode* next;
	int parentIndex = 0;
	
	if(present->n < minKeys)
	{	
		if(present->P == NULL)
		{
			if(present->n == 0)
			{
				root = present->C[0];
				if(root !=NULL)
					root->P = NULL;
			}
		}
		else
		{
			parent = present->P;
			for(parentIndex=0; parent->C[parentIndex] != present; parentIndex++);
			if(parentIndex>0 && parent->C[parentIndex-1]->n > minKeys)
			{
				_borrowFromLeft(present, parentIndex);
			}
			else if(parentIndex < parent->n && parent->C[parentIndex+1]->n > minKeys)
			{
				_borrowFromRight(present, parentIndex);
			}
			else if(parentIndex==0)
			{
				next = _merge(present);
				_balancingAfterDel(next->P);
			}
		}
	}
}

void _borrowFromRight(BTreeNode* present, int parentIdx)
{
	int i;
	BTreeNode* rightSib;
	BTreeNode* parentNode = present->P;

	rightSib = parentNode->C[parentIdx + 1];
	present->n++;
	
	present->keys[present->n - 1] = parentNode->keys[parentIdx];
	parentNode->keys[parentIdx] = rightSib->keys[0];

	if(!present->leaf)
	{
		present->C[present->n] = rightSib->C[0];
		presnet->C[present->n]->P = present;

		for(i=1; i<rightSib->n + 1; i++)
			rightSib->C[i-1] = rightSib->C[i];
	}
	
	for(i=1; i<rightSib->n; i++)
		rightSib->keys[i-1] = rightSib->keys[i];
	
	rightSib->n--;
}

void _borrowFromLeft(BTreeNode* present, int parentIdx)
{
	int i;
	BTreeNode* leftSib;
	BTreeNode* parentNode = present->P;
	present->n = present->n + 1;

	for(i=present->n -1; i>0; i--)
		present->keys[i] = present->C[i-1];
	leftSib = parentNode->C[parentIdx-1];

	if(!present->leaf)
	{
		for(i=present->n; i>0; i--)
			present->C[i] = present->C[i-1];
	
		present->C[0] = leftSib->C[leftSib->n];
		leftSib->C[leftSib->n] = NULL;
		present->C[0]->P = present;
	}

	present->keys[0] = parentNode->keys[parentIdx - 1];
	parentNode->keys[parentIdx-1] = leftSib->keys[leftSib->n -1];
	
	leftSib->n = leftSib->n - 1;
}

BTreeNode* _merge(BTreeNode* present)
{
	BTreeNode* parentNode = present->P;
	int parentIndex = 0;
	int fromParentIndex;
	int i;
	
	for(parentIndex = 0; parentNode->C[parentIndex] != present; parentIndex++);
	BTreeNode* rightSib = parentNode->C[parentIndex+1];

	present->keys[present->n] = parentNode->keys[parentIndex];
	fromParentIndex = present->n;
	
	for(i=0; i<rightSib->n;i++)
		present->keys[present->n +1 +i] = rightSib->keys[i];

	if(!present->leaf)
		for(i=0; i<=rightSib->n; i++)
		{
			present->C[present->n +1+i] = rightSib->C[i];
			present->C[present->n +1+i]->P = present;
		}
	
	for(i=parentIndex+1; i<parentNode->n; i++)
	{
		parentNode->C[i] = parentNode->C[i+1];
		parentNode->keys[i-1] = parentNode->keys[i];
	}
	parentNode->n--;
	present->n = present->n + rightSib->n + 1;
	return present;
}

int _getLevel(BTreeNode* present)
{
	int i;
	int maxLevel = 0;
	int temp;
	if(present==NULL)
		return maxLevel;
	if(present->leaf == ture)
		return maxLevel++;
	
	for(i=0; i<present->n+1; i++)
	{
		temp = _getLevel(present->C[i]);
		
		if(temp>maxLevel)
			maxLevel = temp;
	}
	
	return maxLevel + 1;
}

void _getNumberOfNodes(BTreeNode* present, int* numNodes, int level)
{
	int i;
	if(present==NULL)
		return;
	
	if(present->leaf==false)
	{
		for(i=0; i<present->n+1; i++)
			_getNumberOfNodes(present->C[i], numNodes, level + 1);
	}
	numNodes[level] += 1;
}

void _mappingNodes(BTreeNode* present, BTreeNode ***nodePtr, int* numNodes, int level)
{
	int i;
	if(present==NULL)
		return;
	
	if(present->leaf == false)
	{
		for(i=0; i<present->n+1; i++)
			_mappingNodes(present->C[i], nodePtr, numNodes, level+1);
	}

	nodePtr[level][numNodes[level]] = present;
	numNodes[level] += 1;
}

void printTree()
{
	int level;
	int* numNodes;
	int i,j,k;

	level = _getLevel(root);
	numNodes = (int*) malloc(sizeof(int)* level);
	memset(numNodes, 0,0 level*sizeof(int));
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
