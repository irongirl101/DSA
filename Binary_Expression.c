#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>  // for isdigit()
#include <string.h>

struct node {
    char data[10];
    struct node* left;
    struct node* right;
    struct node* next;
};
struct node *head=NULL;

struct node* newNode(char* data) {
    struct node* node = (struct node*)malloc(sizeof(struct node));
    strcpy(node->data,data);
    node->left = NULL;
    node->right = NULL;
    node->next = NULL;
    return node;
}

void push(struct node* x) {
    x->next = head;
    head = x;
}

struct node* pop() {
    struct node* p = head;
    head = head->next;
    return p;
}

void printInorder(struct node* node) {
    if (node == NULL) return;
    printInorder(node->left);
    printf("%s ", node->data);
    printInorder(node->right);
}

// Recursive evaluation
int eval(struct node* root) {
    // If it's a number (no children)
    if (root->left == NULL && root->right == NULL) {
        return atoi(root->data);   // convert string to int
    }

    int left_val = eval(root->left);
    int right_val = eval(root->right);

    if (strcmp(root->data, "+") == 0) return left_val + right_val;
    if (strcmp(root->data, "-") == 0) return left_val - right_val;
    if (strcmp(root->data, "*") == 0) return left_val * right_val;
    if (strcmp(root->data, "/") == 0) return left_val / right_val; 
    if (strcmp(root->data, "^") == 0) {
        int res = 1;
        for (int i = 0; i < right_val; i++) res *= left_val;
        return res;
    }

    return 0;
}

struct node* getSuccessor(struct node* curr) {
    curr = curr->right;
    while (curr != NULL && curr->left != NULL)
        curr = curr->left;
    return curr;
}
void deleteTree(struct node* root) {
    if (root == NULL) return;

    // Recursively delete children
    deleteTree(root->left);
    deleteTree(root->right);

    // Free current node
    free(root);
}
int main() {
    char expr[] = "3 7 19 * +";
    char* token = strtok(expr, " ");
    struct node *x, *y, *z;

    while (token != NULL) {
        if (strcmp(token, "+") == 0 || strcmp(token, "-") == 0 ||
            strcmp(token, "*") == 0 || strcmp(token, "/") == 0 ||
            strcmp(token, "^") == 0) {
            z = newNode(token);
            x = pop();
            y = pop();
            z->left = y;
            z->right = x;
            push(z);
        } else {
            z = newNode(token);
            push(z);
        }
        token = strtok(NULL, " ");
    }

    printf("Inorder Expression: ");
    printInorder(z);
    printf("\n");

    printf("Evaluated Value = %d\n", eval(z));

    return 0;
}