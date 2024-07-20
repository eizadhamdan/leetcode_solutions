class MinStack {
public:
    int stack[100000000];
    int up = -1;
    int min;
    MinStack() {
        
    }
    
    void push(int val) {
        up++;
        stack[up] = val;

    }
    
    void pop() {
        up--;
    }
    
    int top() {
        if(up == -1)
            return -1;
        return stack[up];
    }
    
    int getMin() {
        min = stack[up];
        for(int i = 0; i < up; i++)
        {
            if(min > stack[i])
            {
                min = stack[i];
            }
        }
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */