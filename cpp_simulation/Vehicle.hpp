#ifndef VEHICLE_HPP
#define VEHICLE_HPP

class Vehicle {
public:
    int id;
    double position;
    double speed;

    Vehicle(int id, double speed);
    void move(double dt);
};

#endif

