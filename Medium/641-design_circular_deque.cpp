class MyCircularDeque
{
public:
    int *queue;
    int front, rear, size, capacity;

    MyCircularDeque(int k)
    {
        queue = new int[k];
        capacity = k;
        front = -1;
        rear = -1;
        size = 0;
    }

    bool insertFront(int value)
    {
        if (isFull())
            return false;

        if (isEmpty())
        {
            front = rear = 0;
        }
        else
        {
            front = (front - 1 + capacity) % capacity;
        }
        queue[front] = value;
        size++;
        return true;
    }

    bool insertLast(int value)
    {
        if (isFull())
            return false;

        if (isEmpty())
        {
            front = rear = 0;
        }
        else
        {
            rear = (rear + 1) % capacity;
        }
        queue[rear] = value;
        size++;
        return true;
    }

    bool deleteFront()
    {
        if (isEmpty())
            return false;

        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front = (front + 1) % capacity;
        }
        size--;
        return true;
    }

    bool deleteLast()
    {
        if (isEmpty())
            return false;

        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            rear = (rear - 1 + capacity) % capacity;
        }
        size--;
        return true;
    }

    int getFront()
    {
        if (isEmpty())
            return -1;
        return queue[front];
    }

    int getRear()
    {
        if (isEmpty())
            return -1;
        return queue[rear];
    }

    bool isEmpty()
    {
        return size == 0;
    }

    bool isFull()
    {
        return size == capacity;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */