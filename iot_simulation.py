import paho.mqtt.client as mqtt
import random
import time
import json

# MQTT broker details
broker = "localhost"
port = 1883

# Define topics for different sensors
topics = {
    "temperature": "iot/simulated/temperature",
    "humidity": "iot/simulated/humidity",
    "light_intensity": "iot/simulated/light_intensity",
    "motion": "iot/simulated/motion"
}

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker, port)

# Functions to generate random sensor data
def generate_temperature():
    return random.uniform(-10.0, 40.0)

def generate_humidity():
    return random.uniform(0.0, 100.0)

def generate_light_intensity():
    return random.uniform(0.0, 1000.0)

def generate_motion():
    return random.choice([True, False])

def simulate_iot_data():
    while True:
        # Generate and publish data for each sensor type
        for sensor, topic in topics.items():
            if sensor == "temperature":
                data = {"temperature": generate_temperature()}
            elif sensor == "humidity":
                data = {"humidity": generate_humidity()}
            elif sensor == "light_intensity":
                data = {"light_intensity": generate_light_intensity()}
            elif sensor == "motion":
                data = {"motion": generate_motion()}
            
            # Convert the data to JSON format
            data_json = json.dumps(data)
            # Publish the data to the corresponding MQTT topic
            client.publish(topic, data_json)
            print(f"Published: {data_json} to topic: {topic}")
        
        # Sleep for 5 seconds before publishing the next set of data
        time.sleep(5)

if __name__ == "__main__":
    simulate_iot_data()
