class ParkingSystem {
public:
    int big_space, medium_space, small_space;
    ParkingSystem(int big, int medium, int small) {
        big_space = big;
        medium_space = medium;
        small_space = small;
    }
    
    bool addCar(int carType) {
        switch (carType) {
            case 1:
                if (big_space > 0) {
                    big_space--;
                    return true;
                } else {
                    return false;
                }
            case 2:
                if (medium_space > 0) {
                    medium_space--;
                    return true;
                } else {
                    return false;
                }
            case 3:
                if (small_space > 0) {
                    small_space--;
                    return true;
                } else {
                    return false;
                }
        }
        return false;           //invalid car type
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */