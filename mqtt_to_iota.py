# import paho.mqtt.client as mqtt
# from iota import Iota, TryteString, Tag, ProposedTransaction, Address
# import json
# import traceback

# # MQTT broker details
# broker = "localhost"
# port = 1883

# # IOTA node details
# iota_node = 'http://localhost:14265'
# seed = 'YFTPMLRQZNGK9POHHULUGCCEERTA9FGTDEQQDWQXPJXPL9HA9PCLYUCWCHGJSDGWLYWWQITEWBYQNTYMG'
# api = Iota(iota_node, seed)

# # Define the topics to subscribe to
# topics = [
#     "iot/simulated/temperature",
#     "iot/simulated/humidity",
#     "iot/simulated/light_intensity",
#     "iot/simulated/motion"
# ]

# # Callback function when a message is received
# def on_message(client, userdata, message):
#     try:
#         data = message.payload.decode()
#         print(f"Received message from topic {message.topic}: {data}")
#         forward_to_iota(data)
#     except Exception as e:
#         print(f"Error processing message: {e}")
#         print(traceback.format_exc())

# # Function to forward data to IOTA Tangle
# def forward_to_iota(data):
#     try:
#         print(f"Attempting to send data to IOTA: {data}")
#         message_trytes = TryteString.from_unicode(data)
#         tx = ProposedTransaction(
#             address=Address('YFTPMLRQZNGK9POHHULUGCCEERTA9FGTDEQQDWQXPJXPL9HA9PCLYUCWCHGJSDGWLYWWQITEWBYQNTYMG'),
#             message=message_trytes,
#             tag=Tag('IOTSIMULATOR'),
#             value=0
#         )
#         print("Transaction created, sending to node...")
#         try:
#             bundle = api.send_transfer(depth=3, transfers=[tx])
#             print(f'Transaction sent successfully. Bundle hash: {bundle["bundle"][0].hash}')
#         except Exception as send_error:
#             print(f"Error during send_transfer: {str(send_error)}")
#             print(f"Full error details: {traceback.format_exc()}")
#     except Exception as e:
#         print(f"Error preparing IOTA transaction: {str(e)}")
#         print("Full error traceback:")
#         print(traceback.format_exc())

# # Create an MQTT client instance
# client = mqtt.Client()

# # Attach the on_message callback function to the client
# client.on_message = on_message

# # Connect to the MQTT broker
# client.connect(broker, port)

# # Subscribe to the defined topics
# for topic in topics:
#     client.subscribe(topic)

# # Start the MQTT client loop to process incoming messages
# client.loop_start()

# # Keep the script running
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     client.loop_stop()
#     print("Script stopped.")

import paho.mqtt.client as mqtt
from iota import Iota, TryteString, Tag, ProposedTransaction, Address
import json
import traceback
import signal

# MQTT broker details
broker = "localhost"
port = 1883

# IOTA node details
iota_node = 'http://localhost:14265'
seed = 'YOUR_TEST_SEED_HERE'
api = Iota(iota_node, seed)

# Define the topics to subscribe to
topics = [
    "iot/simulated/temperature",
    "iot/simulated/humidity",
    "iot/simulated/light_intensity",
    "iot/simulated/motion"
]

# Callback function when a message is received
def on_message(client, userdata, message):
    try:
        data = message.payload.decode()
        print(f"Received message from topic {message.topic}: {data}")
        forward_to_iota(data)
    except Exception as e:
        print(f"Error processing message: {e}")
        print(traceback.format_exc())

# Function to forward data to IOTA Tangle
def forward_to_iota(data):
    try:
        print(f"Attempting to send data to IOTA: {data}")
        if not isinstance(data, str):
            raise ValueError("Incoming data must be a string")
        message_trytes = TryteString.from_unicode(data)
        tx = ProposedTransaction(
            address=Address('YFTPMLRQZNGK9POHHULUGCCEERTA9FGTDEQQDWQXPJXPL9HA9PCLYUCWCHGJSDGWLYWWQITEWBYQNTYMG'),
            message=message_trytes,
            tag=Tag('IOTSIMULATOR'),
            value=0
        )
        print("Transaction created, sending to node...")
        try:
            bundle = api.send_transfer(depth=3, transfers=[tx])
            print(f'Transaction sent successfully. Bundle hash: {bundle["bundle"][0].hash}')
            # Store the bundle hash for future reference
            with open('bundle_hashes.txt', 'a') as f:
                f.write(f"{bundle['bundle'][0].hash}\n")
        except Exception as send_error:
            print(f"Error during send_transfer: {str(send_error)}")
            print(f"Full error details: {traceback.format_exc()}")
    except Exception as e:
        print(f"Error preparing IOTA transaction: {str(e)}")
        print("Full error traceback:")
        print(traceback.format_exc())

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_message callback function to the client
client.on_message = on_message

# Connect to the MQTT broker
try:
    client.connect(broker, port)
    print("Connected to MQTT broker")
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")
    print(traceback.format_exc())
    exit(1)

# Subscribe to the defined topics
for topic in topics:
    client.subscribe(topic)
    print(f"Subscribed to topic: {topic}")

# Start the MQTT client loop to process incoming messages
client.loop_start()

# Set up signal handler to exit cleanly
def signal_handler(sig, frame):
    print("Received signal, stopping script")
    client.loop_stop()
    print("Script stopped.")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Keep the script running
while True:
    pass