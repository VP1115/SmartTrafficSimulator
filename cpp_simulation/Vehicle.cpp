#include "Vehicle.hpp"

Vehicle::Vehicle(int id, double speed)
    : id(id), speed(speed), position(0.0) {}

void Vehicle::move(double dt) {
    position += speed * dt;
}

