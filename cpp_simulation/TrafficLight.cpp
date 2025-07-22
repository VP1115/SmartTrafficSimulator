#include "TrafficLight.hpp"

TrafficLight::TrafficLight(double interval)
    : state(LightState::RED), timer(0), interval(interval) {}

void TrafficLight::update(double dt) {
    timer += dt;
    if (timer >= interval) {
        switchState();
        timer = 0;
    }
}

void TrafficLight::switchState() {
    if (state == LightState::RED)
        state = LightState::GREEN;
    else
        state = LightState::RED;
}

