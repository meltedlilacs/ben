#ifndef LIST_H
#define LIST_H

#include "node.h"

/**
 * The list class is a generic, extremely lightweight linked list. it should be used by overriding the node class and adding child objects using the add() method
 *
 * @tparam T the type of data to be stored in the list
 */
template <class T>
class List {
	public:
		/**
		 * Default constructor, simply initializes all variables
		 */
		List();
		/**
		 * adds the argument to the end of the list. object must be allocated on heap. takes over control of object, ie DO NOT DELETE OBJECT
		 *
		 * @param object the address of the object to be added to the list
		 */
		void add(Node<T>* object);
		/**
		 * the current length of the list
		 *
		 * @return the list length
		 */
		int length();
		/**
		 * accessor function to get the nth member of the list
		 *
		 * @param position the 0-indexed position of the wanted object
		 *
		 * @return pointer to object, or 0 if position to large or small
		 */
		Node<T>* get(int position);
		/**
		 * delete all elements in list
		 */
		~List();
	protected:
		Node<T>* first;
		int size;
	};

template <class T>
List<T>::List() {
	size = 0;
	first = 0;
	}
template <class T>
void List<T>::add(Node<T>* object) {
	if(length() == 0) {
		first = object;
		}
	else {
		get(length() - 1)->setNext(object);
		}
	size++;
	}
template <class T>
int List<T>::length() {
	return size;
	}
template <class T>
Node<T>* List<T>::get(int position) {
	if(position < length() && position >= 0) {
		Node<T>* returnValue = first;
		for(int i = 0; i < position; i++) {
			returnValue = returnValue->getNext();
			}
		return returnValue;
		}
	return 0;
	}
template <class T>
List<T>::~List() {
	Node<T>* nextValue = first;
	while(nextValue) {
		Node<T>* deleteThis = nextValue;
		nextValue = deleteThis->getNext();
		delete deleteThis;
		}
	}

#endif