# Linked-List-in-Python

Contains the skeleton code to implement a simple linked list and a double linked list.

## Learning Objectives

After completing the tasks, you should know the following:

### Primary Learning Objectives (Python)

- Able to modify and run a Python module;
- Understand and implement a singly linked list; and
- Understand and implement a doubly linked list.

### Secondary Learning Objectives (Git)

- Able to make a fork (personal copy) of a git repository;
- Understand how to clone a repository to your local machine;
- Able to commit local changes (and understand when to commit and how to design meaningful commit messages); and
- Able to push local changes back to your repository.

## Tasks

### Task A (Git familiarisation)

The aim of task A is to familarise yourself with the git workflow. For part of this course you will be expected to complete an assignment (*30% of total grade*) which includes implementing algorithms using python and submitting a report containing theoretical and empirical analysis of your implementation. We will be using git to gauge your progress and to analyse your development process, and so good software engineering principles will be expected to be followed. The following tasks will teach you how to use the basics of git:

1. Fork the repository;
2. Clone the repository to your local machine;
3. Amend the files ```simple_linked_list.py``` and ```double_linked_list.py``` to include your student name/number;
4. Commit the changes with a descriptive commit message; and
5. Push the changes to your online repository.

Completing the above exercise will familiarise you with the git workflow, and allow you to see how the autograders etc work.

TODO: Add details for tasks below, e.g.

*(1) Fork the repository*

To fork a repository using github classroom...

### TASK B 

The Python file for the singly linked list (```simple_linked_list.py```) has most of the functionality implemented. Your task is to complete the implementation for the two ```remove``` methods. You are to code these methods for a singly linked list. You should not change the interface (types, method names, return types, parameters). Afterwards, open and examine the skeleton for a doubly linked list (```double_linked_list.py```). Implement the ```add```, ```insert```, two ```remove``` and the ```reversePrint``` methods. Finally, use the interactive interface of linked list demo to test your implementations. 

To test the singly linked list, type: ```python3 linked_list_demo.py single```

To test the doubly linked list, type: ```python3 linked_list_demo.py double```

*In a PDF Report, provide answers to the following questions*:

1. Which type of linked list is faster for printing the list in reverse (the ```reversePrint()``` method)?
2. For an unsorted doubly linked list, could you implement a faster search than the one provided? Describe what changes you would make.

## What is a Linked List?

Linked list is a basic type of data structure commonly used to implement abstract data types of collections, such as sequences and adjacency lists. As a data structure, it consists of a group of nodes, where each node stores an element of the collection (see *Figure 1a*, right figure). In addition, each node contains a reference to the next node in the list.

![image](https://github.com/RMIT-COSC2123-3119-AA25/Linked-List-in-Python/blob/main/img/Example%20of%20Linked%20List.png)

For example, in *Figure 1b*, we have a linked list representing a collection of two elements, ’A’ and ’P’. Node *A* is a node in the linked list that contains the data **A** and is pointing to node **P**. If a node is the only one or the last element in the list, as it has no “next” element, it can contain a **NULL** reference (not pointing to any other node). In *Figure 1a*, node **A** contains a **NULL** reference as it is the only node in the list. Typically, a list is accessed through a structure (e.g., structure *list_t* in left figure of *Figure 1a*). Usually, the list structure holds three types of information: 

1. the number of nodes in a list;
2. **HEAD** - the reference to the first node; and
3. **TAIL** - the reference to the last node.

In *Figure 1b*, **HEAD** is pointing to the first node **A** and **TAIL** is pointing to the last node **P**.

There are two main types of linked list implementations – singly linked list and doubly linked list. In singly linked list, each node has one pointer/reference to the next node in the list (see *Figure 2a*). In *Figure 2a*, the **HEAD** is pointing to the first node **A** and **TAIL** is pointing to the last node **M**. Singly linked list enables fast insertion (at head or tail). However, search can be slow as it may require traversing all the nodes from **HEAD** to **TAIL** in a singly link list.

In doubly linked list, each node has two pointers/references, one to the next node and the other to the previous node. In *figure (d)*, the node **D** has the reference to its next node **H** and the reference to its previous node **Q**. The doubly linked list uses more space (need to store the extra pointer/reference per node), but for some operations can be faster (which operations are for you to find out in this lab) – this is an example of space-time tradeoff.

![image](https://github.com/RMIT-COSC2123-3119-AA25/Linked-List-in-Python/blob/main/img/Example%20of%20Singly%20and%20Doubly%20Linked%20Lists.png)
