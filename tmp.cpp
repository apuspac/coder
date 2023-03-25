template <classT>
classNode
{
public:
    T value;
    Node<T> *next;
    Node<T> *prev;

public:
    Node(T v) : value(v), next(nullptr), prev(nullptr) {}
};
template <classT>
classLinkedList
{
private: /***storesthefirstNodein"dummy->next",*andthelastNodein"dummy->prev".*/
    Node<T> *dummy;

public:
    LinkedList<T>() : dummy(newNode<T>(T())) {}
    T Head() const { returndummy->next->value; }
    T Last() const { returndummy->prev->value; }
};
*6bidirectional linked list = 双方向連結リスト
