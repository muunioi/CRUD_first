CRUD_first
================

> 1. pk 가능 목록 : ID, 전화번호, 이메일
> 2. pk 불가능 목록 : 라이언, 이름, 학번, 학과/학부

markdown 문법 연습하기
===============

this is a normal paragraph:
~~~
this is a code block
~~~
end code block

'textarea' 일반 

```
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
```

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#ifdef _MSC_VER
#pragma warning(disable: 4996)
#endif

typedef struct _node_t {
	int data;
	struct _node_t* left;
	struct _node_t* right;
}node_t;

node_t* create_node(int data) {
	node_t* node = (node_t*)malloc(sizeof(node_t));
	node->data = data;
	node->left = node->right = NULL;

	return node;
}

```
