#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>
#include "Road.hpp"
#include "TrafficLight.hpp"   

int main() {
    Road road(100.0);
    road.addVehicle(Vehicle(1, 10.0));
    road.addVehicle(Vehicle(2, 12.0));
    TrafficLight light(5.0); // switch every 5 seconds

    std::ofstream file("traffic_data.csv");
    file << "Time,TrafficLight,VehicleID,Position\n"; // CSV header

    for (int t = 0; t < 20; ++t) {
        light.update(1.0);
        road.update(1.0);

        std::string lightColor = (light.state == LightState::GREEN) ? "GREEN" : "RED";

        for (auto& v : road.vehicles) {
            file << t << "," << lightColor << "," << v.id << "," << v.position << "\n";
        }

        std::cout << "Time: " << t << "s | Light: " << lightColor << "\n";
        for (auto& v : road.vehicles) {
            std::cout << "  Vehicle " << v.id << " position: " << v.position << "\n";
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }

    file.close();
    return 0;
}



