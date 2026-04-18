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

### Key Functions

__main() (Orchestrator)__

Starts the program and launches all three sensors at the same time using asyncio.gather().

__send_telemetry(location) (Sensor Worker)__

Connects to Azure IoT Hub, then continuously sends data every 10 seconds in a loop until the program is stopped.

__random.uniform() (Data Generator)__

Generates realistic fake sensor data by producing random values within a safe weather range (e.g., -10°C to 2°C) to simulate changing ice conditions.

## Sensor Data Format

{
    "location": "FifthAve",
    "windowEnd": "2026-04-16T05:05:00.0000000Z",
    "id": "FifthAve-2026-04-16T05:05:00.0000000Z",
    "avgIceThickness": 29.790666666666667,
    "minIceThickness": 20.29,
    "maxIceThickness": 39.86,
    "avgSurfaceTemp": -3.2676666666666674,
    "minSurfaceTemp": -9.62,
    "maxSurfaceTemp": 1.81,
    "maxSnowAccumulation": 9.3,
    "avgExternalTemp": -13.453666666666667,
    "readingCount": 30,
    "safetyStatus": "Caution",
    "_rid": "qUMFANvSf2IuAAAAAAAAAA==",
    "_self": "dbs/qUMFAA==/colls/qUMFANvSf2I=/docs/qUMFANvSf2IuAAAAAAAAAA==/",
    "_etag": "\"2000c088-0000-0a00-0000-69e06d9f0000\"",
    "_attachments": "attachments/",
    "_ts": 1776315807
}
