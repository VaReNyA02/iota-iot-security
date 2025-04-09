import paho.mqtt.client as mqtt

# MQTT broker details
broker = "localhost"
port = 1883

# Define the topics to subscribe to
topics = [
    "iot/simulated/temperature",
    "iot/simulated/humidity",
    "iot/simulated/light_intensity",
    "iot/simulated/motion"
]

# Callback function when a message is received
def on_message(client, userdata, message):
    data = message.payload.decode()
    print(f"Received message from topic {message.topic}: {data}")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_message callback function to the client
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port)

# Subscribe to the defined topics
for topic in topics:
    client.subscribe(topic)

# Start the MQTT client loop to process incoming messages
client.loop_forever()
