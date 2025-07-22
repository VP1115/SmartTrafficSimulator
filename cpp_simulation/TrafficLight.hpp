#ifndef TRAFFICLIGHT_HPP
#define TRAFFICLIGHT_HPP

enum class LightState { RED, GREEN };

class TrafficLight {
public:
    LightState state;
    double timer;
    double interval;

    TrafficLight(double interval);
    void update(double dt);
    void switchState();
};

#endif

