#ifndef ROAD_HPP
#define ROAD_HPP

#include <vector>
#include "Vehicle.hpp"

class Road {
public:
    double length;
    std::vector<Vehicle> vehicles;

    Road(double length);
    void update(double dt);
    void addVehicle(Vehicle v);
};

#endif

