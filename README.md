# IOTA IoT Security Simulation

This project demonstrates a secure data pipeline for an Internet of Things (IoT) environment using:
- **Python** scripts for data generation and forwarding
- **MQTT** for publish/subscribe messaging
- A Dockerized **IOTA Hornet Node** for decentralized data storage
- **Docker Compose** for simplified deployment

---

## 🚀 Features

1. **IoT Data Simulation**  
   - `iot_simulation.py`: Simulates sensor readings (e.g., temperature, humidity) and publishes them to designated MQTT topics.

2. **MQTT Subscriber**  
   - `mqtt_subscriber.py`: Subscribes to MQTT topics and prints incoming messages, useful for debugging data flow.

3. **MQTT to IOTA Forwarder**  
   - `mqtt_to_iota.py`: Receives IoT data via MQTT and forwards it to the IOTA Tangle by creating secure transactions.

4. **Seed & Address Generation**  
   - `generate_seed.py`: Dynamically generates an 81-character IOTA seed.
   - `generate_address.py`: Derives a new IOTA address from a given seed.

5. **Node Connectivity Testing**  
   - `node_test.py`: Tests connectivity to the IOTA node by fetching node information.

6. **Docker & Hornet Configuration**  
   - `docker-compose.yml`: Defines services to run a Hornet Node and an MQTT broker using Docker.
   - `config.json`: Provides the Hornet Node configuration (with public routes, P2P settings, etc.).

---

## 📂 Project Structure
## 🛠 Installation & Usage

1. **Clone the Repository**
   git clone https://github.com/VaReNyA02/iota-iot-security.git
   cd iota-iot-security

2. **Install Python Dependencies**
   pip install -r requirements.txt
  
3. **Start Docker Services**
   docker-compose up -
   
4. **Generate a Test Seed & Address**
   python generate_seed.py
   python generate_address.py

5. **Simulate IoT Data**
   python iot_simulation.py

6. **Subscribe to MQTT Topics**
   python mqtt_subscriber.py
   
7. **Forward Data to IOTA**
   python mqtt_to_iota.py
   
8. **Test IOTA Node Connectivity**
   python node_test.py


## 2. **Security & Disclaimers**
## 🔒 Security & Disclaimers

- **Seed Values:**  
  The code includes placeholder seeds (e.g., `"YOUR_TEST_SEED_HERE"`). Do not commit real production seeds in a public repository.

- **Configuration:**  
  This project is for demonstration and educational purposes only. No sensitive production data is exposed.

## 🔗 Useful Links

- [IOTA Developer Documentation](https://docs.iota.org/)
- [Shimmer Network Wiki](https://wiki.iota.org/shimmer)
- [Paho MQTT Python Client Documentation](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
- [Docker Documentation](https://docs.docker.com/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request with your changes.

## 🏆 Acknowledgments

- Thanks to the IOTA Foundation for their comprehensive documentation and support.
- Inspired by community projects focused on IoT security and distributed ledger integration.

   

