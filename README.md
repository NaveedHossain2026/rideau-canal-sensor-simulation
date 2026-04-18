# Rideau Canal IoT Sensor Simulator

## Overview

__What the simulator does__

This project is a high-fidelity Python-based IoT simulator that monitors environmental conditions along the Rideau Canal Skateway. It simulates three physical sensor nodes placed at key locations along the canal, generating real-time telemetry data on ice safety. The system supports data-driven decision-making for public safety and maintenance operations by providing continuous monitoring and analysis of ice conditions.

__Technologies Used__

- Language: Python 

- Connectivity: Azure IoT Device SDK 

- Concurrency: asyncio for simultaneous multi-device simulation.


## Prerequisites

Python 3.9 or higher installed.

An Azure IoT Hub with three registered devices (DowsLake, FifthAvenue, NAC).

## Installation

Clone the repository:

git clone [your-repo-link]

cd rideau-canal-sensor-simulation

Install the required libraries:

pip install -r requirements.txt

## Configuration

Create a .env file in the root directory

## Usage

To start the simulation, run:

python sensor_simulator.py

## Code Structure

### Main Components

__1. Locations List (LOCATIONS)__
   
A simple list that stores each sensor location and its Azure IoT connection details.

__2. Async Event Loop (asyncio)__
   
The “manager” of the program that runs multiple sensor tasks at the same time.

__3. Environment Loader (dotenv)__

Loads secure Azure credentials from a .env file instead of hardcoding them in the code.
