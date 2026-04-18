import os
import time
import json
import random
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from azure.iot.device.aio import IoTHubDeviceClient

load_dotenv()

# Configuration for the three locations
LOCATIONS = [
    {"id": "DowsLake", "conn_str": os.getenv("CONN_STR_DOWS")},
    {"id": "FifthAve", "conn_str": os.getenv("CONN_STR_FIFTH")},
    {"id": "NAC", "conn_str": os.getenv("CONN_STR_NAC")}
]

async def send_telemetry(location):
    client = IoTHubDeviceClient.create_from_connection_string(location["conn_str"])
    await client.connect()
    print(f"Connected sensor: {location['id']}")

    try:
        while True:
            # Simulate realistic winter data
            data = {
                "deviceId": location["id"],
                "iceThickness": round(random.uniform(20.0, 40.0), 2),
                "surfaceTemp": round(random.uniform(-10.0, 2.0), 2),
                "snowAccumulation": round(random.uniform(0.0, 10.0), 2),
                "externalTemp": round(random.uniform(-20.0, -5.0), 2),
                "timestamp": datetime.utcnow().isoformat()
            }
            
            payload = json.dumps(data)
            print(f"Sending from {location['id']}: {payload}")
            
            await client.send_message(payload)
            await asyncio.sleep(10) # Frequency: 10 seconds
            
    except Exception as e:
        print(f"Error on {location['id']}: {e}")
    finally:
        await client.shutdown()

async def main():
    # Run all three sensors concurrently
    await asyncio.gather(
        send_telemetry(LOCATIONS[0]),
        send_telemetry(LOCATIONS[1]),
        send_telemetry(LOCATIONS[2])
    )

if __name__ == "__main__":
    asyncio.run(main())