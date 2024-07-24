class MyHashSet {
public:
    vector<list<int>> table;
    int large_prime = 10007;

    int hash(int key) {
        return key % large_prime;
    }

    MyHashSet() {
        table.resize(large_prime);
    }
    
    void add(int key) {
        int index = hash(key);
        for (auto iter = table[index].begin(); iter != table[index].end(); ++iter) {
            if (*iter == key) {
                return;         //key already exists
            }
        }
        table[index].push_back(key);
    }
    
    void remove(int key) {
        int index = hash(key);
        table[index].remove(key);
    }
    
    bool contains(int key) {
        int index = hash(key);
        for (auto iter = table[index].begin(); iter != table[index].end(); ++iter) {
            if (*iter == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */