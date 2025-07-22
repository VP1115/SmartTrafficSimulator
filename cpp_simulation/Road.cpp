#include "Road.hpp"

Road::Road(double length) : length(length) {}

void Road::addVehicle(Vehicle v) {
    vehicles.push_back(v);
}

void Road::update(double dt) {
    for (auto& v : vehicles) {
        v.move(dt);
        if (v.position > length) v.position = 0; // loop back
    }
}

